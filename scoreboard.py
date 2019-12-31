import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
	def __init__(self,ai_settings,screen,stats):
		self.ai_settings=ai_settings
		self.screen=screen
		self.stats=stats
		self.screen_rect=self.screen.get_rect()
		#font setting for score storing
		self.text_color=(30,30,30)
		self.font=pygame.font.SysFont(None,30)
		#preparing the score
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ship()
		
	def prep_score(self):
		"""to turn the score into a render image"""
		rounded_score=int(round(self.stats.score,-1))
		self.score_str="Score "+"{:,}".format(rounded_score)
		self.score_img=self.font.render(self.score_str,True,self.text_color,self.ai_settings.bg_color)
		self.score_rect=self.score_img.get_rect()
		self.score_rect.top=self.screen_rect.top
		self.score_rect.centerx=self.screen_rect.centerx -30
		
	def prep_high_score(self):
		self.high_score=int(round(self.stats.high_score,-1))
		self.high_score_str="High Score "+"{:,}".format(self.high_score)
		self.high_score_img=self.font.render(self.high_score_str,True,self.text_color,self.ai_settings.bg_color)
		self.high_score_rect=self.high_score_img.get_rect()
		self.high_score_rect.top=self.screen_rect.top
		self.high_score_rect.right=self.screen_rect.right -20
		
	def prep_level(self):
		self.level_str="level "+str(+self.stats.level)
		self.level_img=self.font.render(self.level_str,True,self.text_color,self.ai_settings.bg_color)
		self.level_rect=self.level_img.get_rect()
		self.level_rect.right=self.screen_rect.right -20
		self.level_rect.top=self.high_score_rect.bottom +10
	
	def prep_ship(self):
		self.ships = Group()
		for ship_number in range(self.stats.ship_left):
			ship = Ship(self.ai_settings,self.screen)
			ship.rect.x=10+ ship_number*ship.rect.width
			ship.rect.y=10
			self.ships.add(ship)
		
	def show_score(self):
		self.screen.blit(self.score_img,self.score_rect)
		self.screen.blit(self.high_score_img,self.high_score_rect)
		self.screen.blit(self.level_img,self.level_rect)
		#drwa ships
		self.ships.draw(self.screen)
