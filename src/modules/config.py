''' This file contains all the global variables that are used in the project. '''

import pygame, os
from assets.recourse_path import recourse_path

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Initialize modules and window size
pygame.init()
DISPLAY_SIZE = pygame.display.Info().current_w, pygame.display.Info().current_h
WINDOW_WIDTH = int(DISPLAY_SIZE[0])  # the width and the height of the window
WINDOW_HEIGHT = int(DISPLAY_SIZE[1])
MAX_FPS = 60
DELAY_TIME = 100
clock = pygame.time.Clock()

# Setting up window
pygame.display.set_caption("Conway's Game of Life")
try:
    pygame.display.set_icon(pygame.image.load(recourse_path(os.path.join("assets", "images", "icon.png"))))
except FileNotFoundError:
    pass
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

grid_size = 200
zoom_factor = 2.0
block_size = WINDOW_HEIGHT / grid_size * zoom_factor
viewport_x = (grid_size * block_size - WINDOW_WIDTH) / 2
viewport_y = (grid_size * block_size - WINDOW_HEIGHT) / 2
selected_pattern = None
