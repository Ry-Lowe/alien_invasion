import sys
import pygame
import time
from pygame.sprite import Sprite

pygame.init()
screen = pygame.display.set_mode((1000, 600))
screen.fill((255, 255, 255))

sprout = pygame.image.load("C:/Users/m253768/Desktop/EW200/Labs/Lab7/alien_invasion/images/rocket.bmp")
alien = pygame.image.load("C:/Users/m253768/Desktop/EW200/Labs/Lab7/alien_invasion/images/alien.bmp")
character_rect = sprout.get_rect()
screen_rect = screen.get_rect()
character_rect.midleft = screen_rect.midleft
bullet = pygame.Rect(0,0,10,5)
color = (0,0,0)
bullet.midleft = character_rect.midright
alien_rect = alien.get_rect()
alien_rect.topright = screen_rect.topright
clear_alien = pygame.Rect(alien_rect.left, 0, screen_rect.width-alien_rect.left, screen_rect.height)
clear = pygame.Rect(character_rect.right, 0, screen_rect.width-character_rect.width, screen_rect.height)
collisions = pygame.Rect.colliderect(bullet, alien_rect)
x=0




while x<10:
    time.sleep(1)
    clock = pygame.time.Clock()
    for y in range(0, screen_rect.height):
        screen.blit(alien, alien_rect)
        alien_rect.y += 1.5 * alien_rect.height
        pygame.display.flip()
    clear_alien = pygame.Rect(alien_rect.right, 0, screen_rect.width - alien_rect.right, screen_rect.height)
    screen.fill((255,255,255), rect=clear_alien)
    alien_rect.top = screen_rect.top
    alien_rect.x -= 1.5 * alien_rect.width
    screen.fill((255, 255, 255), rect=character_rect)
    screen.fill((255, 255, 255), rect=bullet)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                character_rect.y -= 40
                bullet.midleft = character_rect.midright
                if character_rect.top < screen_rect.top:
                    character_rect.top = screen_rect.top

            elif event.key == pygame.K_DOWN:
                character_rect.y += 40
                bullet.midleft = character_rect.midright
                if character_rect.bottom > screen_rect.bottom:
                    character_rect.bottom = screen_rect.bottom

            elif event.key == pygame.K_SPACE:
                while bullet.right < screen_rect.right:
                    clear_bullet = pygame.Rect(bullet.left, bullet.top-20, 50, 100)
                    screen.fill((255,255,255), rect= clear_bullet)
                    screen.blit(sprout, character_rect)
                    bullet.x += 10
                    pygame.draw.rect(screen, color, bullet)
                    pygame.display.flip()
                    time.sleep(.02)

                if bullet.right >= screen_rect.right:
                    screen.fill((255, 255, 255), rect=bullet)
                    bullet.midleft = character_rect.midright

    screen.blit(sprout, character_rect)
    pygame.draw.rect(screen, color, bullet)
    if alien_rect.left < character_rect.right:
        alien_rect.topright = screen_rect.topright
        screen.fill((255,255,255), rect=clear)
    if collisions == True:
        screen.fill((255, 255, 255), rect=alien_rect)
        screen.fill((255, 255, 255), rect=bullet)
        x +=1

    clock.tick(60)
    pygame.display.flip()

