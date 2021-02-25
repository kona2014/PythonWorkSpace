import pygame
import os
########################################################################################################
# 1. Basic Setting ( Must Coding )
pygame.init()

# Screen Size
screen_width = 640 
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Title
pygame.display.set_caption("KONA Game")

# Current Folder Path
path = os.path.dirname(os.path.realpath(__file__))

# FPS
clock = pygame.time.Clock()
########################################################################################################
# 2. User Default Setting

# Background Image
background = pygame.image.load(path + "/Image/BG.JPG")

# Text Font
game_font = pygame.font.Font(None, 40)

# Total Running Time(SEC)
total_time = 100

# 시작시간정의
start_ticks = pygame.time.get_ticks()

# User Character
character = pygame.image.load(path + "/Image/CH.jpg")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# Weapon
weapon = pygame.image.load(path + "/Image/WEAPON.png")
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]
weapon_x_pos = (screen_width / 2) - (weapon_width / 2)
weapon_y_pos = (screen_height / 2) - (weapon_height / 2)
weapon_speed = 5

weapons = []

# Ball
# 공의 가변적 요소는 1. 스피드, 2. 사이즈(이미지), 3. 방향(x_pos), 4. 튕김(y_pos)
ball_speeds_y = [-18, -15, -12, -9]
ball_images = [
    pygame.image.load(path + "/Image/ball_01.png"),
    pygame.image.load(path + "/Image/ball_02.png"),
    pygame.image.load(path + "/Image/ball_03.png"),
    pygame.image.load(path + "/Image/ball_04.png")
]

balls = []

# 최초 생성 정보 
balls.append({
    "pos_x" : 50,
    "pos_y" : 50,
    "image_index" : 0,
    "to_x" : 3,
    "to_y" : -6,
    "init_speed_y" : ball_speeds_y[0]
})

# Move 
to_x = 0

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
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + character_width / 2 - weapon_width / 2
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:  # 키보드를 뗐다
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 움직임 적용
    character_x_pos += to_x * dt
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]
    # for w in weapons: # 천정에 닿으면 사라지는 무기
    #     if w[1] < 0:
    #         weapons.remove(w) # 리스트 내에 리스트가 일치하면 제거.
    # 이렇게도 구현할 수 있다. 
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

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

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_image_index = ball_val["image_index"]

        ball_rect = ball_images[ball_image_index].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

    #   공과 캐릭터 충돌
        if ball_rect.colliderect(character_rect):
            running = False
            break

        # 공과 무기 충돌
        # for weapon_val in enumerate(weapons):
        #     weapon_x_pos = weapon_val[0]
        #     weapon_y_pos = weapon_val[1]

        #     weapon_rect = 





    # 그리기 

    screen.fill((0, 0, 255))
    # screen.blit(background, (0,0)) # 배경 그리기.

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(character, (character_x_pos, character_y_pos))

    # 공 그리기
    for ball_index, ball_value in enumerate(balls):
        ball_pos_x = ball_value["pos_x"]
        ball_pos_y = ball_value["pos_y"]
        ball_image_index = ball_value["image_index"]

        ball_size = ball_images[ball_image_index].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 벽 충돌처리.
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_value["to_x"] = ball_value["to_x"] * -1

        # 바닥충돌
        if ball_pos_y >= screen_height - ball_height:
            ball_value["to_y"] = ball_value["init_speed_y"]
        else: # 그 외에는 중력 적용
            ball_value["to_y"] += 0.5

        ball_value["pos_x"] += ball_value["to_x"]
        ball_value["pos_y"] += ball_value["to_y"]

        screen.blit(ball_images[ball_image_index], (ball_pos_x, ball_pos_y))

    # 타이머 집어넣기
    # 경과 시간 계산
    elapsed_time = ( pygame.time.get_ticks() - start_ticks ) / 1000 # 초 단위로 변환(/1000)
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update()

#  Delay
# pygame.time.delay(2000) # (ms 라서 1000 곱해줘서 sec 계산)

# 게임 종료처리
pygame.quit()