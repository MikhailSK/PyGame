import numpy as np
from unit import *
from screen import *

arr_wall = [[11, 16], [11, 0], [11, 4], [11, 12], [7, 10],
            [7, 6], [15, 6], [15, 10], [19, 2],
            [19, 14], [3, 14], [3, 2], [11, 8]]
arr_castle = [[0, 8], [22, 8]]

all_sprites = pygame.sprite.Group()
warrior_select_r = WarriorUnitSelectR(all_sprites)
warrior_select_b = WarriorUnitSelectB(all_sprites)
create_unit = CreateUnit(all_sprites)


class Board:
    # создание поля
    def __init__(self, width, height, screen):
        self.screen = screen
        self.color = {0: (0, 0, 0), -1: (0, 150, 50),
                      1: (255, 150, 0), 2: (0, 110, 10),
                      11: (107, 24, 255), 22: (255, 93, 25),
                      12: (0, 150, 50), "frame": (40, 154, 65)}
        self.xod = -1
        self.turn = 1
        self.width_board = width
        self.height_board = height
        self.width = width * BOARD_S + 10
        self.height = height * BOARD_S + 10
        self.board = np.zeros((self.width_board, self.height_board))
        self.board_b = self.board
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.b_x_y = None
        self.is_map_rendered = 0
        self.arr = []
        self.par_click = 0
        self.select = None

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        step = self.cell_size
        x_pos, y_pos = 0, 0
        for x in range(self.left, self.width_board * step, step):
            y_pos = 0
            for y in range(self.top, self.height_board * step, step):
                pygame.draw.rect(self.screen, (150, 190, 16),
                                 (x, y, 30, 30), 1)
                m_par = 0
                if x_pos == 0:
                    if y_pos == 0:
                        if self.board[x_pos + 1][y_pos] \
                                in range(12, 13) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(12, 13):
                            m_par = 11
                        elif self.board[x_pos + 1][y_pos] \
                                in range(22, 23) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(22, 23):
                            m_par = 22
                    elif y_pos == BOARD_H - 1:
                        if self.board[x_pos + 1][y_pos] \
                                in range(12, 13) \
                                or self.board[x_pos][y_pos - 1] \
                                in range(12, 13):
                            m_par = 11
                        elif self.board[x_pos + 1][y_pos] \
                                in range(22, 23) \
                                or self.board[x_pos][y_pos - 1] \
                                in range(22, 23):
                            m_par = 22
                    else:
                        if self.board[x_pos + 1][y_pos] \
                                in range(12, 13) \
                                or self.board[x_pos][y_pos - 1] \
                                in range(12, 13) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(12, 13):
                            m_par = 11
                        elif self.board[x_pos + 1][y_pos] \
                                in range(22, 23) \
                                or self.board[x_pos][y_pos - 1] \
                                in range(22, 23) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(22, 23):
                            m_par = 22
                elif x_pos == BOARD_W - 1:
                    if y_pos == 0:
                        if self.board[x_pos - 1][y_pos] \
                                in range(12, 13) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(12, 13):
                            m_par = 11
                        elif self.board[x_pos - 1][y_pos] \
                                in range(22, 23) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(22, 23):
                            m_par = 22
                    elif y_pos == BOARD_H - 1:
                        if self.board[x_pos - 1][y_pos] \
                                in range(12, 13) \
                                or self.board[x_pos][y_pos - 1] \
                                in range(12, 13):
                            m_par = 11
                        elif self.board[x_pos - 1][y_pos] \
                                in range(22, 23) \
                                or self.board[x_pos][y_pos - 1] \
                                in range(22, 23):
                            m_par = 22
                    else:
                        if self.board[x_pos - 1][y_pos] \
                                in range(12, 13) \
                                or self.board[x_pos][y_pos - 1] \
                                in range(12, 13) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(12, 13):
                            m_par = 11
                        elif self.board[x_pos - 1][y_pos] \
                                in range(22, 23) \
                                or self.board[x_pos][y_pos - 1] \
                                in range(22, 23) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(22, 23):
                            m_par = 22
                else:
                    if y_pos == BOARD_H - 1:
                        if self.board[x_pos - 1][y_pos] \
                                in range(12, 13) \
                                or self.board[x_pos][y_pos - 1] \
                                in range(12, 13) \
                                or self.board[x_pos + 1][y_pos] \
                                in range(12, 13):
                            m_par = 11
                        elif self.board[x_pos - 1][y_pos] \
                                in range(22, 23) \
                                or self.board[x_pos][y_pos - 1] \
                                in range(22, 23) \
                                or self.board[x_pos + 1][y_pos] \
                                in range(22, 23):
                            m_par = 22
                    elif y_pos == 0:
                        if self.board[x_pos - 1][y_pos] \
                                in range(12, 13) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(12, 13) \
                                or self.board[x_pos + 1][y_pos] \
                                in range(12, 13):
                            m_par = 11
                        elif self.board[x_pos - 1][y_pos] \
                                in range(22, 23) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(22, 23) \
                                or self.board[x_pos + 1][y_pos] \
                                in range(22, 23):
                            m_par = 22
                    else:
                        if self.board[x_pos - 1][y_pos] \
                                in range(12, 13) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(12, 13) \
                                or self.board[x_pos + 1][y_pos] \
                                in range(12, 13) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(12, 13):
                            m_par = 11
                        elif self.board[x_pos - 1][y_pos] \
                                in range(22, 23) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(22, 23) \
                                or self.board[x_pos + 1][y_pos] \
                                in range(22, 23) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(22, 23):
                            m_par = 22
                if m_par != 0:
                    pygame.draw.rect(self.screen, self.color[m_par],
                                     (x, y, 30, 30), 1)
                y_pos += 1
            x_pos += 1

        if self.is_map_rendered == 0:
            for i in arr_wall:
                wall = Wall([int(i[0]) * BOARD_S + 10,
                             int(i[1]) * BOARD_S + 10], screen)
                wall.render()
                wall.all_sprites.draw(screen)
                self.board[i[0]][i[1]] = 1
                map_units[(i[0], i[1])] = wall

            castle_blue = CastleBlue([int(arr_castle[0][0]) *
                                      BOARD_S + 10,
                                      int(arr_castle[0][1]) *
                                      BOARD_S + 10], screen)
            castle_blue.render()
            castle_blue.all_sprites.draw(screen)
            self.board[arr_castle[0][0]][arr_castle[0][1]] = 12
            map_units[(arr_castle[0][0], arr_castle[0][1])] \
                = castle_blue

            castle_red = CastleRed([int(arr_castle[1][0]) *
                                    BOARD_S + 10,
                                    int(arr_castle[1][1]) *
                                    BOARD_S + 10], screen)
            castle_red.render()
            castle_red.all_sprites.draw(screen)
            self.board[arr_castle[1][0]][arr_castle[1][1]] = 22
            map_units[(arr_castle[1][0], arr_castle[1][1])] \
                = castle_red

            pygame.draw.rect(screen, self.color["frame"],
                             (5, 10, 5, 510))
            pygame.draw.rect(screen, self.color["frame"],
                             (700, 10, 5, 510))
            pygame.draw.rect(screen, self.color["frame"],
                             (5, 5, 700, 5))
            pygame.draw.rect(screen, self.color["frame"],
                             (5, 520, 700, 5))
            pygame.display.flip()

            all_sprites = pygame.sprite.Group()
            sprite.image = load_image("end_game.png")
            sprite.rect = sprite.image.get_rect()
            all_sprites.add(sprite)
            sprite.rect.x = 733
            sprite.rect.y = 450
            all_sprites.draw(screen)

            self.is_map_rendered = 1

    def get_cell(self, mouse_position):
        x_pos, y_pos = mouse_position
        if self.par_click == 0 or self.par_click == 2:
            if ((x_pos <= 5 or x_pos >= self.width - 5)
                or (y_pos <= 5 or y_pos >= self.height - 5))\
                    and self.select is None:
                    if self.par_click != 2:
                        if sprite.rect.collidepoint((x_pos, y_pos)):
                            print("END TURN")
                            if self.turn == 1:
                                self.turn = 2

                                pygame.draw.rect(screen, (125, 120, 74),
                                                 (724, 525, 200, 70))

                                font = pygame.font.Font(None, 40)
                                text = font.render("RED",
                                                   1, (218, 22, 10))
                                text_x = 795
                                text_y = 550
                                screen.blit(text, (text_x, text_y))

                            elif self.turn == 2:
                                self.turn = 1

                                pygame.draw.rect(screen, (125, 120, 74),
                                                 (790, 525, 70, 70))

                                font = pygame.font.Font(None, 40)
                                text = font.render("BLUE",
                                                   1, (28, 22, 210))
                                text_x = 788
                                text_y = 550
                                screen.blit(text, (text_x, text_y))
                        elif create_unit.rect.collidepoint((x_pos, y_pos)):
                            print("CREATE NEW")
                            self.par_click = 10
                        else:
                            print("miss", x_pos, y_pos, sep="-------")
                        self.b_x_y = None
            elif (self.select is not None and self.par_click == 2) or self.par_click == 0 or self.par_click == 2:
                b_x_pos = (x_pos - 10) // 30
                b_y_pos = (y_pos - 10) // 30
                print(b_x_pos, b_y_pos)
                self.b_x_y = []
                self.b_x_y.append(b_x_pos)
                self.b_x_y.append(b_y_pos)
                self.arr.append([b_x_pos, b_y_pos])
                if self.par_click == 2:
                    coord = (b_x_pos, b_y_pos)
                    coord_px = (b_x_pos * BOARD_S + 10, b_y_pos * BOARD_S + 10)
                    warrior = None
                    if self.select == 11:
                        warrior = WarriorBlue(coord_px, screen)
                        self.board[b_x_pos][b_y_pos] = 12
                    elif self.select == 21:
                        warrior = WarriorRed(coord_px, screen)
                        self.board[b_x_pos][b_y_pos] = 22

                    map_units[coord] = warrior
                    warrior.render()
                    warrior.all_sprites.draw(screen)

                    self.select = None
                    self.par_click = 0
                # self.board[b_x_pos][b_y_pos] = 1
        elif self.par_click == 10:
            if warrior_select_b.rect.collidepoint((x_pos, y_pos)) and self.turn == 1:
                self.par_click = 2
                self.select = 11
                print("WARRIOR BLUE SELECTED")
            elif warrior_select_r.rect.collidepoint((x_pos, y_pos)) and self.turn == 2:
                self.par_click = 2
                self.select = 21
                print("WARRIOR RED SELECTED")

    def on_click(self):
        if self.b_x_y is not None:
            x_pos, y_pos = self.b_x_y[0], self.b_x_y[1]
            if self.board[x_pos][y_pos] != 1:
                pygame.draw.rect(self.screen,
                                 self.color[self.board[x_pos][y_pos]],
                                 (int(x_pos) *
                                  BOARD_S + 10,
                                  int(y_pos) *
                                  BOARD_S + 10, 30, 30), 1)
                try:
                    print(map_units[(x_pos, y_pos)])
                    unit = map_units[(x_pos, y_pos)]
                    unit.get_damage(5)
                    print(unit.health)
                except KeyError:
                    print("Try other")

    def get_click(self, mouse_pos):
        self.get_cell(mouse_pos)
        if self.par_click == 2:
            self.on_click()

