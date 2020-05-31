import pygame 
import random
screen=width,height = 700, 500

pygame.init()
window=pygame.display.set_mode(screen)
pygame.display.set_caption("SPACE SHIT")
#GAME_ICON
icon=pygame.image.load('icon.png') #64x64
pygame.display.set_icon(icon)

#PLAYER
player_img=pygame.image.load('player.png')#64x64
player_x=(width/2) -32
player_y=height-100
player_speed=5

def player(x,y):
    window.blit(player_img,(x,y))

#enemy
enemy_img=pygame.image.load('enemy.png')#64x64
enemy_x=random.randint(7,width-70)
enemy_y=4
enemy_speed=2
def enemy(x,y):
    global enemy_y, enemy_x
    enemy_y+=enemy_speed
    if enemy_y>=height-64:
        enemy_x=random.randint(7,width-70)
        enemy_y =4
    window.blit(enemy_img,(x,y))

#ready - -cant see it
#fire - -travelling
bullet_img=pygame.image.load('bullet.png')
bullet_x=0 
bullet_y=player_y - 24
bullet_speed=5
bullet_state='ready'
def fireBullet(x,y):
	global bullet_speed,bullet_state
	
	window.blit(bullet_img,(x,y))
	x=bullet_x
	y-=bullet_speed
	


clock=pygame.time.Clock()
run=True
while run:
    clock.tick(120)
    
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x>=0:
    	player_x-=player_speed
    if keys[pygame.K_RIGHT] and player_x<=width-64:
    	player_x+=player_speed
    if keys[pygame.K_SPACE] and bullet_y==player_y-24:
    	#if bullet_state== 'ready':
    	bullet_state='fire'
    	bullet_x=player_x+32-12
    	fireBullet(bullet_x,bullet_y)
    if bullet_state=='fire' and bullet_y>0:
    	fireBullet(bullet_x,bullet_y)
    	bullet_y-=bullet_speed
    if bullet_state== 'fire' and bullet_y <4  :
    	bullet_state='ready'
    	bullet_y= player_y-24


    enemy(enemy_x,enemy_y)
    
    player(player_x,player_y)
    pygame.display.update()

pygame.quit()

