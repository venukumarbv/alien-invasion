
import pygame

import sys

from bullet import Bullet

from alien import Alien

from time import sleep

def check_keydown_events(event,ai_settings, screen, ship, bullets):

	# Check for the Right key
	if event.key == pygame.K_RIGHT:
        	#Update the Right movement flag
		 ship.move_right = True
	
         # Check for the Left key
	if event.key == pygame.K_LEFT:
         	#Update the left movement flag
        	ship.move_left = True
	
	# Firing the bullets
	elif event.key == pygame.K_SPACE:
		fire_bullets(ai_settings, screen,ship,bullets)

	# Quit the game if Q/q is pressed
	
	elif event.key == pygame.K_q:
		sys.exit()

	

def fire_bullets(ai_settings,screen,ship,bullets):

	if len(bullets) < ai_settings.bullet_allowed:		
		new_bullet = Bullet(ai_settings,screen, ship)
		bullets.add(new_bullet)

def check_keyup_events(event, ship):

	# if released kry is Right arrow
	if event.key == pygame.K_RIGHT:
		ship.move_right = False

	# if the released key is Left arrow
	if event.key == pygame.K_LEFT:
		ship.move_left = False

def check_events(ai_settings,screen,stats,sb, play_button, ship,aliens, bullets):
	'''  Watch keyboard or mouse events '''
	for event in pygame.event.get():

		# Check for quit botton press
		if event.type == pygame.QUIT:
			sys.exit()

		# Check for mouse button pressed on play button
		
		elif event.type == pygame.MOUSEBUTTONDOWN:
			
			mouse_x, mouse_y = pygame.mouse.get_pos()
			
			check_play_button(ai_settings, screen, stats,sb, play_button,ship,aliens, bullets, mouse_x, mouse_y)
	
		# Check for the key Pressed 	
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen, ship,bullets)
			

		# Check for key released 
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)			


def update_screen(ai_settings, screen,stats,sb, ship, aliens, bullets, play_button):
	'''Update the images on the screen and flip the screen'''
	
	# Change the background colour 
	screen.fill(ai_settings.screen_bg_colour)

	#Redraw new bullets behind ship and aliens

	for bullet in bullets.sprites():
		bullet.draw_bullet()

	#call ship; display ship on the center of the screen
	ship.blitme()

	aliens.draw(screen)

	#Draw the score information

	sb.show_score()

	#Draw the play_button only if the game is inactive

	if not stats.game_active:
		play_button.draw_button()

	#flip the screen everytime
	pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
	# Deleting the bullets that have disappeared
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	print(len(bullets))
	check_bullet_alien_collision (ai_settings,screen,stats, sb, ship,aliens,bullets)

def check_bullet_alien_collision (ai_settings,screen,stats, sb, ship,aliens,bullets):
	#check for any bullets that have hit aliens.
	#If so, get rid of the alien and bullet

	collisions = pygame.sprite.groupcollide(bullets, aliens,True,True)

	if collisions:

		for aliens in collisions.values():

			stats.score += ai_settings.alien_points * len(aliens)

			sb.prep_score()

		check_high_score(stats, sb)

	if len(aliens) ==0:
		#Destroy existing bullets speed up the game and create a new fleet and new level
		bullets.empty()

		ai_settings.increase_speed()

		# Incerease the Level
	
		stats.level += 1

		sb.prep_level()
		
		create_fleet(ai_settings, screen, ship, aliens)

		


def get_number_rows(ai_settings, ship_height, alien_height):

	available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)

	number_rows = int(available_space_y / (2 * alien_height))

	return number_rows


def get_number_aliens_x(ai_settings, alien_width):


	available_space_x = ai_settings.screen_width - 2 * alien_width

	number_aliens_x = int(available_space_x / (2 * alien_width))
	
	return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number, row_number):

	alien = Alien(ai_settings, screen)

	alien_width = alien.rect.width

	alien.x = alien_width + 2 * alien_width * alien_number

	alien.rect.x = alien.x

	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number

	aliens.add(alien)

def create_fleet(ai_settings, screen,ship, aliens):
	'''Create a full fleet of aliens'''

	#Create an alien and findout how maany aliens in a row
	#Spacing between aliens is of one alien width
	
	alien = Alien(ai_settings, screen)
	
	number_aliens_x =get_number_aliens_x(ai_settings, alien.rect.width)

	number_rows = get_number_rows(ai_settings, ship.rect.height,alien.rect.height)
	#create a first row of aliens
	

	for row_number in range(number_rows):	
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen,aliens,alien_number,row_number)


def check_fleet_edges(ai_settings, aliens):
	'''Respond appropriately if any alien has reached the edge'''
	
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):

	'''Drop the entire fleet and change the fleet direction'''
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1


def update_aliens(ai_settings,stats,screen,sb, ship, aliens,bullets):
	'''Update the position of all aliens of the fleet'''

	check_fleet_edges(ai_settings, aliens)

	aliens.update()

	#look for alien-ship collision

	if pygame.sprite.spritecollideany(ship, aliens):
		
		#print("Ship Hit!!")
		ship_hit(ai_settings, stats, screen,sb, ship, aliens, bullets)
	
	check_aliens_bottom(ai_settings, stats, screen,sb, ship, aliens, bullets)

def ship_hit(ai_settings, stats, screen, sb,ship, aliens, bullets):
	'''Respond to ship being hit by aliens'''
	
	if stats.ships_left > 0 :
		#Decrement the ships left
		stats.ships_left -= 1

		#Update Score board

		sb.prep_ships()

		#Empty the list of aliens and bullets
		aliens.empty()
		bullets.empty()

		#create a new fleet at the center of the screen
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()

		#pause
		sleep(1)

	else:
		stats.game_active = False

		pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):

	'''Check if any aliens have reached the bottom of the screen'''

	screen_rect = screen.get_rect()

	for alien in aliens.sprites() :
	
		if alien.rect.bottom >= screen_rect.bottom:
		
			#Treat this as ship got hit
			
			ship_hit(ai_settings, stats, screen,sb, ship, aliens, bullets)
			break

def check_play_button(ai_settings, screen, stats,sb, play_button,ship,aliens, bullets, mouse_x, mouse_y):

	'''Start a new game when a play player cliscks Play'''

	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

	if button_clicked and not stats.game_active:

		# Reset the game settings, alien,ship,bullet speeds 
	
		ai_settings.initialize_dynamic_settings()

		#Hide the mouse button

		pygame.mouse.set_visible(False)

		#Reset the game statsitics

		stats.reset_stats()

		stats.game_active = True


		#Reset the scoreboard image

		sb.prep_score()
		
		sb.prep_high_score()

		sb.prep_level()

		sb.prep_ships()

		#Empty list of aliens and bullets
	
		aliens.empty()
	
		bullets.empty()

	
		#Create a new fleet and center the ship
		
		create_fleet(ai_settings, screen, ship, aliens)	

		ship.center_ship()
		


def check_high_score(stats, sb):
	
	'''check if there is new High score'''

	if stats.score > stats.high_score:

		stats.high_score = stats.score

		sb.prep_high_score()
























