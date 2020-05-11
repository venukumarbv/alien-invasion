
class GameStats():
	'''Tracking statistics for alien invasion'''

	def __init__(self,ai_settings):
		'''Initialize statistics.'''

		self.ai_settings = ai_settings
		self.reset_stats()
		
		#Start alien invsion in an active FLAG
		self.game_active = False
		
		#High score
		
		self.high_score = 0

	def reset_stats(self):
		
		self.ships_left = self.ai_settings.ship_limit 

		self.score = 0

		self.level = 1


