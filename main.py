import pygame
import os

WIDTH, HEIGHT = 1500, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Podarn")

WHITE = (255, 255, 255)

FPS = 60

PLAYER = pygame.image.load(os.path.join('Assets', 'player.jpg'))
MR_HAPPY = pygame.image.load(os.path.join('Assets', 'mrhappy.jpg'))


def draw_window():
    WIN.fill(WHITE)
    WIN.blit(PLAYER, (100, 100))
    WIN.blit(MR_HAPPY, (300, 300))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == '__main__':
    main()
