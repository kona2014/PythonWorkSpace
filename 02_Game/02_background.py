import pygame
# from typing_extensions import runtime

pygame.init() # 초기화 반드시 필요

# 화면크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("KONA Game") # 게임 이름

# 배경이미지 불러오기
background = pygame.image.load("D:/Project/PythonWorkSpace/02_Game/Image/BG.JPG")

# Event Loop 
running = True #게임 진행중 여부 확인. 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 255))
    # screen.blit(background, (0,0)) # 배경 그리기.

    pygame.display.update()

# 게임 종료처리
pygame.quit()