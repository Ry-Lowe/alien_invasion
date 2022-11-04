import pygame
import time
from random import randint



pygame.init()
screen = pygame.display.set_mode((1000, 600))
screen.fill((0, 0, 0))
star = pygame.image.load('particleStar.png')
star_rect = star.get_rect()
screen_rect = screen.get_rect()
screen.blit(star, star_rect)

while True:
    while True:
        randnumx = randint(star_rect.width, 200)
        screen.blit(star, star_rect)
        star_rect.x += randnumx
        if star_rect.right > screen_rect.right:
            break
    randnumy = randint(star_rect.height, 200)
    star_rect.left = screen_rect.left
    star_rect.y += randnumy
    if star_rect.bottom > screen_rect.bottom:
        break
    screen.blit(star, star_rect)
pygame.display.flip()
time.sleep(10)