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

# 캐릭터 불러오기
character = pygame.image.load("D:/Project/PythonWorkSpace/02_Game/Image/CH.jpg")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height


# Event Loop 
running = True #게임 진행중 여부 확인. 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if event.type == pygame.KEYDOWN:
            # if event.key 

    screen.fill((0, 0, 255))
    # screen.blit(background, (0,0)) # 배경 그리기.

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

# 게임 종료처리
pygame.quit()