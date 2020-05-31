#
#    ____             _     __       __            ____             _____            _     _   __                 
#   / __ )  __  __   (_)   / /  ____/ /   _____   / __ )   __  __  / ___/  ____ _   (_)   / | / /  ____ _   ____ _
#  / __  | / / / /  / /   / /  / __  /   / ___/  / __  |  / / / /  \__ \  / __ `/  / /   /  |/ /  / __ `/  / __ `/
# / /_/ / / /_/ /  / /   / /  / /_/ /   (__  )  / /_/ /  / /_/ /  ___/ / / /_/ /  / /   / /|  /  / /_/ /  / /_/ / 
#/_____/  \__,_/  /_/   /_/   \__,_/   /____/  /_____/   \__, /  /____/  \__,_/  /_/   /_/ |_/   \__,_/   \__, /  
#                                                       /____/                                           /____/   
#					SpaceInvaders
#			Developed and Maintained By SaiNag
#			 https://github.com/SainagGadangi


import pygame 
import random
screen=width,height =626, 626#854, 569

pygame.init()
window=pygame.display.set_mode(screen)
pygame.display.set_caption("SPACE INVADERS")
#GAME_ICON
icon=pygame.image.load('./images/icon.png') #64x64
pygame.display.set_icon(icon)





#PLAYER
player_img=pygame.image.load('./images/player2.png')#64x64
player_x=(width/2) -32
player_y=height-100
player_speed=5

player_score=100
font= pygame.font.Font('freesansbold.ttf', 32)
text_x= 30
text_y =10
collisions=3

def player(x,y):
	window.blit(player_img,(x,y))

#enemy---
enemy_img=pygame.image.load('./images/enemy.png')#64x64
enemy_x=random.randint(7,width-70)
enemy_y=4
enemy_speed=2
def enemy(x,y):
    global enemy_y, enemy_x, collisions
    enemy_y+=enemy_speed
    if enemy_y>=height-32:
        enemy_x=random.randint(7,width-70)
        enemy_y =4
        collisions-=1
    window.blit(enemy_img,(x,y))

#ready - -cant see it
#fire - -travelling
bullet_img=pygame.image.load('./images/bullet2.png') #24x24
bullet_x=0 
bullet_y=player_y - 24
bullet_speed=5
bullet_state='ready'
def fireBullet(x,y):
	global bullet_speed,bullet_state
	
	window.blit(bullet_img,(x,y))
	x=bullet_x
	y-=bullet_speed
#checking for collision
#enemy_x(x1),enemy_y(y1); player_x(x2), player_y(y2)

def isCollided(enemy_x, enemy_y, player_x, player_y):
	distance=((enemy_x - player_x)**2 + (enemy_y - player_y)**2)**(1/2)
	if distance < 64:
		return True 
	else:
		return False
	
def isDestroyed(enemy_x, enemy_y, bullet_x, bullet_y):
	global player_score
	distance1=	((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2)**(1/2)
	if distance1 <32:
		return True
	else:
		return False


def show_score(x,y):
	score= font.render("Score: " + str(player_score), True, (255,255,255))
	window.blit(score, (x,y))


over_font= pygame.font.Font('freesansbold.ttf', 64)
def game_over(x,y):
	over_text= over_font.render("GAME OVER", True , (255,255,255))
	window.blit(over_text, (x,y))


#background
bg_img= pygame.image.load('./images/back2.jpg')
clock=pygame.time.Clock()
run=True
while run:
	clock.tick(120)
	
	window.fill((0,0,0))
	window.blit(bg_img, (0,0))
	show_score(text_x,text_y)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run=False

	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and player_x>=0:
		player_x-=player_speed
	if keys[pygame.K_RIGHT] and player_x<=width-64:
		player_x+=player_speed
	if keys[pygame.K_SPACE]  or keys[pygame.K_KP0]and bullet_y==player_y-24:
		#if bullet_state== 'ready':
		bullet_state='fire'
		bullet_x=player_x+32-12
		fireBullet(bullet_x,bullet_y)
	if bullet_state=='fire' :
		if bullet_y>0:
			fireBullet(bullet_x,bullet_y)
			bullet_y-=bullet_speed
		if bullet_y <4  :
			bullet_state='ready'
			bullet_y= player_y-24


	
	collision=isCollided(enemy_x+32, enemy_y+32, player_x+32, player_y+32)
	if collision:
		enemy_x=random.randint(7,width-70)
		enemy_y =4
		
		collisions-=1
		
		
	destroyed=isDestroyed(enemy_x+32, enemy_y +32, bullet_x + 12, bullet_y)
	if destroyed:
		player_score+=1
		enemy_x=random.randint(7,width-70)
		enemy_y =4
		bullet_state='ready'
		bullet_y= player_y-24
		
	enemy(enemy_x,enemy_y)
	if collision:
		for i in range(4):
			window.blit(bg_img, (0,0))
			pygame.time.delay(100)
			player(player_x,player_y)
			pygame.display.flip()

	player(player_x,player_y)
	
	if collisions==0 :
		game_over(130, (height/2) - 32)
		pygame.display.update()
		pygame.time.delay(4000)
		run = False
	pygame.display.update()
print("player_score: ", player_score)
pygame.quit()

