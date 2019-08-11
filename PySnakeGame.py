import sys
import pygame
import random
from pygame.time import Clock

WIDTH = 640
HEIGHT = 480

CELL_SIZE = 10
SPEED_FACTOR = 1
SPEED = CELL_SIZE * SPEED_FACTOR

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 0, 255)


class Game:
    def __init__(self):
        self.s = Snake()
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = Clock()

    def clear_screen(self):
        self.screen.fill(BLACK)

    def draw(self):
        key = pygame.key.get_pressed()
        self.clear_screen()
        self.s.draw(self.screen)
        self.s.food.draw(self.screen)
        self.s.update(key)
        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.draw()
            self.s.check_eat()
            self.clock.tick(20)


class Snake:
    def __init__(self):
        self.x = random.randrange(0, WIDTH, CELL_SIZE)
        self.y = random.randrange(0, HEIGHT, CELL_SIZE)
        self.x_speed = SPEED
        self.y_speed = 0
        self.food = Food()
        self.total = 1
        self.tail = []

    def check_eat(self):
        # TODO: check if snake eats the food and add 1 to length
        if self.x == self.food.x and self.y == self.food.y:
            self.total += 1
            self.food = Food()

    def check_pos(self):
        if self.x > WIDTH - CELL_SIZE:
            self.x = WIDTH - CELL_SIZE
        if self.x <= 0:
            self.x = 0
        if self.y > HEIGHT - CELL_SIZE:
            self.y = HEIGHT - CELL_SIZE
        if self.y <= 0:
            self.y = 0

    def update(self, key):
        if key[pygame.K_UP]:
            self.x_speed = 0
            self.y_speed = -SPEED
        if key[pygame.K_DOWN]:
            self.x_speed = 0
            self.y_speed = SPEED
        if key[pygame.K_LEFT]:
            self.x_speed = -SPEED
            self.y_speed = 0
        if key[pygame.K_RIGHT]:
            self.x_speed = SPEED
            self.y_speed = 0

        self.x += self.x_speed
        self.y += self.y_speed
        self.check_pos()

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, CELL_SIZE, CELL_SIZE))


class Food:
    def __init__(self):
        self.x = random.randrange(0, WIDTH, CELL_SIZE)
        self.y = random.randrange(0, HEIGHT, CELL_SIZE)

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, CELL_SIZE, CELL_SIZE))


if __name__ == '__main__':
    game = Game()
    game.run()
