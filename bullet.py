
import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
	''' A class to manage bullets fired by the ship '''
	
	def __init__(self, ai_settings,screen, ship):
	
		super(Bullet, self).__init__() # include the __init__() of the superclass Spirit
		self.screen = screen
	
		# Creating bullet rect from the scratch
		self.rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height)
		
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		# Store the bullet position in decimal values
		self.y = float(self.rect.y)

		self.colour = ai_settings.bullet_colour
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		'''Move the bullets up the screen'''
	
		self.y -= self.speed_factor
	
		self.rect.y = self.y

	def draw_bullet(self):
		'''Draw the bullet on the screen '''

		pygame.draw.rect(self.screen, self.colour, self.rect)
		
