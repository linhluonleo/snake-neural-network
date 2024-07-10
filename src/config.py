import math

import numpy as np

map_size = 10
tile_size = 64
screen_height = map_size * tile_size
screen_width = screen_height * 2

fov = math.pi * 2
half_fov = math.pi
casted_rays = 8
angle = fov / casted_rays


direction = {
    0: np.array([0, -1]),
    1: np.array([1, 0]),
    2: np.array([0, 1]),
    3: np.array([-1, 0]),
}

n_input = 16
n_hidden = 10
n_output = 4
