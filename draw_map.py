import pygame
from time import sleep

SIDE_LENGTH = 10
root3 = 3**0.5
pygame.init()
window = pygame.display.set_mode((400,200), pygame.RESIZABLE)

def draw_hex(center):
    x,y = center
    corners = [
        (x + SIDE_LENGTH,   y),
        (x + SIDE_LENGTH/2, y + root3/2*SIDE_LENGTH),
        (x - SIDE_LENGTH/2, y + root3/2*SIDE_LENGTH),
        (x - SIDE_LENGTH,   y),
        (x - SIDE_LENGTH/2, y - root3/2*SIDE_LENGTH),
        (x + SIDE_LENGTH/2, y - root3/2*SIDE_LENGTH)
    ]
    num_corners = len(corners)+1
    pygame.draw.polygon(window, (255,255,255), corners, 1)

def hex_to_pixel(point):
    x,y = point
    return (x*3/2*SIDE_LENGTH, y*root3/2*SIDE_LENGTH)

def is_valid_cell(point):
    x,y = point
    return (x+y) % 2 == 0

draw_hex(hex_to_pixel((3,3)))
pygame.display.flip()
sleep(3)
pygame.quit()
