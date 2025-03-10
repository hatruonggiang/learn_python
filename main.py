import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ game
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

# Màu sắc
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Thiết lập tốc độ game
clock = pygame.time.Clock()
SPEED = 10  # FPS

# 2: tạo rắn và thức ăn
snake_pos = [[100, 50], [90, 50], [80, 50]]  # Vị trí của rắn
snake_direction = "RIGHT"  # Hướng đi ban đầu
change_to = snake_direction

food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
food_spawn = True
score = 0

# 3: xử lý di chuyển của rắn
def change_direction(event):
    global change_to
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and snake_direction != "DOWN":
            change_to = "UP"
        elif event.key == pygame.K_DOWN and snake_direction != "UP":
            change_to = "DOWN"
        elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
            change_to = "LEFT"
        elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
            change_to = "RIGHT"

# 4: cập nhật trạng thái rắn
def move_snake():
    global snake_direction
    snake_direction = change_to

    if snake_direction == "UP":
        snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] - 10])
    elif snake_direction == "DOWN":
        snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] + 10])
    elif snake_direction == "LEFT":
        snake_pos.insert(0, [snake_pos[0][0] - 10, snake_pos[0][1]])
    elif snake_direction == "RIGHT":
        snake_pos.insert(0, [snake_pos[0][0] + 10, snake_pos[0][1]])

    # Kiểm tra nếu rắn không ăn thức ăn, loại bỏ phần đuôi
    if snake_pos[0] != food_pos:
        snake_pos.pop()
    else:
        global food_spawn, score
        food_spawn = False
        score += 1

# 5: kiểm tra va chạm
def check_collision():
    if snake_pos[0][0] < 0 or snake_pos[0][0] >= WIDTH or snake_pos[0][1] < 0 or snake_pos[0][1] >= HEIGHT:
        return True

    for block in snake_pos[1:]:
        if snake_pos[0] == block:
            return True

    return False

# 6: vẽ màn hình game
def draw_elements():
    screen.fill(BLACK)

    # Vẽ rắn
    for pos in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    # Vẽ thức ăn
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    pygame.display.flip()

#7: chạy vòng lặp game chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        change_direction(event)

    move_snake()

    if check_collision():
        running = False  # Kết thúc game nếu va chạm

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
        food_spawn = True

    draw_elements()
    clock.tick(SPEED)

pygame.quit()
