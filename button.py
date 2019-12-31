import pygame.font

class Button():
	def __init__(self,screen,msg):
		#initialise parameter
		self.screen=screen
		self.screen_rect=self.screen.get_rect()
		
		#create button body
		self.width,self.height=200,50
		self.button_color=(0,0,0)
		self.text_color=(255,255,255)
		self.font=pygame.font.SysFont(None,48)
		
		#build the buttons rect and center it
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.center=(600,200)
		
		#buttons msg needs to be prep only once
		self.prep_msg(msg)
	
	def prep_msg(self,msg):
		"""turn msg into a rendering image"""
		self.image_msg=self.font.render(msg,True,self.text_color,self.button_color)
		self.image_rect=self.image_msg.get_rect()
		self.image_rect.center=(600,200)
		
	def draw_button(self):
		#draw the button to screen
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.image_msg,self.image_rect)
