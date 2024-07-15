import numpy as np
import pygame

from config import *
from snake import *


class Apple:
    def __init__(self):
        self.apple_pos = np.array(np.random.randint(10, size=2)) * cell_size
        self.apple_rect = pygame.Rect(*self.apple_pos, cell_size, cell_size)

    def update(self):
        while (self.apple_pos == Snake().body).all(1).any():
            self.apple_pos = np.array(np.random.randint(10, size=2)) * cell_size
            print(1)

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            "red",
            self.apple_rect,
        )
