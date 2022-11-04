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
screen.blit(alien, alien_rect)

def draw_aliens():

    while True:
        screen.blit(alien, alien_rect)
        alien_rect.y += alien_rect.height
        pygame.display.flip()
        if alien_rect.bottom > screen_rect.bottom:
            alien_rect.topright = screen_rect.topright
            break

while True:
    while True:
        clock = pygame.time.Clock()
        screen.blit(sprout, character_rect)
        pygame.draw.rect(screen, color, bullet)
        draw_aliens()
        #screen.fill((255, 255, 255))
        pygame.display.flip()
        clock.tick(60)
        if pygame.event.get() == True:
            break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                character_rect.y -= 40
                bullet.center = character_rect.center
                if character_rect.top < screen_rect.top:
                    character_rect.top = screen_rect.top

            elif event.key == pygame.K_DOWN:
                character_rect.y += 40
                bullet.center = character_rect.center
                if character_rect.bottom > screen_rect.bottom:
                    character_rect.bottom = screen_rect.bottom

            elif event.key == pygame.K_SPACE:
                while bullet.right < screen_rect.right:
                    bullet.x += 10
                    time.sleep(.02)
                    pygame.draw.rect(screen, color, bullet)
                    screen.blit(sprout, character_rect)
                    draw_aliens()
                    pygame.display.flip()
                    screen.fill((255,255,255))

                if bullet.right >= screen_rect.right:
                    bullet.center = character_rect.center
                    pygame.draw.rect(screen, color, bullet)
                    screen.blit(sprout, character_rect)
                    draw_aliens()
                    pygame.display.flip()
                    screen.fill((255, 255, 255))



pygame.display.flip()
time.sleep(5)



