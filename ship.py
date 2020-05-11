
import pygame

from pygame.sprite import Sprite

class Ship(Sprite):

	def __init__(self,ai_settings, screen):

		super().__init__()
		
		self.screen = screen # store the screen
	
		self.ai_settings = ai_settings 

		#Load the ship image  
		self.image = pygame.image.load('Images/ship.bmp')
	
		# Create a rectangular ship image
		self.rect = self.image.get_rect()

		#Create a rectangular screen
		self.screen_rect = self.screen.get_rect()

		#Start each ship at bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#Store the decimal value for the Ship center
		self.center = float(self.rect.centerx)
	
		
 
		#Right  Movement flag
		self.move_right = False

		# Left Movement flaf
		self.move_left = False 

	def update(self):
		''' Updating the movement flag if the key is kept pressed '''
		# Right Edge	
		if self.move_right and self.rect.right < self.screen_rect.right:
			# Update the ship center position; Increment (right)
			self.center += self.ai_settings.ship_speed_factor
		# Left edge
		if self.move_left and self.rect.left > 0:
			# Update the ship center position; Decrement (left)
			self.center -= self.ai_settings.ship_speed_factor
		
		#Update the ship_center to rect
		self.rect.centerx = self.center

	def blitme(self):
		
		self.screen.blit(self.image, self.rect)


	def center_ship(self):

		self.center = self.screen_rect.centerx




