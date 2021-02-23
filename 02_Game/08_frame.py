import pygame
########################################################################################################
# 1. Basic Setting ( Must Coding )
pygame.init()

# Screen Size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Title
pygame.display.set_caption("KONA Game")

# FPS
clock = pygame.time.Clock()
########################################################################################################
# 2. User Default Setting

# Background Image
background = pygame.image.load("D:/Project/PythonWorkSpace/02_Game/Image/BG.JPG")

# Text Font
game_font = pygame.font.Font(None, 40)

# Total Sunning Time(SEC)
total_time = 10

# 시작시간정의
start_ticks = pygame.time.get_ticks()


# User Character
character = pygame.image.load("D:/Project/PythonWorkSpace/02_Game/Image/CH.jpg")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# Enemy Char.
enemy = pygame.image.load("D:/Project/PythonWorkSpace/02_Game/Image/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)

# Move 
to_x = 0
to_y = 0

# Move Speed
speed = 0.6


########################################################################################################
# 3. Event Loop 
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

    # 세로 경계 설정.
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리 - Rect 정보 업데이트.
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 처리 - 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했음")
        running = False

    screen.fill((0, 0, 255))
    # screen.blit(background, (0,0)) # 배경 그리기.

    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # 타이머 집어넣기
    # 경과 시간 계산
    elapsed_time = ( pygame.time.get_ticks() - start_ticks ) / 1000 # 초 단위로 변환(/1000)
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255,255))
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update()

#  Delay
pygame.time.delay(2000) # (ms 라서 1000 곱해줘서 sec 계산)

# 게임 종료처리
pygame.quit()