''' This module contains functions to initialize the display and update it '''

import numpy as np
import pygame
from modules.colors import *
from modules.game_rules_implementation import update_neighbors
from modules.config import *
from modules.side_panel_functions import draw_sidebar
from modules.preset_patterns import *

def draw_grid(screen, size, grid_size, viewport_x, viewport_y):
    ''' Draw the grid lines on the screen '''
    start_x = int(viewport_x // size)
    start_y = int(viewport_y // size)
    
    for x in range(start_x, grid_size):
        screen_x = x * size - viewport_x
        if screen_x > WINDOW_HEIGHT:
            break
        pygame.draw.line(screen, COLOR_GRID, (screen_x, 0), (screen_x, WINDOW_HEIGHT))
    
    for y in range(start_y, grid_size):
        screen_y = y * size - viewport_y
        if screen_y > WINDOW_HEIGHT:
            break
        pygame.draw.line(screen, COLOR_GRID, (0, screen_y), (WINDOW_HEIGHT, screen_y))

def get_start_screen(size, pattern_number):
    ''' Get an initial pattern for the game screen from presets '''
    patterns = {
        '1': replicator,
        '2': pentadecathlon,
        '3': pulsar,
        '4': gosper_glider_gun,
        '5': hammerhead_spaceship,
        '6': spacefiller
    }
    
    if pattern_number in patterns:
        pattern = patterns[pattern_number]
        # Create a blank grid and place the pattern in the center
        grid = np.zeros((size, size), dtype=int)
        offset_x = (size - pattern.shape[1]) // 2
        offset_y = (size - pattern.shape[0]) // 2
        grid[offset_y:offset_y+pattern.shape[0], offset_x:offset_x+pattern.shape[1]] = pattern
        return grid
    else:
        # Default blank grid
        return np.zeros((size, size), dtype=int)

def update_display(window, cells, size, viewport_x, viewport_y, grid_size, delay_time, generation_count, alive_cells):
    ''' Update the display by calling all required functions '''
    window.fill(COLOR_BG)
    update_neighbors(window, cells, size, viewport_x, viewport_y)
    draw_grid(window, size, grid_size, viewport_x, viewport_y)
    draw_sidebar(window, grid_size, delay_time, generation_count, alive_cells)
    pygame.display.flip()