import pygame, time, random
from pygame.locals import *
from pygame.mixer import pause

pygame.init()
myfont = pygame.font.SysFont('timesnewromanbold', 30)
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pong')
pygame.mouse.set_visible(1)
screen.fill((100,10,100))
done=False
pygame

if "vars"=="vars":
  colorlist=[40,40,40]
  scorea=0
  scoreb=0
  playeray=20
  playerby=20
  mvma=2
  mvmb=2
  momenta=0
  momentb=0
  ballpart=0
  clock = pygame.time.Clock()
  ballx=320
  bally=240
  ballmmx=3
  balltotm=1.0
  numbounce=0
  countdown=120
  mvm=True
  hcd=0
  hitx=0
  hity=0
  verthitx=0
  verthity=0
  vertpart=0
  ballmmy=3*float(random.randrange(-100,100,5))/100

def drawscreen():
  screen.fill((200,100,20))
  if ballpart!=0:pygame.draw.circle(screen, (200,100,20+ballpart), (hitx, hity),40-0.1*ballpart,15)
  if vertpart!=0:pygame.draw.circle(screen, (200,100,20+vertpart), (verthitx, verthity),40-0.1*vertpart,15)
  pygame.draw.rect(screen, (0,0,0), pygame.Rect(50, playeray, 20, 80))
  pygame.draw.rect(screen, (0,0,0), pygame.Rect(570, playerby, 20, 80))
  pygame.draw.circle(screen, (0,0,0), (ballx, bally),20,20)
  screen.blit(textsurface,(300,0))
  pygame.display.flip()

while not done:
  dt=clock.tick(60)/20
  for event in pygame.event.get():
    if event.type == pygame.QUIT:  
      done = True  
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: x,y = pygame.mouse.get_pos()
  pressed = pygame.key.get_pressed()
  if mvm:
    if pressed[pygame.K_w]:momenta-=mvma*dt
    if pressed[pygame.K_s]:momenta+=mvma*dt
    if pressed[pygame.K_UP]:momentb-=mvmb*dt
    if pressed[pygame.K_DOWN]:momentb+=mvmb*dt
    if colorlist[0]>149: colchange=-1
    elif colorlist[0]<51: colchange=1
    if playeray<0: playeray=0
    if playeray>400:playeray=400
    if playerby<0:playerby=0
    if playerby>400:playerby=400
  colorlist[0]+=colchange
  textsurface = myfont.render((str(scorea)+"|"+str(scoreb)), False, (0, 0, 0))
  drawscreen()
  print(str(colorlist)+" A:"+str(round(momenta))+" B:"+str(round(momentb)))
  print(round(ballpart))
  playeray+=momenta
  playerby+=momentb
  ballpart/=1.17647058824**dt
  vertpart/=1.17647058824**dt
  momenta*=0.80
  momentb*=0.80
  if countdown==0:
    ballx+=ballmmx
    bally+=ballmmy
    if ballmmx<14 and ballmmx>-14:
      ballmmx*=1.0005
  else: countdown-=1
  if ballx>552 and ballx<594 and bally<playerby+100 and bally>playerby-20 and hcd==0:
    ballmmx*=-1
    ballmmy*=0.8
    ballmmy+=momentb*0.5
    hcd=30
    hitx,hity,ballpart=ballx,bally,200
  if ballx<88 and ballx>46 and bally<playeray+100 and bally>playeray-20 and hcd==0:
    ballmmx*=-1
    ballmmy*=0.8
    ballmmy+=momenta*0.5
    hcd=30
    hitx,hity,ballpart=ballx,bally,200
  if bally>460:
    ballmmy*=-1
    bally=460
    vertpart,verthity,verthitx=200,bally,ballx
  if bally<20:
    vertpart,verthity,verthitx,bally,ballmmy=200,bally,ballx,20,ballmmy*-1
  print(ballmmx)
  print(ballmmy)
  if ballx>640 or ballx<0:
    if ballx>640:
      scorea+=1
      serve=1
    else:
      scoreb+=1
      serve=-1
    ballx,bally,ballmmx,ballmmy,countdown=320,240,3*serve,3*float(random.randrange(-100,100,5))/100,120
    if scorea>10 or scoreb>10:
      if scorea>10:winner="A"
      if scoreb>10:winner="B"
      firedown=random.randrange(1,100,1)
      loffire=[]
      textsurface = myfont.render("Player "+(str(winner)+" WINS!!!"), False, (0, 0, 0))
      while not done:
        screen.fill((200,100,20))
        if firedown==0:
          loffire.append([random.randrange(120,520,1),random.randrange(90,390,1),200])
          firedown=random.randrange(1,100,1)
        else:firedown-=1
        for work in loffire:
          pygame.draw.circle(screen, (200,100,20+work[2]), (work[0], work[1]),40-0.1*work[2],15)
          loffire[loffire.index(work)][2]-=1
          if work[2]==0:
            loffire.remove(work)
        screen.blit(textsurface,(230,240))
        pygame.display.flip()
        for event in pygame.event.get():
          if event.type == pygame.QUIT:  
            done = True  
  if hcd>0:hcd-=1




  
