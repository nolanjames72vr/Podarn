import pygame
import os
import random
pygame.font.init()

WIDTH, HEIGHT = 1500, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Podarn")

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
PROGRESS_FONT = pygame.font.SysFont('comicsans', 20)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)

BROWN = (139, 69, 19)
GREY = (128, 128, 128)
ORANGE = (255, 140, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
BLUE = (0, 0, 255)

FPS = 60

SQUARE_HIT_BROWN = pygame.USEREVENT + 1
SQUARE_HIT_GREY = pygame.USEREVENT + 2
SQUARE_HIT_ORANGE = pygame.USEREVENT + 3
SQUARE_HIT_YELLOW = pygame.USEREVENT + 4
SQUARE_HIT_PURPLE = pygame.USEREVENT + 5
SQUARE_HIT_BLUE = pygame.USEREVENT + 6
SQUARE_HIT_BLACK = pygame.USEREVENT + 7
HAPPY_HIT = pygame.USEREVENT + 9

PLAYER = pygame.image.load(os.path.join('Assets', 'player.jpg'))
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
MR_HAPPY = pygame.image.load(os.path.join('Assets', 'mrhappy.jpg'))
MR_HAPPY_WIDTH, MR_HAPPY_HEIGHT = 75, 75


class Square:
    def __init__(self, rect, color, code):
        self.rect = rect
        self.color = color
        self.code = code

    def update_position(self):
        self.rect.x = random.randrange(140, WIDTH-280)
        self.rect.y = random.randrange(70, HEIGHT-20)


def draw_window(playerhitbox, mrhappyhitbox, squares, player_health, brown_count, grey_count, orange_count,
                yellow_count, purple_count, blue_count, black_count):
    WIN.fill(WHITE)
    progress_text = HEALTH_FONT.render("Progress: Not Much", True, BLACK)
    WIN.blit(progress_text, (10, 10))
    brown_text = PROGRESS_FONT.render("Brown: " + str(brown_count), True, BLACK)
    WIN.blit(brown_text, (30, progress_text.get_height() + 10))
    grey_text = PROGRESS_FONT.render("Grey: " + str(grey_count), True, BLACK)
    WIN.blit(grey_text, (30, progress_text.get_height() + 10 + brown_text.get_height()))
    orange_text = PROGRESS_FONT.render("Orange: " + str(orange_count), True, BLACK)
    WIN.blit(orange_text, (30, progress_text.get_height() + 10 + brown_text.get_height() * 2))
    yellow_text = PROGRESS_FONT.render("Yellow: " + str(yellow_count), True, BLACK)
    WIN.blit(yellow_text, (30, progress_text.get_height() + 10 + brown_text.get_height() * 3))
    purple_text = PROGRESS_FONT.render("Purple: " + str(purple_count), True, BLACK)
    WIN.blit(purple_text, (30, progress_text.get_height() + 10 + brown_text.get_height() * 4))
    blue_text = PROGRESS_FONT.render("Blue: " + str(blue_count), True, BLACK)
    WIN.blit(blue_text, (30, progress_text.get_height() + 10 + brown_text.get_height() * 5))
    black_text = PROGRESS_FONT.render("Black: " + str(black_count), True, BLACK)
    WIN.blit(black_text, (30, progress_text.get_height() + 10 + brown_text.get_height() * 6))
    player_health_text = HEALTH_FONT.render("Health: " + str(player_health), True, BLACK)
    WIN.blit(player_health_text, (WIDTH - player_health_text.get_width() - 10, 10))
    WIN.blit(PLAYER, (playerhitbox.x, playerhitbox.y))
    for square in squares:
        pygame.draw.rect(WIN, square.color, square.rect)
    WIN.blit(MR_HAPPY, (mrhappyhitbox.x, mrhappyhitbox.y))
    pygame.display.update()


def player_movement(keys_pressed, playerhitbox):
    if keys_pressed[pygame.K_a] and playerhitbox.x > 0:
        playerhitbox.x -= 5
    if keys_pressed[pygame.K_d] and playerhitbox.x < WIDTH - PLAYER_WIDTH:
        playerhitbox.x += 5
    if keys_pressed[pygame.K_w] and playerhitbox.y > 0:
        playerhitbox.y -= 5
    if keys_pressed[pygame.K_s] and playerhitbox.y < HEIGHT - PLAYER_WIDTH:
        playerhitbox.y += 5


def detect_hit(playerhitbox, mrhappyhitbox, squares):
    for square in squares:
        if playerhitbox.colliderect(square):
            pygame.event.post(pygame.event.Event(pygame.USEREVENT + square.code))
            square.update_position()
    if playerhitbox.colliderect(mrhappyhitbox):
        pygame.event.post(pygame.event.Event(HAPPY_HIT))


def generate_squares():
    squares = []
    for i in range(7):
        if i == 0:
            color = BROWN
        elif i == 1:
            color = GREY
        elif i == 2:
            color = ORANGE
        elif i == 3:
            color = YELLOW
        elif i == 4:
            color = PURPLE
        elif i == 5:
            color = BLUE
        elif i == 6:
            color = BLACK
        else:
            color = RED
        square = Square(pygame.Rect(random.randrange(140, WIDTH-280),
                                    random.randrange(70, HEIGHT-20), 20, 20), color, i+1)
        squares.append(square)
    return squares


def main():
    playerhitbox = pygame.Rect(100, 400, PLAYER_WIDTH, PLAYER_HEIGHT)
    mrhappyhitbox = pygame.Rect(700, 400, MR_HAPPY_WIDTH, MR_HAPPY_HEIGHT)

    player_health = 100
    mr_happy_health = 500

    brown_count = 0
    grey_count = 0
    orange_count = 0
    yellow_count = 0
    purple_count = 0
    blue_count = 0
    black_count = 0

    squares = generate_squares()

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    brown_count = 0
                    grey_count = 0
                    orange_count = 0
                    yellow_count = 0
                    purple_count = 0
                    blue_count = 0
                    black_count = 0
                    print(pygame.mouse.get_pos())
                if event.key == pygame.K_q:
                    print("BYE")

            if event.type == HAPPY_HIT:
                player_health -= 1
                mr_happy_health -= 1

            if event.type == SQUARE_HIT_BROWN:
                brown_count += 1
            if event.type == SQUARE_HIT_GREY:
                grey_count += 1
            if event.type == SQUARE_HIT_ORANGE:
                orange_count += 1
            if event.type == SQUARE_HIT_YELLOW:
                yellow_count += 1
            if event.type == SQUARE_HIT_PURPLE:
                purple_count += 1
            if event.type == SQUARE_HIT_BLUE:
                blue_count += 1
            if event.type == SQUARE_HIT_BLACK:
                black_count += 1

        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, playerhitbox)

        detect_hit(playerhitbox, mrhappyhitbox, squares)

        draw_window(playerhitbox, mrhappyhitbox, squares, player_health, brown_count, grey_count, orange_count,
                    yellow_count, purple_count, blue_count, black_count)

    pygame.quit()


if __name__ == '__main__':
    main()
