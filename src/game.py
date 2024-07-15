import sys

import pygame

from apple import *
from config import *
from snake import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Snake Game")

        self.snake = Snake()
        self.apple = Apple()

        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.direction = direction[0]
                if event.key == pygame.K_DOWN:
                    self.snake.direction = direction[2]
                if event.key == pygame.K_LEFT:
                    self.snake.direction = direction[3]
                if event.key == pygame.K_RIGHT:
                    self.snake.direction = direction[1]

    def update(self):
        self.snake.update()
        self.apple.update()
        if np.all(self.snake.head == self.apple.apple_pos):
            print(12)

    def draw(self, screen):
        self.screen.fill("white")
        self.snake.draw(screen)
        self.apple.draw(screen)
        pygame.display.update()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw(self.screen)
            self.clock.tick(10)
