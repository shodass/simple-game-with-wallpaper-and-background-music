import pygame
import random

score=0
red=(255,0,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)

pygame.init()

speed=5
width=1080
height=700

font=pygame.font.SysFont("bitstreamverasans",50)
game_over=False
screen_ratio=(width,height)

my_size=50
enemy_size=my_size
enemy_y=0
enemy_x=400
enemy_pos=[enemy_x,enemy_y,enemy_size,enemy_size]
enemy_list=[enemy_pos]
my_x=600
my_y=540

time=pygame.time.Clock()
screen=pygame.display.set_mode(screen_ratio)
pygame.mixer.init()
pygame.mixer.music.load("m1.mp3") 
pygame.mixer.music.play(-1,0.0)

def levels(score,speed):
    if score< 10:
        speed=5
    elif score< 20:
        speed=10
    elif score<30:
        speed=15
    elif score<40:
        speed=20
    elif score<100:
        speed=25
    elif score<200:
        speed=30
    elif score<250:
        speed=45
    else:
        speed=55
    return speed
    
def enemies(enemy_list):
    time_delay=random.random()
    if len(enemy_list)< 12 and time_delay< 0.1:
        robot_x=random.randint(0,width-enemy_size)
        robot_y=0
        enemy_list.append([robot_x,robot_y])
        
def draw(enemy_list):
    for enemy in enemy_list:
        pygame.draw.rect(screen,blue,(enemy[0],enemy[1],enemy_size,enemy_size))
        
def update_enemies(enemy_list,score):
    for enemy in enemy_list:
        if (enemy[1]>=0 and enemy[1] <=height):
            enemy[1]+=speed
        else:
            enemy_list.pop(enemy_list.index(enemy))
            score+=1
    return score
    
            
def all_collisions(enemy_list):
    for enemy in enemy_list:
        if (enemy[0]>=my_x and enemy[0]<(my_x+my_size)) or (my_x>=enemy[0] and my_x<(enemy[0]+enemy_size)):
            if (enemy[1]>=my_y and enemy[1]<(my_y+my_size)) or (my_y>=enemy[1] and my_y<(enemy[1]+enemy_size)):
                return True        
    return False
        
while (game_over==False):
    
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                my_x-=25
                if my_x<0:
                    my_x=width-55
            if event.key==pygame.K_RIGHT: 
                my_x+=25
                if my_x>width-55:
                    my_x=20
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                my_y-=20
                if my_y<0:
                    my_y=height-55
            if event.key==pygame.K_DOWN:
                my_y+=20
                if my_y>height-55:
                    my_y=55
            
        if event.type==pygame.QUIT:
            pygame.display.quit()
            pygame.mixer.quit()
    bg_image=pygame.image.load("bro.jpg")        
    screen.fill(black)
    screen.blit(bg_image,[0,0])
    
    enemies(enemy_list)
    draw(enemy_list)
        
    score=update_enemies(enemy_list,score)
    speed=levels(score,speed)
    text="score:"+str(score)
    label=font.render(text,1,white)
    screen.blit(label,(width-200,height-60))
    
    if all_collisions(enemy_list)==True:
        print(score)
        pygame.mixer.quit()
        game_over=True
        pygame.display.quit()
        print("GAME_OVER")
        
    
    
    time.tick(30)
    my_pos=(my_x,my_y,my_size,my_size)
    
    pygame.draw.rect(screen,red,my_pos)
    pygame.display.update()
    