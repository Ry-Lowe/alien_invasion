import sys
import pygame
import time
pygame.init()
screen = pygame.display.set_mode((1050, 600))
screen.fill((255, 255, 255))

sprout = pygame.image.load("C:/Users/m253768/Desktop/EW200/Labs/Lab7/alien_invasion/images/rocket.bmp")
alien = pygame.image.load("C:/Users/m253768/Desktop/EW200/Labs/Lab7/alien_invasion/images/alien.bmp")
character_rect = sprout.get_rect()
alien_rect = alien.get_rect()
screen_rect = screen.get_rect()
character_rect.midleft = screen_rect.midleft
bullet = pygame.Rect(0,0,10,5)
color = (0,0,0)
bullet.center = character_rect.center
alien_rect.topright = screen_rect.topright
#screen.blit(alien, alien_rect)
def draw_aliens():
    while True:
        screen.blit(alien, alien_rect)
        alien_rect.y += alien_rect.height
        pygame.display.flip()
        if alien_rect.bottom > screen_rect.bottom:
            break
draw_aliens()
pygame.display.flip()
time.sleep(5)