import pygame
import time

from pygame.locals import *

"""
    This is the main file for the game. It will be the file that is run to start the game.
    It will be responsible for creating the window, and running the game loop.
    Resources:
    https://youtu.be/8dfePlONtls?list=PLyuuFBQATZK785lLIN_z0EvQPzjfksTZ2
"""


class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = 100
        self.y = 100
        self.direction = "down"

    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.update()

    # move left
    def move_left(self):
        self.direction = "left"

    # move right
    def move_right(self):
        self.direction = "right"

    # move up
    def move_up(self):
        self.direction = "up"

    # move down
    def move_down(self):
        self.direction = "down"

    def walk(self) -> None:
        """Moves the player in the direction the player is currently facing."""
        if self.direction == "left":
            self.x -= 10
        if self.direction == "right":
            self.x += 10
        if self.direction == "up":
            self.y -= 10
        if self.direction == "down":
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

    def run(self) -> None:
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
            self.snake.walk()
            time.sleep(0.2)


if __name__ == "__main__":

    game = Game()
    game.run()  # run game
