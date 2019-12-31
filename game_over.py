import pygame
class GameOver():
	"""for game over """
	def __init__(self,screen):
		#load image and get its rect
		self.screen=screen
		self.image=pygame.image.load("images/game_over.bmp")
		self.rect=self.image.get_rect()
		self.screen_rect=self.screen.get_rect()
		
		#load the image at the center of screen
		
		self.rect.centerx=self.screen_rect.centerx
		self.rect.centery=self.screen_rect.centery
		#self.center=float(self.rect.centerx)
	
	def blitme(self):
		"""draw ship at its current location"""
		self.screen.fill((0,0,0))
		self.screen.blit(self.image,self.rect)
