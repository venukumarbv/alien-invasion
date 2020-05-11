
import pygame

from Settings import Settings

from ship import Ship

import game_functions as gf

from pygame.sprite import Group

from game_stats import GameStats

from button import Button

from scoreboard import Scoreboard


def run_game():

	pygame.init() #initializing the pygame
	
	#assign the class Settings to the object ai_settings
	ai_settings = Settings()

	#Surface objecr screen
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) 
	

	# Setting caption for the game	
	pygame.display.set_caption("VK Games")

	#Make the Play_button
	
	play_button = Button(ai_settings, screen, "Play")

	#Make ship
	ship = Ship(ai_settings, screen)

	#Make a Group to store bullets
	bullets = Group()

	#Make a Group to store aliens

	aliens = Group()
	
	#Create the fleet of aliens

	gf.create_fleet(ai_settings,screen,ship, aliens )

	#Create an instance to store game statistics and create a scoreboard
	
	stats = GameStats(ai_settings)

	sb = Scoreboard(ai_settings, screen, stats)

	while True:
		
		# check for events
		gf.check_events(ai_settings,screen,stats,sb, play_button, ship,aliens, bullets)

		if stats.game_active:
			#ship Update
			ship.update()
		
			bullets.update()
		
			gf.update_bullets(ai_settings, screen,stats, sb, ship, aliens,bullets)

			gf.update_aliens(ai_settings,stats,screen,sb, ship, aliens,bullets)
	
		#Updating the screen
		gf.update_screen(ai_settings, screen,stats, sb, ship,aliens, bullets,play_button)

run_game()
				

