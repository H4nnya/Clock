import pygame
from datetime import datetime


def image(image_name=str()):
    return pygame.image.load(f'sprites/{image_name}')


def sprite(sprit_name, posx, posy):
    return screen.blit(image(sprit_name), (posx, posy))


pygame.init()
screen = pygame.display.set_mode((620, 620))
open_screen = True
pygame.display.set_caption('Clock')

while open_screen:
    hour = f'{datetime.now().hour}'
    minute = f'{datetime.now().minute}'
    second = f'{datetime.now().second}'
    screen.fill(0)
    sprite('background.png', 0, 0)
    
    if len(hour) == 2:
        sprite(f'{hour[0]}.png', 60, 250)
        sprite(f'{hour[1]}.png', 140, 250)
    else:
        sprite('0.png', 60, 250)
        sprite(f'{hour[0]}.png', 140, 250)

    sprite('two_point.png', 205, 260)

    if len(minute) == 2:
        sprite(f'{minute[0]}.png', 260, 250)
        sprite(f'{minute[1]}.png', 340, 250)
    else:
        sprite('0.png', 260, 250)
        sprite(f'{minute[0]}.png', 340, 250)

    if len(second) == 2:
        sprite(f's{second[0]}.png', 445, 252)
        sprite(f's{second[1]}.png', 485, 252)
    else:
        sprite('s0.png', 445, 252)
        sprite(f's{second[0]}.png', 485, 252)

    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open_screen = False
