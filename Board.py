import pygame
import random
import numpy as np
from unit import *

BOARD_W = 23
BOARD_H = 17
BOARD_S = 30
arr_wall = [[11, 16], [11, 0], [11, 4], [11, 12], [7, 10],
            [7, 6], [15, 6], [15, 10], [19, 2],
            [19, 14], [3, 14], [3, 2], [11, 8]]
arr_castle = [[0, 8], [22, 8]]


class Board:
    # создание поля
    def __init__(self, width, height, screen):
        self.screen = screen
        self.color = {0: (0, 0, 0), -1: (0, 150, 50),
                      1: (255, 150, 0)}
        self.xod = -1
        self.width_board = width
        self.height_board = height
        self.width = width * BOARD_S + 10
        self.height = height * BOARD_S + 10
        # self.board = [[1] * width for _ in range(height)]
        self.board = np.zeros((self.width_board, self.height_board))
        self.board_b = self.board
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.b_x_y = None
        self.is_map_rendered = 0
        self.arr = []

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        step = self.cell_size
        for x in range(self.left, self.width_board * step, step):
            for y in range(self.top, self.height_board * step, step):
                pygame.draw.rect(self.screen, (150, 190, 16),
                                 (x, y, 30, 30), 1)

        if self.is_map_rendered == 0:
            for i in arr_wall:
                wall = Wall([int(i[0]) * BOARD_S + 10,
                             int(i[1]) * BOARD_S + 10], screen)
                wall.render()
                wall.all_sprites.draw(screen)

            castle_blue = CastleBlue([int(arr_castle[0][0]) *
                                      BOARD_S + 10,
                                      int(arr_castle[0][1]) *
                                      BOARD_S + 10], screen)
            castle_blue.render()
            castle_blue.all_sprites.draw(screen)

            castle_red = CastleRed([int(arr_castle[1][0]) *
                                    BOARD_S + 10,
                                    int(arr_castle[1][1]) *
                                    BOARD_S + 10], screen)
            castle_red.render()
            castle_red.all_sprites.draw(screen)

            pygame.display.flip()

            self.is_map_rendered = 1

    def get_cell(self, mouse_position):
        x_pos, y_pos = mouse_position
        if (x_pos <= 5 or x_pos >= self.width - 5) or\
                (y_pos <= 5 or y_pos >= self.height - 5):
            print("miss", x_pos, y_pos, sep="-------")
            self.b_x_y = None
        else:
            b_x_pos = (x_pos - 10) // 30
            b_y_pos = (y_pos - 10) // 30
            print(b_x_pos, b_y_pos)
            self.b_x_y = []
            self.b_x_y.append(b_x_pos)
            self.b_x_y.append(b_y_pos)
            self.arr.append([b_x_pos, b_y_pos])
            print(self.arr)
            self.board[b_x_pos][b_y_pos] = 1

    def on_click(self):
        if self.b_x_y is not None:
            x_pos, y_pos = self.b_x_y[0], self.b_x_y[1]
            pygame.draw.rect(self.screen,
                             self.color[self.board[x_pos][y_pos]],
                             (int(x_pos) *
                              BOARD_S + 10,
                              int(y_pos) *
                              BOARD_S + 10, 30, 30), 1)

    def get_click(self, mouse_pos):
        self.get_cell(mouse_pos)
        self.on_click()
