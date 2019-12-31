import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
	def __init__(self,ai_settings,screen):
		"""initialise the ship and set its starting position"""
		super().__init__()
		self.screen=screen
		self.ai_settings=ai_settings
		
		#load the ship image and gets its rectangle
		self.image=pygame.image.load('images/ship.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=self.screen.get_rect()
		
		#start with new ship at bottom of the screen
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom
		self.center=float(self.rect.centerx)
		
		#movement flag
		self.moving_right=False
		self.moving_left=False
			
	def blitme(self):
		"""draw ship at its current location"""
		self.screen.blit(self.image,self.rect)
		
	def update(self):
		"""update the ship position based on flag"""
		#update ship center value not the rect
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.center+=self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left>0:
			self.center-=self.ai_settings.ship_speed_factor
		#update rect object from centerx
		self.rect.centerx=self.center
	
	def center_ship(self):
		"""center the ship"""
		self.center=self.screen_rect.centerx
