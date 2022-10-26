import sys
import pygame
import time
pygame.init()
screen = pygame.display.set_mode((1000, 600))
screen.fill((255, 255, 255))
class Draw_character():
    def __init__(self):
        x=0

    def draw(self):
        sprout = pygame.image.load("C:/Users/m253768/Desktop/EW200/Labs/Lab7/alien_invasion/images/rocket.bmp")
        character_rect = sprout.get_rect()
        screen_rect = screen.get_rect()
        character_rect.center = screen_rect.center


        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        character_rect.x += 40
                        if character_rect.right > screen_rect.right:
                            character_rect.right = screen_rect.right
                    elif event.key == pygame.K_LEFT:
                        character_rect.x -= 40
                        if character_rect.left < screen_rect.left:
                            character_rect.left = screen_rect.left
                    elif event.key == pygame.K_UP:
                        character_rect.y -= 40
                        if character_rect.top < screen_rect.top:
                            character_rect.top = screen_rect.top
                    elif event.key == pygame.K_DOWN:
                        character_rect.y += 40
                        if character_rect.bottom > screen_rect.bottom:
                            character_rect.bottom = screen_rect.bottom
                screen.fill((255, 255, 255))
                screen.blit(sprout, character_rect)
                pygame.display.flip()

Sprout = Draw_character()
Sprout.draw()

