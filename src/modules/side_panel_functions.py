''' This module contains functions to draw the rules and controls on the screen '''

import pygame
from modules.colors import *
from modules.config import *
from assets.recourse_path import recourse_path as rp

def blit_text(window, text, pos, font, color, control_keys=None):
    ''' 
    Helper function to handle text wrapping. 
    It splits the text into lines that fit within the window width and adjusts line spacing.
    '''
    words = text.split(' ')
    space_width = font.size(' ')[0]
    max_width = WINDOW_WIDTH - WINDOW_HEIGHT - 20  # Available width in the sidebar
    x, y = pos
    line = ''
    line_spacing = font.get_linesize() + 5  # Adjust line spacing as needed
    
    for word in words:
        # Check if the word is a control key that needs to be highlighted
        word_color = COLOR_ALIVE_NEXT if control_keys and word in control_keys else color
        test_line = f"{line}{word} "
        text_width, _ = font.size(test_line)
        
        if text_width <= max_width:
            line = test_line
        else:
            window.blit(font.render(line, True, color), (x, y))
            y += line_spacing
            line = f"{word} "
    
    if line:  # Blit any remaining text
        window.blit(font.render(line, True, color), (x, y))
        y += line_spacing
        
    return y  # Return the updated y position for the next line of text

def draw_rules(window):
    ''' Draw the rules on the screen '''
    font = pygame.font.Font(rp(os.path.join(ROOT_DIR, 'assets', 'fonts', 'opensans.ttf')), 30)
    
    # Heading
    heading = font.render("Conway's Game of Life", True, COLOR_ALIVE_NEXT)
    text_rect = heading.get_rect(center=(WINDOW_HEIGHT + (WINDOW_WIDTH - WINDOW_HEIGHT) // 2, 30))
    window.blit(heading, text_rect)
    
    font = pygame.font.Font(rp(os.path.join(ROOT_DIR, 'assets', 'fonts', 'opensans.ttf')), 20)
    
    # Rules Text
    rules_text = [
        ("Introduction:", COLOR_ALIVE_NEXT),
        ("A cellular automaton devised by mathematician John Conway. "
         "Simulates the evolution of a grid of cells based on simple rules.", COLOR_REGULAR_TEXT),
        ("Logic/Rules:", COLOR_ALIVE_NEXT),
        ("1. A dead cell with exactly three live neighbors becomes a live cell.", COLOR_REGULAR_TEXT),
        ("2. A live cell with two or three live neighbors remains alive.", COLOR_REGULAR_TEXT),
        ("3. A live cell with fewer than two or more than three live neighbors dies.", COLOR_REGULAR_TEXT)
    ]
    
    y_offset = 70
    for line, color in rules_text:
        if line == "Logic/Rules:":
            y_offset += 20  # Adjust spacing before the rules
        y_offset = blit_text(window, line, (WINDOW_HEIGHT + 20, y_offset), font, color)
        y_offset += 10  # Adjust spacing between different lines of text

    return y_offset + 20  # Return y_offset for subsequent content

def draw_controls(window, start_y, grid_size, delay_time):
    ''' Draw the controls on the screen '''
    font = pygame.font.Font(rp(os.path.join(ROOT_DIR, 'assets', 'fonts', 'opensans.ttf')), 26)
    
    # Heading
    heading = font.render("Controls:", True, COLOR_ALIVE_NEXT)
    text_rect = heading.get_rect(center=(WINDOW_HEIGHT + (WINDOW_WIDTH - WINDOW_HEIGHT) // 2, start_y))
    window.blit(heading, text_rect)
    
    font = pygame.font.Font(rp(os.path.join(ROOT_DIR, 'assets', 'fonts', 'opensans.ttf')), 20)
    
    # Controls Text
    controls_text = [
        ("SPACE:  start/stop", ["Space"]),
        ("BACKSPACE:  clear grid", ["Backspace"]),
        ("R/L CLICK:  draw/erase", ["Right/left click"]),
        (f"UP/DOWN:  grid size = {grid_size}", ["Up", "Down"]),
        (f"RIGHT/LEFT:  speed = {(1000 - delay_time) / 100}", ["Right", "Left"]),
        ("SCROLL:  zoom", ["Scroll"])
    ]
    
    # Column positions
    column_x1 = WINDOW_HEIGHT + 20
    column_x2 = WINDOW_HEIGHT + (WINDOW_WIDTH - WINDOW_HEIGHT) // 2 + 20
    column_width = column_x2 - column_x1

    y_offset = start_y + 30
    midpoint = (len(controls_text) + 1) // 2  # Ensure even split or slight bias if odd number

    # Draw first column
    for i in range(midpoint):
        line, keys = controls_text[i]
        y_offset = blit_text(window, line, (column_x1, y_offset), font, COLOR_REGULAR_TEXT, control_keys=keys)
        y_offset += 10  # Adjust spacing between different lines of text

    # Draw second column
    y_offset = start_y + 30  # Reset y_offset for the second column
    for i in range(midpoint, len(controls_text)):
        line, keys = controls_text[i]
        y_offset = blit_text(window, line, (column_x2, y_offset), font, COLOR_REGULAR_TEXT, control_keys=keys)
        y_offset += 10  # Adjust spacing between different lines of text
        
    return y_offset  # Return y_offset for subsequent content

def draw_preset_patterns(window, start_y):
    ''' Draw the preset pattern options on the screen in two columns '''
    font = pygame.font.Font(rp(os.path.join(ROOT_DIR, 'assets', 'fonts', 'opensans.ttf')), 26)
    heading = font.render("Cool Patterns:", True, COLOR_ALIVE_NEXT)
    heading_rect = heading.get_rect(center=(WINDOW_HEIGHT + (WINDOW_WIDTH - WINDOW_HEIGHT) // 2, start_y + 30))
    window.blit(heading, heading_rect)
    
    font = pygame.font.Font(rp(os.path.join(ROOT_DIR, 'assets', 'fonts', 'opensans.ttf')), 20)
    patterns_text = [
        "1: Replicator",
        "2: Pentadecathlon",
        "3: Pulsar",
        "4: Gosper Glider Gun",
        "5: Hammerhead Spaceship",
        "6: Spacefiller"
    ]
    
    # Calculate positions for two columns
    column_x1 = WINDOW_HEIGHT + 20
    column_x2 = WINDOW_HEIGHT + (WINDOW_WIDTH - WINDOW_HEIGHT) // 2 + 20
    column_width = column_x2 - column_x1
    midpoint = len(patterns_text) // 2

    y_offset = start_y + 60
    
    # Draw first column
    for i in range(midpoint):
        text = patterns_text[i]
        y_offset = blit_text(window, text, (column_x1, y_offset), font, COLOR_REGULAR_TEXT)
        y_offset += 10  # Adjust spacing between different lines of text
    
    # Reset y_offset for the second column
    y_offset = start_y + 60
    
    # Draw second column
    for i in range(midpoint, len(patterns_text)):
        text = patterns_text[i]
        y_offset = blit_text(window, text, (column_x2, y_offset), font, COLOR_REGULAR_TEXT)
        y_offset += 10  # Adjust spacing between different lines of text

    return y_offset

def display_stats(window, y_start, generation, alive_cells):
    ''' Display the current generation and alive cells count '''
    font = pygame.font.Font(rp(os.path.join(ROOT_DIR, 'assets', 'fonts', 'opensans.ttf')), 18)
    text = f"Generation: {generation}  |  Alive Cells: {alive_cells}"
    text_surface = font.render(text, True, COLOR_ALIVE_NEXT)
    text_rect = text_surface.get_rect(center=(WINDOW_HEIGHT + (WINDOW_WIDTH - WINDOW_HEIGHT) // 2, y_start + 60))
    window.blit(text_surface, text_rect)
    
    warning = font.render("Reduce grid size for better performance", True, (200, 0, 0))
    warning_rect = warning.get_rect(center=(WINDOW_HEIGHT + (WINDOW_WIDTH - WINDOW_HEIGHT) // 2, y_start + 90))
    window.blit(warning, warning_rect)

def draw_sidebar(window, grid_size, delay_time, generation_count, alive_cells):
    ''' Draw the sidebar on the screen to show controls and rules '''
    pygame.draw.rect(window, COLOR_GRID, (WINDOW_HEIGHT, 0, WINDOW_WIDTH - WINDOW_HEIGHT, WINDOW_HEIGHT))
    y_offset = draw_rules(window)
    y_offset = draw_controls(window, y_offset, grid_size, delay_time)
    y_offset = draw_preset_patterns(window, y_offset)
    display_stats(window, y_offset, generation_count, alive_cells)
    pygame.display.flip()
