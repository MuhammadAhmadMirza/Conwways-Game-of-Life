''' Implement the game rules for the Game of Life and update the cells for the next generation '''

import numpy as np
import pygame
import scipy.signal
from modules.colors import *
from modules.config import *

def update_neighbors(window, cells, size, viewport_x, viewport_y, width_progress=False):
    ''' Update the cells for the next generation and draw them on the screen '''
    updated_cells = np.copy(cells)  # Copy to preserve original values

    # Create another array of neighbors sum using convolution
    neighbors_sum = scipy.signal.convolve2d(cells, np.ones((3, 3)), mode='same', boundary='wrap') - cells
    
    for row in range(cells.shape[0]):
        for col in range(cells.shape[1]):
            screen_x = col * size - viewport_x
            screen_y = row * size - viewport_y

            if 0 <= screen_x < WINDOW_WIDTH and 0 <= screen_y < WINDOW_HEIGHT:
                alive = neighbors_sum[row, col]
                color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT
                if cells[row, col] == 1:
                    if alive < 2 or alive > 3:  # Too few or too many neighbors
                        if width_progress:
                            color = COLOR_DIE_NEXT
                        updated_cells[row, col] = 0
                    else:  # 2 or 3 neighbors, sufficient to be alive
                        updated_cells[row, col] = 1
                        if width_progress:
                            color = COLOR_ALIVE_NEXT
                else:
                    if alive == 3:  # Exactly 3 neighbors, cell is born
                        updated_cells[row, col] = 1
                        if width_progress:
                            color = COLOR_ALIVE_NEXT

                pygame.draw.rect(window, color, (screen_x, screen_y, size, size))

    return updated_cells
