
## A Class to define the settings of the game like resolution and the background colour

class Settings():

	def __init__(self):
		
		self.screen_width = 900
		self.screen_height = 500
		self.screen_bg_colour = (230, 230, 230)
		self.ship_limit = 3
		
		# Bullet Attrinutes
		
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_colour = 60,60,60 # grey colour bulle
		self.bullet_allowed = 5

		# ALien Settings
		self.fleet_drop_speed = 10

		#How quickly the game speeds up

		self.speedup_scale = 1.1

		#How quickly alien point values increase

		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):

		''' Initialize the settings that change throught the game'''

		self.ship_speed_factor = 1.5

		self.bullet_speed_factor = 3 
		
		self.alien_speed_factor = 1
		
		# Fleet direction 1 represents Right, fleet direction -1 Left
		
		self.fleet_direction = 1

		#Every alien shot-down points
		
		self.alien_points = 50


	def increase_speed(self):
	
		'''Increase Speed Settings alien point values'''

		self.ship_speed_factor *= self.speedup_scale

		self.bullet_speed_factor *= self.speedup_scale

		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = (self.alien_points * self.score_scale)
		
		

		
