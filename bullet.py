import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self,ai_settings,screen,ship):
		super().__init__()
		self.screen=screen
		#create bullet rect from scratch
		self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
		self.rect.centerx=ship.rect.centerx
		self.rect.top=ship.rect.top
		#store the bullet position as decimal
		self.y=float(self.rect.y)
		
		self.color=ai_settings.bullet_color
		self.speed_factor=ai_settings.bullet_speed_factor
	def update(self):
		#move the bullet up to the screen
		self.y -= self.speed_factor
		self.rect.y=self.y
	def draw_bullet(self):
		"""draw bullet on to the screen"""
		pygame.draw.rect(self.screen,self.color,self.rect)
