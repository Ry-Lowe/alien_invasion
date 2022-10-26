import pygame
import sys
while True:
    pygame.init()
    screen = pygame.display.set_mode((200, 200))
    screen.fill((0, 0, 255))
    pygame.display.flip()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(event.key)