import pygame
import sys
from time import sleep

BLACK = (0, 0, 0) #R,G,B
padWidth = 480
padHeight = 640

#게임에 등장하는 객체를 드로잉
def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x,y)) #지정한 좌표에 위치하도록 출력


def initGame():
    global gamePad, clock, background, fighter, missile, padHeight
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight)) # 화면크기
    pygame.display.set_caption('Shoothing Game') # 상단에 게임이름 출력
    background = pygame.image.load('C:\PyShooting\images/background.png') # 배경이지미 출력
    fighter = pygame.image.load('C:\PyShooting\images/fighter.png') # 전투기 이미지 출력
    missile = pygame.image.load('C:\PyShooting\images/missile.png')
    clock = pygame.time.Clock()


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

        
        pygame.display.update() #게임화면을 다시그린다.
        

        clock.tick(60)

    pygame.quit()


initGame()
runGame()
