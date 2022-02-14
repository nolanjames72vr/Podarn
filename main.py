import pygame
import os

WIDTH, HEIGHT = 1500, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Podarn")

WHITE = (255, 255, 255)

FPS = 60

PLAYER = pygame.image.load(os.path.join('Assets', 'player.jpg'))
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
MR_HAPPY = pygame.image.load(os.path.join('Assets', 'mrhappy.jpg'))
MR_HAPPY_WIDTH, MR_HAPPY_HEIGHT = 75, 75


def draw_window(playerhitbox, mrhappyhitbox):
    WIN.fill(WHITE)
    WIN.blit(PLAYER, (playerhitbox.x, playerhitbox.y))
    WIN.blit(MR_HAPPY, (mrhappyhitbox.x, mrhappyhitbox.y))
    pygame.display.update()


def player_movement(keys_pressed, playerhitbox):
    if keys_pressed[pygame.K_a]:
        playerhitbox.x -= 5
    if keys_pressed[pygame.K_d]:
        playerhitbox.x += 5
    if keys_pressed[pygame.K_w]:
        playerhitbox.y -= 5
    if keys_pressed[pygame.K_s]:
        playerhitbox.y += 5


def main():
    playerhitbox = pygame.Rect(100, 400, PLAYER_WIDTH, PLAYER_HEIGHT)
    mrhappyhitbox = pygame.Rect(700, 400, MR_HAPPY_WIDTH, MR_HAPPY_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, playerhitbox)
        draw_window(playerhitbox, mrhappyhitbox)

    pygame.quit()


if __name__ == '__main__':
    main()
