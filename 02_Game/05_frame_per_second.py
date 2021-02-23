import pygame
# from typing_extensions import runtime

pygame.init() # 초기화 반드시 필요

# 화면크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("KONA Game") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경이미지 불러오기
background = pygame.image.load("D:/Project/PythonWorkSpace/02_Game/Image/BG.JPG")

# 캐릭터 불러오기
character = pygame.image.load("D:/Project/PythonWorkSpace/02_Game/Image/CH.jpg")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

# 이동속도

speed = 0.6


# Event Loop 
running = True #게임 진행중 여부 확인. 

while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:  # 키보드를 눌렀다
            if event.key == pygame.K_LEFT:
                to_x -= speed
            elif event.key == pygame.K_RIGHT:
                to_x += speed
            elif event.key == pygame.K_UP:
                to_y -= speed
            elif event.key == pygame.K_DOWN:
                to_y += speed

        if event.type == pygame.KEYUP:  # 키보드를 뗐다
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계 설정.
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 가로 경계 설정.
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.fill((0, 0, 255))
    # screen.blit(background, (0,0)) # 배경 그리기.

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

# 게임 종료처리
pygame.quit()