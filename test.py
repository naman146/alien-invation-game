import pygame
import sys
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from game_over import GameOver
from button import Button
from scoreboard import Scoreboard

def run_game():
	#initialise pygame
	pygame.init()
	ai_settings=Settings()
	screen = pygame.display.set_mode((ai_settings.screen_height,ai_settings.screen_width))
	pygame.display.set_caption("alien invasion")
	#make a ship
	ship = Ship(ai_settings,screen)
	#make a group to store bullets
	bullets = Group()
	#make a group of alien
	aliens = Group()
	#create a fleet of aliens
	gf.create_fleet(ai_settings,screen,ship,aliens)
	#initialise ggame_Status
	stats=GameStats(ai_settings)
	#initialise game_over
	gameover=GameOver(screen)
	#initialise button
	play_button=Button(screen,"Play")
	#initialise scoreboard
	sb=Scoreboard(ai_settings,screen,stats)
	
	while True:
		#redraw the screen for every loop pass through
		gf.check_events(ai_settings,stats,screen,ship,aliens,bullets,play_button,sb)
		if stats.game_active:
			ship.update()
			bullets.update()
			gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets,sb)
			#deleting extra bullets
			gf.update_bullets(ai_settings,screen,stats,ship,aliens,bullets,sb)
		gf.update_screen(ai_settings,stats,screen,ship,aliens,bullets,gameover,play_button,sb)
			
run_game()
