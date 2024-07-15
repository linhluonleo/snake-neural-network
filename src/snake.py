import numpy as np
import pygame

from config import *


class Snake:
    def __init__(self):
        self.body = np.array(
            [[1 * cell_size, 0 * cell_size], [0 * cell_size, 0 * cell_size]]
        )
        self.head = self.body[0]
        self.direction = direction[np.random.randint(4)]

    def update(self):
        body_copy = self.body[:-1]
        body_copy = np.insert(
            body_copy, 0, body_copy[0] + (self.direction * cell_size), axis=0
        )
        self.body = body_copy.copy()

    def draw(self, screen):
        for block in self.body:
            block_rect = pygame.Rect(block[0], block[1], cell_size, cell_size)
            pygame.draw.rect(screen, "grey", block_rect)
