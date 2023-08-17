import pygame
from pygame.locals import *


def display_image(image_path):
    pygame.init()
    screen_width = 1200
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    image = pygame.image.load(image_path)
    resized_image = pygame.transform.scale(image, (screen_width, screen_height))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.blit(resized_image, (0, 0))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


image_path = "gallery/sprites/ins.jpg"
display_image(image_path)
