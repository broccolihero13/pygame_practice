import pygame

pygame.init()

width = 900
height = 700
screenDim = (width,height)

screen = pygame.display.set_mode(screenDim)
finished = False

while not finished:
    for event in pygame.event.get():
        
    pygame.display.flip()