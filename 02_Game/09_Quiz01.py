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

# 게임결과
game_result = "Game Over"

# Move 
to_x = 0
to_y = -6

# Move Speed
speed = 0.4
 

# User Character
character = pygame.image.load(path + "/Image/character.png")
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
ball_speeds_y = [-18, -16, -14, -12]
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
    "to_y" : to_y,
    "init_speed_y" : ball_speeds_y[0]
})

weapon_del_idx = -1
ball_del_idx = -1




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
            game_result = "Game Over"
            running = False
            break

        # 공과 무기 충돌
        for weapon_index, weapon_val in enumerate(weapons):
            game_result = "Time Over"

            weapon_x_pos = weapon_val[0]
            weapon_y_pos = weapon_val[1]

            weapon_rect = weapon.get_rect() # 무기 이미지는 하나뿐(weapon)
            weapon_rect.left = weapon_x_pos
            weapon_rect.top = weapon_y_pos

            if weapon_rect.colliderect(ball_rect):
                # 해당 공과 무기를 동시에 삭제한다.
                weapon_del_idx = weapon_index
                ball_del_idx = ball_idx

                # 제일 작은공이 아니면 공을 쪼개준다. 
                if ball_image_index < 3:
                    ball_width = ball_rect.size[0]   
                    ball_height = ball_rect.size[1] 

                    ball_s_size = ball_images[ball_image_index + 1].get_rect().size
                    ball_s_width = ball_s_size[0]
                    ball_s_height = ball_s_size[1]

                    balls.append({
                        "pos_x" : ball_pos_x + ball_width / 2 - ball_s_width / 2,
                        "pos_y" : ball_pos_y - ball_height / 2 + ball_s_height / 2,
                        "image_index" : ball_image_index + 1,
                        "to_x" : 3,
                        "to_y" : to_y,
                        "init_speed_y" : ball_speeds_y[ball_image_index + 1]
                    })    

                    balls.append({
                        "pos_x" : ball_pos_x + ball_width / 2 - ball_s_width / 2,
                        "pos_y" : ball_pos_y - ball_height / 2 + ball_s_height / 2,
                        "image_index" : ball_image_index + 1,
                        "to_x" : -3,
                        "to_y" : to_y,
                        "init_speed_y" : ball_speeds_y[ball_image_index + 1]
                    })    

                break # weapon for 빠져나감

        if weapon_del_idx > -1: # 리스트의 인덱스는 0부터 시작하므로 -1보다 큰 어떤 인덱스 여부 체크.
            del weapons[weapon_del_idx]
            weapon_del_idx = -1 # 지우고 나면 다시 초기화
            break # Ball for 빠져나감

    if ball_del_idx > -1: # 인덱스가 -1 이면 공이 충돌 안했다는 뜻 
        del balls[ball_del_idx]
        ball_del_idx = -1

        if len(balls) == 0:
            game_result = "Mission Complete"
            running = False

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
        game_result = "Time Over"
        running = False

    pygame.display.update()

msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()


#  Delay
pygame.time.delay(2000) # (ms 라서 1000 곱해줘서 sec 계산)

# 게임 종료처리
pygame.quit()