import pygame
import random
import numpy as np
from Board import Board, BOARD_H, BOARD_W, BOARD_S


size = width, height = BOARD_W * BOARD_S + 20,\
                       BOARD_H * BOARD_S + 20
screen = pygame.display.set_mode(size)
board = Board(BOARD_W, BOARD_H, screen)
screen.fill((0, 0, 0))

running = True
par_space = 0
FPS = 20
par = -1
clock = pygame.time.Clock()


while running:
    if par == -1:
        board.render()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            board.get_click(event.pos)
            par *= -1

    pygame.display.flip()
    clock.tick(FPS)
