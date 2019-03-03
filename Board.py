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
archer_select_r = ArcherUnitSelectR(all_sprites)
archer_select_b = ArcherUnitSelectB(all_sprites)
priest_select_r = PriestUnitSelectR(all_sprites)
priest_select_b = PriestUnitSelectB(all_sprites)
create_unit = CreateUnit(all_sprites)
move_unit = MoveUnit(all_sprites)
damage_unit = DamageUnit(all_sprites)


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
        self.res_r = 2
        self.res_r_add = 1
        self.res_b = 2
        self.res_b_add = 1
        self.select = None
        self.select_unit = None
        self.select_coord = None

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
                                in range(12, 16) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(12, 16):
                            m_par = 11
                        elif self.board[x_pos + 1][y_pos] \
                                in range(22, 26) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(22, 26):
                            m_par = 22
                    elif y_pos == BOARD_H - 1:
                        if self.board[x_pos + 1][y_pos] \
                                in range(12, 16) \
                                or self.board[x_pos][y_pos - 1] \
                                in range(12, 16):
                            m_par = 11
                        elif self.board[x_pos + 1][y_pos] \
                                in range(22, 26) \
                                or self.board[x_pos][y_pos - 1] \
                                in range(22, 26):
                            m_par = 22
                    else:
                        if self.board[x_pos + 1][y_pos] \
                                in range(12, 16) \
                                or self.board[x_pos][y_pos - 1] \
                                in range(12, 16) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(12, 16):
                            m_par = 11
                        elif self.board[x_pos + 1][y_pos] \
                                in range(22, 26) \
                                or self.board[x_pos][y_pos - 1] \
                                in range(22, 26) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(22, 26):
                            m_par = 22
                elif x_pos == BOARD_W - 1:
                    if y_pos == 0:
                        if self.board[x_pos - 1][y_pos] \
                                in range(12, 16) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(12, 16):
                            m_par = 11
                        elif self.board[x_pos - 1][y_pos] \
                                in range(22, 26) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(22, 26):
                            m_par = 22
                    elif y_pos == BOARD_H - 1:
                        if self.board[x_pos - 1][y_pos] \
                                in range(12, 16) \
                                or self.board[x_pos][y_pos - 1] \
                                in range(12, 16):
                            m_par = 11
                        elif self.board[x_pos - 1][y_pos] \
                                in range(22, 26) \
                                or self.board[x_pos][y_pos - 1] \
                                in range(22, 26):
                            m_par = 22
                    else:
                        if self.board[x_pos - 1][y_pos] \
                                in range(12, 16) \
                                or self.board[x_pos][y_pos - 1] \
                                in range(12, 16) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(12, 16):
                            m_par = 11
                        elif self.board[x_pos - 1][y_pos] \
                                in range(22, 26) \
                                or self.board[x_pos][y_pos - 1] \
                                in range(22, 26) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(22, 26):
                            m_par = 22
                else:
                    if y_pos == BOARD_H - 1:
                        if self.board[x_pos - 1][y_pos] \
                                in range(12, 16) \
                                or self.board[x_pos][y_pos - 1] \
                                in range(12, 16) \
                                or self.board[x_pos + 1][y_pos] \
                                in range(12, 16):
                            m_par = 11
                        elif self.board[x_pos - 1][y_pos] \
                                in range(22, 26) \
                                or self.board[x_pos][y_pos - 1] \
                                in range(22, 26) \
                                or self.board[x_pos + 1][y_pos] \
                                in range(22, 26):
                            m_par = 22
                    elif y_pos == 0:
                        if self.board[x_pos - 1][y_pos] \
                                in range(12, 16) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(12, 16) \
                                or self.board[x_pos + 1][y_pos] \
                                in range(12, 16):
                            m_par = 11
                        elif self.board[x_pos - 1][y_pos] \
                                in range(22, 26) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(22, 26) \
                                or self.board[x_pos + 1][y_pos] \
                                in range(22, 26):
                            m_par = 22
                    else:
                        if self.board[x_pos - 1][y_pos] \
                                in range(12, 16) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(12, 16) \
                                or self.board[x_pos + 1][y_pos] \
                                in range(12, 16) \
                                or self.board[x_pos][y_pos - 1] \
                                in range(12, 16):
                            m_par = 11
                        elif self.board[x_pos - 1][y_pos] \
                                in range(22, 26) \
                                or self.board[x_pos][y_pos + 1] \
                                in range(22, 26) \
                                or self.board[x_pos + 1][y_pos] \
                                in range(22, 26) \
                                or self.board[x_pos][y_pos - 1] \
                                in range(22, 26):
                            m_par = 22
                if m_par != 0 and self.board[x_pos][y_pos] != 1:
                    pygame.draw.rect(self.screen, self.color[m_par],
                                     (x, y, 30, 30), 1)
                    if self.board[x_pos][y_pos] not in range(12, 16)\
                            and self.board[x_pos][y_pos]\
                            not in range(22, 26):
                        if m_par == 11:
                            self.board[x_pos][y_pos] = -11
                        elif m_par == 22:
                            self.board[x_pos][y_pos] = -21
                y_pos += 1
            x_pos += 1

        pygame.draw.rect(screen, (238, 160, 74),
                         (724, 452, 200, 60))

        font = pygame.font.Font(None, 28)

        if self.turn == 1:
            text = font.render("RES-B: " + str(self.res_b) + "(+" + str(self.res_b_add) + ")",
                               1, (78, 22, 10))
        else:
            text = font.render("RES-R: " + str(self.res_r) + "(+" + str(self.res_r_add) + ")",
                               1, (78, 22, 10))
        text_x = 765
        text_y = 475
        screen.blit(text, (text_x, text_y))

        if self.is_map_rendered == 0:

            pygame.draw.rect(screen, (125, 120, 74),
                             (724, 380, 200, 70))

            font = pygame.font.Font(None, 40)
            text = font.render("BLUE",
                               1, (28, 22, 210))
            text_x = 788
            text_y = 403
            screen.blit(text, (text_x, text_y))
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
            sprite.rect.y = 300
            all_sprites.draw(screen)

            self.is_map_rendered = 1

    def get_cell(self, mouse_position):
        x_pos, y_pos = mouse_position
        if self.par_click == 0 or self.par_click == 2\
                or self.par_click == 11 or self.par_click == 12\
                or self.par_click == 110 or self.par_click == 120:
            if ((x_pos <= 5 or x_pos >= self.width - 5)
                or (y_pos <= 5 or y_pos >= self.height - 5))\
                    and self.select is None:
                    if self.par_click != 2:
                        if sprite.rect.collidepoint((x_pos, y_pos)):
                            print("END TURN")

                            for unit in map_units.keys():
                                map_units[unit].moved = 0

                            if self.turn == 1:
                                self.turn = 2
                                self.res_b += self.res_b_add

                                pygame.draw.rect(screen, (125, 120, 74),
                                                 (724, 380, 200, 70))

                                font = pygame.font.Font(None, 40)
                                text = font.render("RED",
                                                   1, (218, 22, 10))
                                text_x = 795
                                text_y = 403
                                screen.blit(text, (text_x, text_y))

                            elif self.turn == 2:
                                self.turn = 1
                                self.res_r += self.res_r_add

                                pygame.draw.rect(screen, (125, 120, 74),
                                                 (790, 380, 70, 70))

                                font = pygame.font.Font(None, 40)
                                text = font.render("BLUE",
                                                   1, (28, 22, 210))
                                text_x = 788
                                text_y = 403
                                screen.blit(text, (text_x, text_y))
                        elif create_unit.rect.collidepoint((x_pos, y_pos)):
                            print("CREATE NEW")
                            self.par_click = 10
                        elif move_unit.rect.collidepoint((x_pos, y_pos)):
                            print("MOVE")
                            self.par_click = 11
                        elif damage_unit.rect.collidepoint((x_pos, y_pos)):
                            print("DAMAGE")
                            self.par_click = 12
                        else:
                            print("miss", x_pos, y_pos, sep="-------")
                        self.b_x_y = None
            elif (self.select is not None and self.par_click == 2)\
                    or self.par_click == 0 or self.par_click == 2\
                    or self.par_click == 11 or self.par_click == 12\
                    or self.par_click == 110 or self.par_click == 120:
                b_x_pos = (x_pos - 10) // 30
                b_y_pos = (y_pos - 10) // 30
                print(b_x_pos, b_y_pos)
                self.b_x_y = []
                self.b_x_y.append(b_x_pos)
                self.b_x_y.append(b_y_pos)
                self.arr.append([b_x_pos, b_y_pos])
                coord = (b_x_pos, b_y_pos)
                coord_px = (b_x_pos * BOARD_S + 10, b_y_pos * BOARD_S + 10)
                if self.par_click == 2:
                    warrior = None
                    archer = None
                    priest = None
                    if self.board[b_x_pos][b_y_pos] == -11 or self.board[b_x_pos][b_y_pos] == -21:
                        need_render = 0
                        if self.select in range(11, 16) and self.board[b_x_pos][b_y_pos] == -11:
                            if self.select == 11 and b_x_pos < 11:
                                warrior = WarriorBlue(coord_px, screen)
                                if (self.res_b - warrior.cell) >= 0:
                                    self.board[b_x_pos][b_y_pos] = 13
                                    self.res_b -= warrior.cell
                                    need_render = 1
                                else:
                                    print("NO RES BLUE")
                            elif self.select == 12 and b_x_pos < 11:
                                archer = ArcherBlue(coord_px, screen)
                                if (self.res_b - archer.cell) >= 0:
                                    self.board[b_x_pos][b_y_pos] = 13
                                    self.res_b -= archer.cell
                                    need_render = 2
                                else:
                                    print("NO RES BLUE")
                            elif self.select == 13 and b_x_pos < 11:
                                priest = PriestBlue(coord_px, screen)
                                if (self.res_b - priest.cell) >= 0:
                                    self.board[b_x_pos][b_y_pos] = 13
                                    self.res_b -= priest.cell
                                    need_render = 3
                                else:
                                    print("NO RES BLUE")
                        elif self.select in range(21, 26) and self.board[b_x_pos][b_y_pos] == -21:
                            if self.select == 21 and b_x_pos > 11:
                                warrior = WarriorRed(coord_px, screen)
                                if (self.res_r - warrior.cell) >= 0:
                                    self.board[b_x_pos][b_y_pos] = 23
                                    self.res_r -= warrior.cell
                                    need_render = 1
                                else:
                                    print("NO RES RED")
                            elif self.select == 22 and b_x_pos > 11:
                                archer = ArcherRed(coord_px, screen)
                                if (self.res_b - archer.cell) >= 0:
                                    self.board[b_x_pos][b_y_pos] = 13
                                    self.res_b -= archer.cell
                                    need_render = 2
                                else:
                                    print("NO RES BLUE")
                            elif self.select == 23 and b_x_pos > 11:
                                priest = PriestRed(coord_px, screen)
                                if (self.res_b - priest.cell) >= 0:
                                    self.board[b_x_pos][b_y_pos] = 13
                                    self.res_b -= priest.cell
                                    need_render = 3
                                else:
                                    print("NO RES BLUE")

                        if need_render == 1:
                            map_units[coord] = warrior
                            warrior.render()
                            warrior.all_sprites.draw(screen)
                        elif need_render == 2:
                            map_units[coord] = archer
                            archer.render()
                            archer.all_sprites.draw(screen)
                        elif need_render == 3:
                            map_units[coord] = priest
                            priest.render()
                            priest.all_sprites.draw(screen)

                        self.select = None
                        self.par_click = 0
                elif self.par_click == 11 or self.par_click == 12:
                    try:
                        self.select_unit = map_units[coord]
                        if self.par_click == 11:
                            self.par_click = 110
                            self.select_coord = coord
                        elif self.par_click == 12:
                            self.par_click = 120
                            self.select_coord = coord
                    except KeyError:
                        print("TRY OTHER")
                elif self.par_click == 110:
                    print("Ready to move", coord)
                    unit = None
                    if self.turn == 1:
                        if self.select_unit.name == "warrior_b":
                            if self.board[coord[0]][coord[1]] == -11:
                                unit = WarriorBlue(coord_px, screen, self.select_unit.health, self.select_unit.moved)
                        if self.select_unit.name == "archer_b":
                            if self.board[coord[0]][coord[1]] == -11:
                                unit = ArcherBlue(coord_px, screen, self.select_unit.health, self.select_unit.moved)
                        if self.select_unit.name == "priest_b":
                            if self.board[coord[0]][coord[1]] == -11:
                                unit = PriestBlue(coord_px, screen, self.select_unit.health, self.select_unit.moved)
                    else:
                        if self.select_unit.name == "warrior_r":
                            if self.board[coord[0]][coord[1]] == -21:
                                unit = WarriorRed(coord_px, screen, self.select_unit.health, self.select_unit.moved)
                        if self.select_unit.name == "archer_r":
                            if self.board[coord[0]][coord[1]] == -21:
                                unit = ArcherRed(coord_px, screen, self.select_unit.health, self.select_unit.moved)
                        if self.select_unit.name == "priest_r":
                            if self.board[coord[0]][coord[1]] == -21:
                                unit = PriestRed(coord_px, screen, self.select_unit.health, self.select_unit.moved)

                    if unit is not None and unit.moved + 1 <= unit.move:
                        pygame.draw.rect(self.screen, (0, 0, 0),
                                         (self.select_coord[0] * BOARD_S + 10,
                                          self.select_coord[1] * BOARD_S + 10, 30, 30))

                        self.board[coord[0]][coord[1]] = self.board[self.select_coord[0]][self.select_coord[1]]
                        self.board[self.select_coord[0]][self.select_coord[1]] = 0

                        unit.render()
                        map_units[coord] = unit
                        map_units[self.select_coord] = None
                        map_units.pop(self.select_coord)
                        unit.all_sprites.draw(screen)
                        unit.moved += 1
                        self.par_click = 0
                        print(unit.moved)

        elif self.par_click == 10:
            if warrior_select_b.rect.collidepoint((x_pos, y_pos)) and self.turn == 1:
                self.par_click = 2
                self.select = 11
                print("WARRIOR BLUE SELECTED")
            elif warrior_select_r.rect.collidepoint((x_pos, y_pos)) and self.turn == 2:
                self.par_click = 2
                self.select = 21
                print("WARRIOR RED SELECTED")
            elif archer_select_b.rect.collidepoint((x_pos, y_pos)) and self.turn == 1:
                self.par_click = 2
                self.select = 12
                print("ARCHER BLUE SELECTED")
            elif archer_select_r.rect.collidepoint((x_pos, y_pos)) and self.turn == 2:
                self.par_click = 2
                self.select = 22
                print("ARCHER RED SELECTED")
            elif priest_select_b.rect.collidepoint((x_pos, y_pos)) and self.turn == 1:
                self.par_click = 2
                self.select = 13
                print("PRIEST BLUE SELECTED")
            elif priest_select_r.rect.collidepoint((x_pos, y_pos)) and self.turn == 2:
                self.par_click = 2
                self.select = 23
                print("PRIEST RED SELECTED")

    def on_click(self):
        if self.b_x_y is not None:
            x_pos, y_pos = self.b_x_y[0], self.b_x_y[1]
            if self.board[x_pos][y_pos] != 1 and self.par_click != 11 and self.par_click != 12:
                pygame.draw.rect(self.screen,
                                 self.color[self.board[x_pos][y_pos]],
                                 (int(x_pos) *
                                  BOARD_S + 10,
                                  int(y_pos) *
                                  BOARD_S + 10, 30, 30), 1)
                # try:
                #     print(map_units[(x_pos, y_pos)])
                #     unit = map_units[(x_pos, y_pos)]
                #     unit.get_damage(5)
                #     print(unit.health)
                # except KeyError:
                #     print("Try other")

    def get_click(self, mouse_pos):
        self.get_cell(mouse_pos)
        print(self.par_click)
        if self.par_click == 2 or self.par_click == 11 or self.par_click == 12:
            self.on_click()

