import pygame
from sys import exit as EndProgram
from random import randint as RandomInt
from time import sleep as wait

#const
BLOCK_WIDTH_MIN=200
BLOCK_WIDTH_MAX=380
BLOCK_HEIGHT_MIN=30
BLOCK_HEIGHT_MAX=60
BLOCK_SPEED_MIN=3
BLOCK_SPEED_MAX=6
WIN_WIDTH_HEIGHT=800
PLAYER_SIZE=20
PLAYER_SPEED=2
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
AllColours=[WHITE,BLACK,GRAY,LIGHT_BLUE,GREEN,YELLOW,PINK]

#funcs
def RandomHeight():
    return RandomInt(BLOCK_HEIGHT_MIN,BLOCK_HEIGHT_MAX)
def RandomWidth():
    return RandomInt(BLOCK_WIDTH_MIN,BLOCK_WIDTH_MAX)
def RandomSpeed():
    return RandomInt(BLOCK_SPEED_MIN,BLOCK_SPEED_MAX)
def RandomColor():
    return AllColours[RandomInt(0,len(AllColours)-1)]

#go,program,go!
pygame.init()
pygame.display.set_caption('SpaceCube')
background_image = pygame.image.load('background.jpg')

def main():
    FPS=60
    x=(WIN_WIDTH_HEIGHT-PLAYER_SIZE)/2
    y=(WIN_WIDTH_HEIGHT-PLAYER_SIZE)/2
    GameGo=True
    t=0
    angle=0
    
    VragiRect=[]
    VragiAngle=[]
    VragiColour=[]
    VragiSpeed=[]
    VragiNum=0
    
    sc=pygame.display.set_mode((WIN_WIDTH_HEIGHT,WIN_WIDTH_HEIGHT))
    sc.blit(background_image,(0,0))
    cubesc=pygame.Surface((PLAYER_SIZE,PLAYER_SIZE))
    pygame.draw.rect(cubesc,YELLOW,(0,0,PLAYER_SIZE,PLAYER_SIZE))
    pygame.draw.rect(cubesc,(0,255,100),(1,1,PLAYER_SIZE-1,PLAYER_SIZE-1),3)
    sc.blit(cubesc,(x,y))
    
    pygame.display.update()
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                EndProgram()
        
        if GameGo:
            keys=pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                x-=PLAYER_SPEED
            if keys[pygame.K_RIGHT]:
                x+=PLAYER_SPEED
            if keys[pygame.K_UP]:
                y-=PLAYER_SPEED
            if keys[pygame.K_DOWN]:
                y+=PLAYER_SPEED

            if x<10:
                x=10
            elif x>WIN_WIDTH_HEIGHT-PLAYER_SIZE-10:
                x=WIN_WIDTH_HEIGHT-PLAYER_SIZE-10
            if y<10:
                y=10
            elif y>WIN_WIDTH_HEIGHT-PLAYER_SIZE-10:
                y=WIN_WIDTH_HEIGHT-PLAYER_SIZE-10
            
            sc.blit(background_image,(0,0))
            sc.blit(cubesc,(x,y))

            i=0
            while i<VragiNum:
                r=VragiRect[i]
                remove=False
                if VragiAngle[i]==0:
                    r.move_ip(0,VragiSpeed[i])
                    if r[1]>WIN_WIDTH_HEIGHT+10:
                        remove=True
                elif VragiAngle[i]==1:
                    r.move_ip(0,-VragiSpeed[i])
                    if r[1]<-r[3]-10:
                        remove=True
                elif VragiAngle[i]==2:
                    r.move_ip(VragiSpeed[i],0)
                    if r[0]>WIN_WIDTH_HEIGHT+10:
                        remove=True
                elif VragiAngle[i]==3:
                    r.move_ip(-VragiSpeed[i],0)
                    if r[0]<-r[2]-10:
                        remove=True
                if remove:
                    VragiRect.pop(i)
                    VragiColour.pop(i)
                    VragiAngle.pop(i)
                    VragiSpeed.pop(i)
                    VragiNum-=1
                    i-=1
                else:
                    pygame.draw.rect(sc,VragiColour[i],VragiRect[i])
                    if (x>r[0] and x<r[0]+r[2] and y>r[1] and y<r[1]+r[3]) or (x+PLAYER_SIZE>r[0] and x+PLAYER_SIZE<r[0]+r[2] and y>r[1] and y<r[1]+r[3]) or (x+PLAYER_SIZE>r[0] and x+PLAYER_SIZE<r[0]+r[2] and y+PLAYER_SIZE>r[1] and y+PLAYER_SIZE<r[1]+r[3]) or (x>r[0] and x<r[0]+r[2] and y+PLAYER_SIZE>r[1] and y+PLAYER_SIZE<r[1]+r[3]):
                        GameGo=False
                        cubesc.fill((255,0,0))
                        sc.blit(cubesc,(x,y))
                        t=0
                i+=1
            
            if t==30:
                i=RandomWidth()
                n=RandomHeight()
                if angle==0:
                    VragiRect.append(pygame.Rect((RandomInt(10,WIN_WIDTH_HEIGHT-n-10),-i,n,i)))
                    VragiAngle.append(0)
                elif angle==1:
                    VragiRect.append(pygame.Rect((RandomInt(10,WIN_WIDTH_HEIGHT-n-10),WIN_WIDTH_HEIGHT,n,i)))
                    VragiAngle.append(1)
                elif angle==2:
                    VragiRect.append(pygame.Rect((-i,RandomInt(10,WIN_WIDTH_HEIGHT-n-10),i,n)))
                    VragiAngle.append(2)
                elif angle==3:
                    VragiRect.append(pygame.Rect((WIN_WIDTH_HEIGHT,RandomInt(10,WIN_WIDTH_HEIGHT-n-10),i,n)))
                    VragiAngle.append(3)
                VragiSpeed.append(RandomSpeed())
                VragiColour.append(RandomColor())
                VragiNum+=1
                angle+=1
                if angle==4:
                    angle=0
                t=1
            else:
                t+=1

            pygame.display.update()
        else:
            if t==120:
                return
            else:
                t+=1
        clock.tick(FPS)

while True:
    main()
