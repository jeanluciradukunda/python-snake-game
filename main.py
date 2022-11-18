import pygame
from pygame.locals import *


if __name__ == '__main__':
    """intialize pygame"""
    pygame.init()

    surface = pygame.display.set_mode((500, 500))
    # fill background with color
    surface.fill((110, 110, 5))
    # flip the display
    # pygame.display.flip()

    # load an image
    image = pygame.image.load('ball.png')

    # event loop
    while True:
        for event in pygame.event.get():
            # if event is key down
            if event.type == KEYDOWN:
                pass
                # if key is escape
                # if event.key == K_ESCAPE:
                #     # quit the game
                #     pygame.quit()
                #     exit(0)
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
    time.sleep(5)

# class Game:
#     def __init__(self):
#         pygame.init()
#         self.screen = pygame.display.set_mode((800, 600))
#         self.clock = pygame.time.Clock()
#         self.running =