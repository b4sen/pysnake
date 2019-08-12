# TODO: don't spawn the food ON the snake


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
GREEN = (0, 255, 0)

# FONT_SIZE has to be a multiple of 10
FONT_SIZE = 30


class Game:
    def __init__(self):
        self.s = Snake()
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont('DejaVu Sans Mono', FONT_SIZE)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = Clock()

    def clear_screen(self):
        self.screen.fill(BLACK)

    def draw(self):
        surf = self.font.render('Points: {}'.format(self.s.total), True, (255, 255, 255))
        key = pygame.key.get_pressed()
        self.clear_screen()
        self.screen.blit(surf, (0, 0))
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
        self.x = random.randrange(0, WIDTH / 2, CELL_SIZE)
        self.y = random.randrange(FONT_SIZE, HEIGHT, CELL_SIZE)
        self.x_speed = SPEED
        self.y_speed = 0
        self.food = Food()
        self.total = 0
        self.tail = []

    def check_eat(self):
        self.check_dead()
        if self.x == self.food.x and self.y == self.food.y:
            self.total += 1
            self.tail.append([self.x, self.y])
            self.food.x = random.randrange(0, WIDTH, CELL_SIZE)
            self.food.y = random.randrange(0, HEIGHT, CELL_SIZE)

    def check_pos(self):
        if self.x > WIDTH - CELL_SIZE:
            self.x = WIDTH - CELL_SIZE
        if self.x <= 0:
            self.x = 0
        if self.y > HEIGHT - CELL_SIZE:
            self.y = HEIGHT - CELL_SIZE
        if self.y <= 0:
            self.y = 0

    def check_dead(self):
        # TODO: check for walls -> dies too early
        if [self.x, self.y] in self.tail:
            print("You died!")
            sys.exit()

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

        if self.total > 0:
            for i in range(self.total - 1):
                self.tail[i] = self.tail[i + 1]
            self.tail[self.total - 1] = [self.x, self.y]

        self.x += self.x_speed
        self.y += self.y_speed
        self.check_pos()

    def draw(self, screen):
        if len(self.tail) != 0:
            for i in range(len(self.tail)):
                pygame.draw.rect(screen, RED, (self.tail[i][0], self.tail[i][1], CELL_SIZE, CELL_SIZE))
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
