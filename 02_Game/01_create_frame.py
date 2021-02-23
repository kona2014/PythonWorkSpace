import pygame
# from typing_extensions import runtime

pygame.init() # 초기화 반드시 필요

# 화면크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("KONA Game") #게임 이름

# Event Loop 
running = True #게임 진행중 여부 확인. 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# 게임 종료처리
pygame.quit()