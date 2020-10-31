import pygame
import sys
import random
import os
from time import sleep

print("path : ", os.getcwd())

# 시스템폰트확인
# print(pygame.font.get_fonts())

BLACK = (0, 0, 0) #R,G,B
padWidth = 480
padHeight = 640
rockImage = ['C:\PyShooting\images/rock01.png',
             'C:\PyShooting\images/rock02.png',
             'C:\PyShooting\images/rock03.png',
             'C:\PyShooting\images/rock04.png',
             'C:\PyShooting\images/rock05.png',
             'C:\PyShooting\images/rock06.png',
             'C:\PyShooting\images/rock07.png',
             'C:\PyShooting\images/rock08.png',
             'C:\PyShooting\images/rock09.png',
             'C:\PyShooting\images/rock10.png',
             'C:\PyShooting\images/rock11.png',
             'C:\PyShooting\images/rock12.png',
             'C:\PyShooting\images/rock13.png',
             'C:\PyShooting\images/rock14.png',
             'C:\PyShooting\images/rock15.png',
             'C:\PyShooting\images/rock16.png',
             'C:\PyShooting\images/rock17.png',
             'C:\PyShooting\images/rock18.png',
             'C:\PyShooting\images/rock19.png',
             'C:\PyShooting\images/rock20.png',
            ]
    

#게임에 등장하는 객체를 드로잉
def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x,y)) #지정한 좌표에 위치하도록 출력


def initGame():
    global gamePad, clock, background, fighter, missile, padHeight, explosion
    pygame.init()
    pygame.font.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight)) # 화면크기
    pygame.display.set_caption('Shoothing Game') # 상단에 게임이름 출력
    background = pygame.image.load('C:\PyShooting\images/background.png') # 배경이지미 출력
    fighter = pygame.image.load('C:\PyShooting\images/fighter.png') # 전투기 이미지 출력
    missile = pygame.image.load('C:\PyShooting\images/missile.png')
    clock = pygame.time.Clock()

    explosion = pygame.image.load('C:\PyShooting\images/explosion.png')

def writeScore(count):
    global gamePad
    font = pygame.font.SysFont('새굴림',20)
    text = font.render('파괴 : ' + str(count), True, (255,255,255))
    gamePad.blit(text,(10,0))

def writePassed(count):
    global gamePad
    font = pygame.font.SysFont("새굴림",20)
    text = font.render('Pass : ' + str(count), True, (255,0,0))
    gamePad.blit(text,(360,0))

def runGame():
    #전역변수
    global gamePad, clock, background, fighter, missile, padHeight
    
    # 무기좌표리스트
    missileXY = []

    # 전투기 크기
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]
    print("fighterWidth : %d" % fighterWidth)
    print("fighterHeight : %d" % fighterHeight)

    # 전투기 초기 위치 (x,y)
    x = padWidth * 0.45
    y = padHeight * 0.9
    print("초기 위치 x : %d" % x)
    print("초기 위치 y : %d" % y)
    fighterX = 0
    fighterY = 0

    # 운석랜덤생성
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]

    # 운석 초기 위치
    rockX = random.randrange(0, padWidth - rockWidth)
    rockY = 0
    rockSpeed = 2

    isShot = False
    shotCount = 0
    rockPassed = 0

    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()    

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:
                    fighterX -= 5

                elif event.key == pygame.K_RIGHT:
                    fighterX += 5

                elif event.key == pygame.K_UP:
                    fighterY -= 5

                elif event.key == pygame.K_DOWN:
                    fighterY += 5 

                elif event.key == pygame.K_SPACE:
                    missileX = x + fighterWidth/2
                    print("missileX : %d" % missileX)
                    missileY = y - fighterHeight
                    print("missileY : %d" % missileY)
                    missileXY.append([missileX,missileY])

            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    fighterY = 0
        """
        randomNum = list(range(1,6,1))   
        for num in random.choice(randomNum,3):
            # 운석랜덤생성
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            time.sleep(randrange(3,6,1)/10)
        """

        #왼쪽, 오른쪽
        x += fighterX
        if x < 0:
            x = 0
        elif x > padWidth - fighterWidth:
            x = padWidth - fighterWidth

        #위,아래
        y += fighterY
        if y < 0:
            y = 0
        elif y > padHeight - fighterHeight :
            y = padHeight - fighterHeight
        
        #gamePad.fill(BLACK)
        drawObject(background, 0, 0)
        drawObject(fighter, x, y)

        # 미사일 발사 화면에 그리기
        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):
                print("i : %d" % i)
                print("bxy : %d" % bxy[1])
                bxy[1] -= 80
                print("bxy[1] : %d" % bxy[1])
                missileXY[i][1] = bxy[1]

                #미사일이 운석에 맞았을경우
                if bxy[1] < rockY:
                    if bxy[0] > rockX and bxy[0] < rockX + rockWidth:
                        missileXY.remove(bxy)
                        isShot = True
                        shotCount += 1


                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except: 
                        pass
        if len(missileXY) != 0:
            for bx, by in missileXY:
                print("bx : %d" % bx)
                print("by : %d" % by)
                drawObject(missile, bx, by)

        if isShot:
            drawObject(explosion, rockX, rockY)
            rock=pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0 
            isShot = False 

        # shotCount별 운석 속도
        if shotCount > 10:
            rockSpeed = 4
        elif shotCount > 20:
            rockSpeed = 8
        
        writeScore(shotCount)

        rockY += rockSpeed # 운석아래움직임
        #운석이 화면밖으로 떨어진 경우
        if rockY > padHeight:
            rock=pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0
            rockPassed += 1 
        
        writePassed(rockPassed)
        drawObject(rock, rockX, rockY)




        pygame.display.update() #게임화면을 다시그린다.
        

        clock.tick(60)

    pygame.quit()


initGame()
runGame()
