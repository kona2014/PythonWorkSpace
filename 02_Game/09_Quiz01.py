import pygame
########################################################################################################
# 1. Basic Setting ( Must Coding )
pygame.init()

# Screen Size
screen_width = 640 
screen_height = 480
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

# Total Running Time(SEC)
total_time = 100

# 시작시간정의
start_ticks = pygame.time.get_ticks()

# User Character
character = pygame.image.load("D:/Project/PythonWorkSpace/02_Game/Image/CH.jpg")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# Weapon
weapon = pygame.image.load("D:/Project/PythonWorkSpace/02_Game/Image/WEAPON.png")
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
    pygame.image.load("D:/Project/PythonWorkSpace/02_Game/Image/ball_01.png"),
    pygame.image.load("D:/Project/PythonWorkSpace/02_Game/Image/ball_02.png"),
    pygame.image.load("D:/Project/PythonWorkSpace/02_Game/Image/ball_03.png"),
    pygame.image.load("D:/Project/PythonWorkSpace/02_Game/Image/ball_04.png")
]

balls = []

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

    # 충돌 처리 - 체크

    screen.fill((0, 0, 255))
    # screen.blit(background, (0,0)) # 배경 그리기.


    # 그리기 
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(character, (character_x_pos, character_y_pos))

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
# pygame.time.delay(2000) # (ms 라서 1000 곱해줘서 sec 계산)

# 게임 종료처리
pygame.quit()