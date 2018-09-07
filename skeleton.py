import pygame,sys

pygame.init()

width = 1000
height = 700
screenDim = (width,height)

screen = pygame.display.set_mode(screenDim)
pygame.display.set_caption("Game Name Here")
finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            # pygame.quit()
        
    pygame.display.flip()

pygame.quit()