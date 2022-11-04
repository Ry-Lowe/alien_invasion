import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1000, 600))
screen.fill((0, 0, 0))
star = pygame.image.load('ballBlue.png')
star_rect = star.get_rect()
screen_rect = screen.get_rect()

while True:
    screen.fill((0, 0, 0))
    screen.blit(star, star_rect)
    while True:
        screen.blit(star, star_rect)
        star_rect.x += (2 * star_rect.width)
        if star_rect.right > screen_rect.right:
            break
    star_rect.left = screen_rect.left
    star_rect.y += (2 * star_rect.height)
    if star_rect.bottom > screen_rect.bottom:
        screen.fill((0,0,0))
        star_rect.topleft = screen_rect.topleft
        continue
    time.sleep(.2)
    pygame.display.flip()
#pygame.display.flip()
#time.sleep(10)