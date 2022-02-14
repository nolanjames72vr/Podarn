import pygame
import os
pygame.font.init()

WIDTH, HEIGHT = 1500, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Podarn")

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

SQUARE_HIT = pygame.USEREVENT + 1
HAPPY_HIT = pygame.USEREVENT + 2

PLAYER = pygame.image.load(os.path.join('Assets', 'player.jpg'))
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
MR_HAPPY = pygame.image.load(os.path.join('Assets', 'mrhappy.jpg'))
MR_HAPPY_WIDTH, MR_HAPPY_HEIGHT = 75, 75


def draw_window(playerhitbox, mrhappyhitbox, player_health):
    WIN.fill(WHITE)
    player_health_text = HEALTH_FONT.render("Health: " + str(player_health), True, BLACK)
    WIN.blit(player_health_text, (WIDTH - player_health_text.get_width() - 10, 10))
    WIN.blit(PLAYER, (playerhitbox.x, playerhitbox.y))
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
            pygame.event.post(pygame.event.Event(SQUARE_HIT))
            print("Square")

    if playerhitbox.colliderect(mrhappyhitbox):
        pygame.event.post(pygame.event.Event(HAPPY_HIT))


def main():
    playerhitbox = pygame.Rect(100, 400, PLAYER_WIDTH, PLAYER_HEIGHT)
    mrhappyhitbox = pygame.Rect(700, 400, MR_HAPPY_WIDTH, MR_HAPPY_HEIGHT)

    player_health = 100
    mr_happy_health = 500

    squares = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    print("HI")
                if event.key == pygame.K_q:
                    print("BYE")

            if event.type == HAPPY_HIT:
                player_health -= 1
                mr_happy_health -= 1

        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, playerhitbox)

        detect_hit(playerhitbox, mrhappyhitbox, squares)

        draw_window(playerhitbox, mrhappyhitbox, player_health)

    pygame.quit()


if __name__ == '__main__':
    main()
