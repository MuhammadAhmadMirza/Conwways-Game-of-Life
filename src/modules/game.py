''' Main game loop and event handling '''

import pygame
import numpy as np
from modules.colors import *
from modules.initialize_display import *
from modules.game_rules_implementation import update_neighbors
from modules.side_panel_functions import draw_sidebar
from modules.config import *

def main():
    global grid_size, block_size, window, DELAY_TIME, zoom_factor, viewport_x, viewport_y
    
    def in_grid(pos):
        return 0 <= pos[0] < WINDOW_HEIGHT and 0 <= pos[1] < WINDOW_HEIGHT
    
    def resize_grid(grid, new_dimension):
        resized_grid = np.zeros((new_dimension, new_dimension), dtype=int)
        min_dim = min(grid.shape[0], new_dimension)
        resized_grid[:min_dim, :min_dim] = grid[:min_dim, :min_dim]
        return resized_grid

    def adjust_viewport():
        global viewport_x, viewport_y
        max_viewport_x = max(0, grid_size * block_size - WINDOW_WIDTH)
        max_viewport_y = max(0, grid_size * block_size - WINDOW_HEIGHT)
        viewport_x = min(max(0, viewport_x), max_viewport_x)
        viewport_y = min(max(0, viewport_y), max_viewport_y)
        return viewport_x, viewport_y

    def place_pattern_in_center(cells, pattern):
        ''' Place the selected pattern in the center of the current grid '''
        pattern_height, pattern_width = pattern.shape
        start_x = (grid_size - pattern_width) // 2
        start_y = (grid_size - pattern_height) // 2
        cells[start_y:start_y + pattern_height, start_x:start_x + pattern_width] = pattern
        return cells

    cells = get_start_screen(grid_size, '0')
    alive_cells = np.sum(cells)
    generation_count = 0
    update_display(window, cells, block_size, viewport_x, viewport_y, grid_size, DELAY_TIME, generation_count, alive_cells)
    pygame.display.flip()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    
                elif event.key == pygame.K_BACKSPACE:
                    cells = get_start_screen(grid_size, '0')
                    generation_count = 0
                
                elif event.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6):
                    # Load the corresponding pattern and place it in the center of the grid
                    pattern_number = chr(event.key)
                    pattern = get_start_screen(grid_size, pattern_number)
                    cells = place_pattern_in_center(cells, pattern)
                    generation_count = 0

                elif event.key == pygame.K_UP and grid_size + 10 <= 400:
                    grid_size += 10
                    block_size = WINDOW_HEIGHT / grid_size * zoom_factor
                    cells = resize_grid(cells, grid_size)
                    viewport_x, viewport_y = adjust_viewport()

                elif event.key == pygame.K_DOWN and grid_size - 10 >= 50:
                    grid_size -= 10
                    block_size = WINDOW_HEIGHT / grid_size * zoom_factor
                    cells = resize_grid(cells, grid_size)
                    viewport_x, viewport_y = adjust_viewport()
                    
                elif event.key == pygame.K_RIGHT:
                    DELAY_TIME = max(0, DELAY_TIME - 50)
                    
                elif event.key == pygame.K_LEFT:
                    DELAY_TIME = min(DELAY_TIME + 50, 1000)
                
                update_display(window, cells, block_size, viewport_x, viewport_y, grid_size, DELAY_TIME, generation_count, alive_cells)
            
            elif event.type == pygame.MOUSEWHEEL:
                zoom_center_x, zoom_center_y = pygame.mouse.get_pos()
                old_size = block_size
                zoom_scale = 1.2 if event.y > 0 else 0.8
                zoom_factor *= zoom_scale
                block_size = WINDOW_HEIGHT / grid_size * zoom_factor

                max_zoom_out = WINDOW_HEIGHT / grid_size
                if block_size < max_zoom_out:
                    block_size = max_zoom_out
                    zoom_factor = block_size / (WINDOW_HEIGHT / grid_size)

                viewport_x += (zoom_center_x + viewport_x) * (block_size / old_size - 1)
                viewport_y += (zoom_center_y + viewport_y) * (block_size / old_size - 1)

                viewport_x, viewport_y = adjust_viewport()

                update_display(window, cells, block_size, viewport_x, viewport_y, grid_size, DELAY_TIME, generation_count, alive_cells)

        if in_grid(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row = min(max(int((pos[1] + viewport_y) / block_size), 0), grid_size - 1)
                col = min(max(int((pos[0] + viewport_x) / block_size), 0), grid_size - 1)
                cells[row, col] = 1
            
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row = min(max(int((pos[1] + viewport_y) / block_size), 0), grid_size - 1)
                col = min(max(int((pos[0] + viewport_x) / block_size), 0), grid_size - 1)
                cells[row, col] = 0
            
            update_display(window, cells, block_size, viewport_x, viewport_y, grid_size, DELAY_TIME, generation_count, alive_cells)

        if running:
            cells = update_neighbors(window, cells, block_size, viewport_x, viewport_y, width_progress=True)
            draw_grid(window, block_size, grid_size, viewport_x, viewport_y)
            draw_sidebar(window, grid_size, DELAY_TIME, generation_count, alive_cells)
            pygame.display.flip()
            generation_count += 1
            
        if running:
            pygame.time.delay(DELAY_TIME)
        
        alive_cells = np.sum(cells)
        clock.tick(MAX_FPS)
