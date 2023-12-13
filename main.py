import sys

import pygame
from pygame.locals import *

import functions as f
from menu import Menu

pygame.init()
screen = pygame.display.set_mode((1000, 800))

font = pygame.font.Font('yoster.ttf', 40)
TEXT_COL = (255, 255, 255)

game_menu = False


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


run = True
while run:
    screen.fill((0, 0, 0))

    if game_menu:
        pass

    draw_text('Press SPACE button', font, TEXT_COL, 300, 400)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_menu = True
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
