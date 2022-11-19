import pygame
from pygame.locals import *


# class snake with block object
class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = 100
        self.y = 100

    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.update()

    # move left
    def move_left(self):
        self.x -= 10
        self.draw()

    # move right
    def move_right(self):
        self.x += 10
        self.draw()

    # move up
    def move_up(self):
        self.y -= 10
        self.draw()

    # move down
    def move_down(self):
        self.y += 10
        self.draw()


# class game
class Game:
    # init
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))
        self.surface.fill((110, 110, 5))
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.snake.move_up()
                    elif event.key == K_DOWN:
                        self.snake.move_down()
                    elif event.key == K_LEFT:
                        self.snake.move_left()
                    elif event.key == K_RIGHT:
                        self.snake.move_right()
                    self.snake.draw()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


if __name__ == "__main__":

    game = Game()
    game.run()  # run game
