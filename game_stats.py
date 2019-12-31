class GameStats():
	"""this is to record the status of a game"""
		
	def __init__(self,ai_settings):
		self.ai_settings=ai_settings
		self.reset_stats()
		self.game_active=False
		self.high_score = 0
	
	def reset_stats(self):
		"""initialise stats so that it can chnage throuout the game"""
		self.ship_left=self.ai_settings.ship_limit
		self.score = 0
		self.level=1
