
import pygame
import time
pygame.init()
screen = pygame.display.set_mode((1000, 600))
screen.fill((255, 255, 255))
class Draw_character():
    def __init__(self):
        x=0

    def draw(self):
        sprout = pygame.image.load('sprout.bmp')
        character_rect = sprout.get_rect()
        screen_rect = screen.get_rect()
        character_rect.center = screen_rect.center
        screen.blit(sprout, character_rect)
        pygame.display.flip()

Sprout = Draw_character()
Sprout.draw()
time.sleep(8)