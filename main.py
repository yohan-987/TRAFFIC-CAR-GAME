import pygame
import random

pygame.init()
font = pygame.font.Font(None, 50)
clock=pygame.time.Clock()

screen=pygame.display.set_mode((1000,700))
pygame.display.set_caption("YOHANNN")
background=pygame.image.load("assets/background/background-1_2.png")
background=pygame.transform.scale(background,(1000,700))  
bg_Y1=0.0
bg_Y2=-700.0
scroll_speed = 3.0

#----Player Data----#
playerImage=pygame.image.load("assets/player/Pcar.png")
playerImage=pygame.transform.scale(playerImage,(150,150))
playerX=370
playerY=480
player_Xchange=0
player_Ychange=0

#----ENEMY DATA----#
enemy_images = [
    pygame.transform.scale(pygame.image.load("assets/enemy/E1.png"), (125,150)),
    pygame.transform.scale(pygame.image.load("assets/enemy/E2.png"), (125,150)),
    pygame.transform.scale(pygame.image.load("assets/enemy/E3.png"), (125,150)),
    pygame.transform.scale(pygame.image.load("assets/enemy/E4.png"), (125,150)),
    pygame.transform.scale(pygame.image.load("assets/enemy/E5.png"), (125,150)),
    pygame.transform.scale(pygame.image.load("assets/enemy/E6.png"), (125,150)),]

enemies=[]


sleep_timer=0
sleep_every=60

#collison 
def collision(playerX,playerY,enemyX,enemyY):
    playerRect=pygame.Rect(playerX,playerY,70,90)
    enemyRect=pygame.Rect(enemyX,enemyY,70,90)
    player_collision=playerRect.colliderect(enemyRect)
    if player_collision:
         return True


def player(playerX,playerY):
    screen.blit(playerImage,(playerX,playerY))
def playermove(playerX,player_Xchange,playerY,player_Ychange):
        playerX+=player_Xchange
        playerY+=player_Ychange
        if playerX>=730:
            playerX=730
        if playerX<=120:
            playerX=120
        if playerY<=0:
            playerY=0
        if playerY>=550:
            playerY=550
        return playerX ,playerY
#def background():

def spawn_enemy(enemies):
    lanes = [195, 335, 495, 655]
    x = random.choice(lanes)
    y = -150
    img = random.choice(enemy_images)
    enemies.append([x, y, img])

def update_enemies(enemies, speed):
    for enemy in enemies[:]:  # Create copy to iterate safely
        enemy[1] += speed
        if enemy[1] > 700:
            enemies.remove(enemy)
        else:
            screen.blit(enemy[2], (enemy[0], enemy[1]))     
def game_over(st,end):
    enemies.clear()
    background=pygame.image.load("assets/background/background-1_2.png")
    background=pygame.transform.scale(background,(1000,700))
    screen.blit(background,(0,0))
    pygame.display.update()
    start_time=pygame.time.get_ticks()
    while pygame.time.get_ticks()-start_time<1000:
        pygame.event.get()
        pygame.time.delay(10)
    waiting=True
    while waiting:
           time=(end-st)/1000
           score=font.render(f"You survided for {time}",True,(0,0,0))
           screen.blit(score,(300,200))
           gg=font.render("GAME OVER",True,(0,0,0))
           screen.blit(gg,(300,300))
           restart_msg = font.render("Press any key to restart", True, (0,0,0))
           screen.blit(restart_msg, (300, 400))
           pygame.display.update()
           for event in pygame.event.get():
               if event.type==pygame.QUIT:
                   pygame.quit()
                   exit()
               if event.type==pygame.KEYDOWN:
                   RE=True
                   waiting=True
                   return RE



 #   enemyImage=pygame.image.load("Ecar.png")
   # enemyImage= pygame.transform.scale(enemyImage, (150,150))
def logic():
    global player_Xchange,playerX,playerY,player_Ychange
    global enemies,enemyImage
    global bg_Y1,bg_Y2,background,scroll_speed,sleep_timer,sleep_every
    running=True
    count=0
    st=pygame.time.get_ticks()
    while running:
        if count>0:
            count=0
            st=0
            st=pygame.time.get_ticks()
            
        clock.tick(60)
        screen.fill((0,0,0))
       # screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        #backgroung

        bg_Y1+=scroll_speed
        bg_Y2+=scroll_speed
        if bg_Y1>=700:
            bg_Y1=bg_Y2-700.0
        if bg_Y2>=700:
            bg_Y2=bg_Y1-700.0

        keys=pygame.key.get_pressed()
        player_Xchange=0
        player_Ychange=0
        if keys[pygame.K_a]:
            player_Xchange-=5
        if keys[pygame.K_d]:
            player_Xchange+=5
        if keys[pygame.K_w]:
            player_Ychange-=5
            scroll_speed=7
        elif keys[pygame.K_s]:
            player_Ychange+=5
            scroll_speed=3
       # elif keys[pygame.K_SPACE]:
            
        #    scroll_speed-=1
        else:
            scroll_speed=5
        # ----PLayer movement----#
        playerX,playerY=playermove(playerX,player_Xchange,playerY,player_Ychange)

        
       
        sleep_timer += 1
        if sleep_timer >= sleep_every:
            sleep_timer = 0
            spawn_enemy(enemies)



         #   screen.blit(enemyImage,(enemyX,enemyY))




        screen.blit(background,(0,int(bg_Y1)))
        screen.blit(background,(0,int(bg_Y2)))
      #  screen.blit(enemyImage,(655,70))


              # ----- Enemy update -----
        speedENEMY=7
        update_enemies(enemies, speedENEMY)
        player(playerX,playerY)
        for enemy in enemies:
            if collision(playerX,playerY,enemy[0],enemy[1]):
                RE=False
                end=pygame.time.get_ticks()
                RE=game_over(st,end)
                if RE:
                                       
                   playerX=370
                   playerY=480
                   player_Xchange=0
                   player_Ychange=0
                   bg_Y1=0.0
                   bg_Y2=-700.0
                   scroll_speed = 3.0
                   count=1
                   end=0
                   continue

                
        pygame.display.update()
        
logic()
pygame.quit()
