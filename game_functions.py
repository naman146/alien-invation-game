import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	if event.key==pygame.K_q:
		sys.exit()
	elif event.key==pygame.K_RIGHT:
		#move the ship towards right
		ship.moving_right=True
	elif event.key==pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	elif event.key==pygame.K_LEFT:
		#move the ship towards left
		ship.moving_left=True
		
def check_keyup_events(event,ship):
	if event.key==pygame.K_RIGHT:
		ship.moving_right=False
	if event.key==pygame.K_LEFT:
		ship.moving_left=False
		
def check_events(ai_settings,stats,screen,ship,aliens,bullets,play_button,sb):
	"""to control keyboard and mouse events"""
	for event in pygame.event.get():
		if event.type==pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type==pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y=pygame.mouse.get_pos()
			check_play_button(ai_settings,stats,screen,ship,aliens,bullets,play_button,mouse_x,mouse_y,sb)					
		elif event.type==pygame.KEYUP:
			check_keyup_events(event,ship)

def check_play_button(ai_settings,stats,screen,ship,aliens,bullets,play_button,mouse_x,mouse_y,sb):
	"""start a new game if user presses play button"""
	if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
		ai_settings.initialise_dynamic_settings()
		pygame.mouse.set_visible(False)
		stats.game_active=True
		
		#empty the list of aliens
		aliens.empty()
		bullets.empty()
		stats.reset_stats()
		sb.prep_score()
		sb.prep_level()
		sb.prep_ship()
		
		#create a new fleet
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()
				
def update_screen(ai_settings,stats, screen, ship, aliens, bullets,gameover,play_button,sb):
	#update images on screen and flips the screen"""
	screen.fill(ai_settings.bg_color)
	#redraw bullets behind ship and alien
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	#display ship
	ship.blitme()
	#display alien
	aliens.draw(screen)
	#display score
	sb.show_score()
	#if game_active is false then gameover
	if not stats.game_active:
		if stats.ship_left==0:
			gameover.blitme()
		play_button.draw_button()
		
		#pygame.display.flip()
		#sleep(5)
		#sys.exit()
	#make the most recent screen draw
	pygame.display.flip()
def update_bullets(ai_settings,screen,stats,ship,aliens,bullets,sb):
	"""to delete the bullets"""
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom<=0:
			bullets.remove(bullet)
	check_bullet_alien_collisions(ai_settings,screen,stats,ship,aliens,bullets,sb)

def fire_bullet(ai_settings,screen,ship,bullets):
	#create a new bullet and store it in group
		new_bullet=Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)

def create_fleet(ai_settings,screen,ship,aliens):
	"""creating fleet of aliens"""
	#create a alien and find number of aliens in a row
	#apacing between aliens is equal to 10
	alien=Alien(ai_settings,screen)
	number_aliens_x=get_number_alien_x(ai_settings,alien.rect.width)
	number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
	
	for row_number in range(number_rows):
		#create the first row of aliens
		for alien_number in range(number_aliens_x):
			#create a alien
			create_alien(ai_settings,screen,aliens,alien_number,row_number)
		
def get_number_alien_x(ai_settings,alien_width):
	"""determine the number of aliens that fit in a row"""
	available_space_x=ai_settings.screen_width-(alien_width)
	number_aliens_x=int(available_space_x / (alien_width))
	return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	"""create an alienand place it in a row"""
	alien=Alien(ai_settings,screen)
	alien_width=alien.rect.width
	#alien_height=alien.rect.height
	#alien=Alien(ai_settings,screen)
	alien.x=alien_width + (2 * alien_width)*alien_number
	alien.rect.x = alien.x
	alien.y = alien.rect.height + (alien.rect.height) * row_number
	alien.rect.y=alien.y
	aliens.add(alien)

def get_number_rows(ai_settings,ship_height,alien_height):
	"""describing the number of rows"""
	available_space_y = ai_settings.screen_height - (4*alien_height) - (4*ship_height)
	number_rows = int(available_space_y / (2*alien_height))
	return number_rows

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb):
	"""respond to ship being hit by aliens"""
	if stats.ship_left >0:
		#decrement ship left
		stats.ship_left -=1
		#empty the list of aliens and bullets
		aliens.empty()
		bullets.empty()
		#create a new fleet and cenetr the ship
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()
		#prepare left ships
		sb.prep_ship()
		#pause
		sleep(2)
	else:
		stats.game_active =False
		pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,sb):
	screen_rect=screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb)
			break

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets,sb):
	"""move aliens group to right"""
	check_fleet_edges(ai_settings,aliens)
	aliens.update()
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb)
	check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,sb)

def check_fleet_edges(ai_settings,aliens):
	"""respond if any alien has reched edges"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break

def change_fleet_direction(ai_settings,aliens):
	"""change the direction of alien if it has reached edges"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1
			
def check_bullet_alien_collisions(ai_settings,screen,stats,ship,aliens,bullets,sb):
	#to che k if any bullet has collided with alien
	#if yes then delete the bullet and alien
	collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_point * len(aliens)
			sb.prep_score()
		chech_high_score(stats,sb)
	#reate new fleet when one is destroyed
	if len(aliens)==0:
		#destroy exixting bullets, speed up game,create new fleet
		bullets.empty()
		ai_settings.increase_speed()
		create_fleet(ai_settings,screen,ship,aliens)
		#increse the level
		stats.level +=1
		sb.prep_level()
		
def chech_high_score(stats,sb):
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()
