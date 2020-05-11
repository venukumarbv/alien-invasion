import pygame 

from pygame.sprite import Sprite

class Alien(Sprite):
	''' A Class to represent single alien in the fleet'''

	def __init__(self, ai_settings, screen):
		
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings
	
		#Load the Alien image and set it's rect attributes
		self.image = pygame.image.load('Images/alien.bmp')
		self.rect = self.image.get_rect()
		
		# Start the first alien at top-left corner
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the alien in exact position
		self.x = float(self.rect.x)

	def blitme(self):
		'''Draw the alien at current position'''
	
		self.screen.blit(self.image, self.rect)
		
	def check_edges(self):
	
		screen_rect = self.screen.get_rect()

		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True

	def update(self):
	
		self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x	

