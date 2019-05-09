import os
from screen import *

pygame.init()

# словарь: координата клетки: объект юнита
map_units = {}

# спрайт кнопки конца хода
end_turn = pygame.sprite.Sprite()


# фунция конца игры
def win(winner):
    screen.fill((0, 0, 0))
    end_game_music.play(-1)
    print(winner)
    pygame.mixer.music.stop()


# загрузка изображения в виде surface
def load_image(name, color_key=None):
    fullname = os.path.join('data', name)

    try:
        image = pygame.image.load(fullname).convert()

        if color_key is not None:
            if color_key == -1:
                color_key = image.get_at((0, 0))
            image.set_colorkey(color_key)

        else:
            image = image.convert_alpha()

        return image

    except pygame.error as message:

        print('Cannot load image:', name)

        raise SystemExit(message)


# начальный экран
class StartGame(pygame.sprite.Sprite):
    image = load_image("start_screen1.png")

    def __init__(self, group):

        super().__init__(group)
        self.image = StartGame.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


# конец игры: победа красного
class EndGameRed(pygame.sprite.Sprite):

    image = load_image("end_screen_b1.png")

    def __init__(self, group):

        super().__init__(group)

        self.image = EndGameRed.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


# конец игры: победа синего
class EndGameBlue(pygame.sprite.Sprite):

    image = load_image("end_screen_r1.png")

    def __init__(self, group):

        super().__init__(group)

        self.image = EndGameBlue.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


# спрайт-кнопка: создать юнита
class CreateUnit(pygame.sprite.Sprite):

    image = load_image("create_unit.png")

    def __init__(self, group):

        super().__init__(group)

        self.image = CreateUnit.image
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 538


# спрайт-кнопка: переместить юнита
class MoveUnit(pygame.sprite.Sprite):

    image = load_image("move_unit.png")

    def __init__(self, group):

        super().__init__(group)

        self.image = MoveUnit.image
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 538


# спрайт-кнопка: атаковать юнита
class DamageUnit(pygame.sprite.Sprite):

    image = load_image("damage_unit.png")

    def __init__(self, group):

        super().__init__(group)

        self.image = DamageUnit.image
        self.rect = self.image.get_rect()
        self.rect.x = 390
        self.rect.y = 538


# спрайт-кнопка: warrior blue
class WarriorUnitSelectB(pygame.sprite.Sprite):

    image = load_image("warrior_b.png")

    def __init__(self, group):

        super().__init__(group)

        self.image = WarriorUnitSelectB.image
        self.rect = self.image.get_rect()
        self.rect.x = 90
        self.rect.y = 541


# спрайт-кнопка: warrior red
class WarriorUnitSelectR(pygame.sprite.Sprite):

    image = load_image("warrior_r.png")

    def __init__(self, group):

        super().__init__(group)

        self.image = WarriorUnitSelectR.image
        self.rect = self.image.get_rect()
        self.rect.x = 124
        self.rect.y = 541


# спрайт-кнопка: archer blue
class ArcherUnitSelectB(pygame.sprite.Sprite):

    image = load_image("archer_b.png")

    def __init__(self, group):

        super().__init__(group)

        self.image = ArcherUnitSelectB.image
        self.rect = self.image.get_rect()
        self.rect.x = 90
        self.rect.y = 576


# спрайт-кнопка: archer red
class ArcherUnitSelectR(pygame.sprite.Sprite):

    image = load_image("archer_r.png")

    def __init__(self, group):

        super().__init__(group)

        self.image = ArcherUnitSelectR.image
        self.rect = self.image.get_rect()
        self.rect.x = 124
        self.rect.y = 576


# спрайт-кнопка: priest blue
class PriestUnitSelectB(pygame.sprite.Sprite):

    image = load_image("priest_b.png")

    def __init__(self, group):

        super().__init__(group)

        self.image = PriestUnitSelectB.image
        self.rect = self.image.get_rect()
        self.rect.x = 158
        self.rect.y = 541


# спрайт-кнопка: priest red
class PriestUnitSelectR(pygame.sprite.Sprite):

    image = load_image("priest_r.png")

    def __init__(self, group):

        super().__init__(group)

        self.image = PriestUnitSelectR.image
        self.rect = self.image.get_rect()
        self.rect.x = 193
        self.rect.y = 541


# спрайт-кнопка: miner blue
class MinerUnitSelectB(pygame.sprite.Sprite):

    image = load_image("miner_b.png")

    def __init__(self, group):

        super().__init__(group)

        self.image = MinerUnitSelectB.image
        self.rect = self.image.get_rect()
        self.rect.x = 158
        self.rect.y = 576


# спрайт-кнопка: miner blue
class MinerUnitSelectR(pygame.sprite.Sprite):

    image = load_image("miner_r.png")

    def __init__(self, group):

        super().__init__(group)

        self.image = MinerUnitSelectR.image
        self.rect = self.image.get_rect()
        self.rect.x = 193
        self.rect.y = 576


# класс юнита, от него наследуются все другие классы юнитов
class MainUnit:

    def __init__(self, m_screen):
        # имя
        self.name = ""

        # урон
        self.damage = 0

        # перемещение
        self.move = 0

        # координаты в клетках
        self.coord = [1, 1]

        # координаты в px
        self.x, self.y = self.coord[0] * BOARD_S + 10, self.coord[1] * BOARD_S + 10

        # тип юнита
        self.type = -1

        # радиус атаки
        self.atk_range = 0

        # здоровье
        self.health = 1

        # максимальное здоровье
        self.max_health = 1

        # экран
        self.screen = m_screen

        # стоимость в ресурсах
        self.cell = 0

        # насколько переместился за ход
        self.moved = 0

        # сколько раз атаковал за ход
        self.attacked = 0

        # сколько ресурсов в ход будет добавлять
        self.res_in_turn = 0

        self.par_image = 1

    # функция перемещения
    def move(self):
        pass

    # функция получения урона
    def get_damage(self, damage):

        self.health -= damage

        if self.health <= 0:
            self.dead()

    # функция атаки
    def put_damage(self, unit_damaged):

        # x атакующего в клетках
        x_1 = (self.coord[0] + 10) // 30
        # y атакующего в клетках
        y_1 = (self.coord[1] + 10) // 30
        # x атакуемого в клетках
        x_2 = (unit_damaged.coord[0] + 10) // 30
        # н атакуемого в клетках
        y_2 = (unit_damaged.coord[1] + 10) // 30

        if abs(x_1 - x_2) + abs(y_1 - y_2) <= self.atk_range:

            self.attacked += 1

            if "warrior" in self.name:
                warrior_attack.play()
                pygame.time.wait(int(warrior_attack.get_length() * 1000))
            if "priest" in self.name:
                heal.play()
                pygame.time.wait(int(heal.get_length() * 1000))
            if "archer" in self.name:
                archer_attack.play()
                pygame.time.wait(int(archer_attack.get_length() * 1000))

            unit_damaged.get_damage(self.damage)

    def render(self, coord, health):
        pass

    # функция смерти
    def dead(self):

        # координаты в px
        self.x, self.y = self.coord[0], self.coord[1]
        # координаты в клетках
        x_b, y_b = (self.coord[0] + 10) // 30, (self.coord[1] + 10) // 30

        # убираем этого юнита их map_units
        map_units[(x_b, y_b)] = None
        map_units.pop((x_b, y_b))

        # очищаем клетку от юнита
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, 30, 30))
        pygame.display.flip()

        print("DEAD" + self.name)

        # звук смерти/разрушения
        if "miner" in self.name:
            u_break.play()
            pygame.time.wait(int(u_break.get_length() * 1000))
        else:
            death.play()
            pygame.time.wait(int(death.get_length() * 1000))

    # показ ноформации о юните
    def get_info(self):

        print("INFO GET")

        button.play()

        pygame.draw.rect(screen, (238, 160, 74),
                         (724, 10, 200, 335))
        font = pygame.font.Font(None, 28)

        text = font.render("Name: " + str(self.name),
                           1, (78, 22, 10))
        text_x = 745
        text_y = 20
        screen.blit(text, (text_x, text_y))

        text = font.render("Max Health: " + str(self.max_health),
                           1, (78, 22, 10))
        text_x = 745
        text_y = 50
        screen.blit(text, (text_x, text_y))

        text = font.render("Health: " + str(self.health),
                           1, (78, 22, 10))
        text_x = 745
        text_y = 80
        screen.blit(text, (text_x, text_y))

        text = font.render("Damage: " + str(self.damage),
                           1, (78, 22, 10))
        text_x = 745
        text_y = 110
        screen.blit(text, (text_x, text_y))

        text = font.render("Range: " + str(self.atk_range),
                           1, (78, 22, 10))
        text_x = 745
        text_y = 140
        screen.blit(text, (text_x, text_y))

        text = font.render("Move: " + str(self.move),
                           1, (78, 22, 10))
        text_x = 745
        text_y = 170
        screen.blit(text, (text_x, text_y))

        text = font.render("Price: " + str(self.cell),
                           1, (78, 22, 10))
        text_x = 745
        text_y = 200
        screen.blit(text, (text_x, text_y))

        text = font.render("Coords: " +
                           str((self.coord[0] + 10) // 30) + "-"
                           + str((self.coord[1] + 10) // 30),
                           1, (78, 22, 10))
        text_x = 745
        text_y = 230

        screen.blit(text, (text_x, text_y))

        text = font.render("Moved: " +
                           str(self.moved),
                           1, (78, 22, 10))
        text_x = 745
        text_y = 260

        screen.blit(text, (text_x, text_y))

        text = font.render("Attacked: " +
                           str(self.attacked),
                           1, (78, 22, 10))
        text_x = 745
        text_y = 290

        screen.blit(text, (text_x, text_y))

        text = font.render("Add res in turn: " +
                           str(self.res_in_turn),
                           1, (78, 22, 10))
        text_x = 745
        text_y = 320

        screen.blit(text, (text_x, text_y))


# Горы загрузка
class WallMg(pygame.sprite.Sprite):

    def __init__(self, group, parent):

        super().__init__(group)

        self.image = parent.image
        self.rect = self.image.get_rect()


# Горы
class Wall(MainUnit):
    def __init__(self, coord, m_screen):

        super().__init__(m_screen)

        self.all_sprites = pygame.sprite.Group()
        self.name = "wall"
        self.health = 900000
        self.coord = coord
        self.image = None

    def render(self, **kwargs):

        if self.par_image == 1:
            self.image = load_image(self.name + ".png")
            self.par_image = 2
        elif self.par_image == 2:
            self.image = load_image(self.name + "_1.png")
            self.par_image = 3
        elif self.par_image == 3:
            self.image = load_image(self.name + "_2.png")
            self.par_image = 4
        elif self.par_image == 4:
            self.image = load_image(self.name + "_3.png")
            self.par_image = 5
        elif self.par_image == 5:
            self.image = load_image(self.name + "_4.png")
            self.par_image = 6
        elif self.par_image == 6:
            self.image = load_image(self.name + "_4.png")
            self.par_image = 7
        else:
            self.image = load_image(self.name + "_6.png")
            self.par_image = 1

        m_wall = WallMg(self.all_sprites, self)
        m_wall.rect.x = self.coord[0]
        m_wall.rect.y = self.coord[1]


# замок синего загрузка
class CastleMgBlue(pygame.sprite.Sprite):

    def __init__(self, group, parent):

        super().__init__(group)

        self.image = parent.image
        self.rect = self.image.get_rect()


# замок синего
class CastleBlue(MainUnit):

    def __init__(self, coord, m_screen):

        super().__init__(m_screen)

        self.all_sprites = pygame.sprite.Group()
        self.name = "blue_castle"
        self.coord = coord
        self.health = 15
        self.max_health = 15
        self.image = None

    def render(self, **kwargs):

        if self.par_image == 1:
            self.image = load_image(self.name + ".png")
            self.par_image = 2
        elif self.par_image == 2:
            self.image = load_image(self.name + "2.png")
            self.par_image = 3
        else:
            self.image = load_image(self.name + "1.png")
            self.par_image = 1

        m_castle = CastleMgBlue(self.all_sprites, self)
        m_castle.rect.x = self.coord[0] + 1
        m_castle.rect.y = self.coord[1] + 1

    def dead(self):

        print("DEAD")

        self.x, self.y = self.coord[0], self.coord[1]
        map_units[(0, 8)] = None
        map_units.pop((0, 8))
        winner = "Red"
        win(winner)


# замок красного загрузка
class CastleMgRed(pygame.sprite.Sprite):

    def __init__(self, group, parent):

        super().__init__(group)

        self.image = parent.image
        self.rect = self.image.get_rect()


# замок красного
class CastleRed(MainUnit):
    def __init__(self, coord, m_screen):

        super().__init__(m_screen)

        self.all_sprites = pygame.sprite.Group()
        self.name = "red_castle"
        self.coord = coord
        self.health = 15
        self.max_health = 15
        self.image = None

    def render(self, **kwargs):

        if self.par_image == 1:
            self.image = load_image(self.name + ".png")
            self.par_image = 2
        elif self.par_image == 2:
            self.image = load_image(self.name + "2.png")
            self.par_image = 3
        else:
            self.image = load_image(self.name + "1.png")
            self.par_image = 1

        m_castle = CastleMgRed(self.all_sprites, self)
        m_castle.rect.x = self.coord[0] + 1
        m_castle.rect.y = self.coord[1] + 1

    def dead(self):

        print("DEAD")

        self.x, self.y = self.coord[0], self.coord[1]
        pygame.draw.rect(self.screen, (150, 190, 16), (self.x, self.y, 30, 30))
        map_units[(22, 8)] = None
        map_units.pop((22, 8))
        pygame.display.flip()
        win("Blue")


# воин красный загрузка
class WarriorMgRed(pygame.sprite.Sprite):

    def __init__(self, group, parent):

        super().__init__(group)

        self.image = parent.image
        self.rect = self.image.get_rect()


# воин красный
class WarriorRed(MainUnit):

    def __init__(self, coord, m_screen, health=5, moved=0, attacked=0):

        super().__init__(m_screen)

        self.all_sprites = pygame.sprite.Group()
        self.name = "warrior_r"
        self.coord = coord
        self.damage = 1
        self.move = 1
        self.moved = moved
        self.cell = 2
        self.attacked = attacked
        self.atk_range = 1
        self.health = health
        self.max_health = 5
        self.image = load_image(self.name + ".png")

    def render(self, **kwargs):

        if self.par_image == 1:
            self.image = load_image(self.name + ".png")
            self.par_image = 0
        elif self.par_image == 2:
            self.image = load_image(self.name + "2.png")
            self.par_image = 1
        else:
            self.image = load_image(self.name + "1.png")
            self.par_image = 2

        warrior_r = WarriorMgRed(self.all_sprites, self)
        warrior_r.rect.x = self.coord[0] + 1
        warrior_r.rect.y = self.coord[1] + 1


# воин красный загрузка
class WarriorMgBlue(pygame.sprite.Sprite):

    def __init__(self, group, parent):

        super().__init__(group)

        self.image = parent.image
        self.rect = self.image.get_rect()


# воин красный
class WarriorBlue(MainUnit):

    def __init__(self, coord, m_screen, health=5, moved=0, attacked=0):

        super().__init__(m_screen)

        self.all_sprites = pygame.sprite.Group()
        self.name = "warrior_b"
        self.coord = coord
        self.damage = 1
        self.move = 1
        self.moved = moved
        self.cell = 2
        self.attacked = attacked
        self.atk_range = 1
        self.health = health
        self.max_health = 5
        self.image = load_image(self.name + ".png")

    def render(self, **kwargs):

        if self.par_image == 1:
            self.image = load_image(self.name + ".png")
            self.par_image = 0
        elif self.par_image == 2:
            self.image = load_image(self.name + "2.png")
            self.par_image = 1
        else:
            self.image = load_image(self.name + "1.png")
            self.par_image = 2

        warrior_b = WarriorMgBlue(self.all_sprites, self)
        warrior_b.rect.x = self.coord[0] + 1
        warrior_b.rect.y = self.coord[1] + 1


# лучник синий загрузка
class ArcherMgBlue(pygame.sprite.Sprite):

    def __init__(self, group, parent):

        super().__init__(group)

        self.image = parent.image
        self.rect = self.image.get_rect()


# лучник синий
class ArcherBlue(MainUnit):
    def __init__(self, coord, m_screen, health=4, moved=0, attacked=0):

        super().__init__(m_screen)

        self.all_sprites = pygame.sprite.Group()
        self.name = "archer_b"
        self.coord = coord
        self.damage = 1
        self.move = 2
        self.moved = moved
        self.cell = 3
        self.attacked = attacked
        self.atk_range = 2
        self.health = health
        self.max_health = 4
        self.image = load_image(self.name + ".png")

    def render(self, **kwargs):

        if self.par_image == 1:
            self.image = load_image(self.name + ".png")
            self.par_image = 0
        elif self.par_image == 2:
            self.image = load_image(self.name + "2.png")
            self.par_image = 1
        else:
            self.image = load_image(self.name + "1.png")
            self.par_image = 2

        archer_b = ArcherMgBlue(self.all_sprites, self)
        archer_b.rect.x = self.coord[0] + 1
        archer_b.rect.y = self.coord[1] + 1


# лучник красный загрузка
class ArcherMgRed(pygame.sprite.Sprite):

    def __init__(self, group, parent):

        super().__init__(group)

        self.image = parent.image
        self.rect = self.image.get_rect()


# лучник красный
class ArcherRed(MainUnit):
    def __init__(self, coord, m_screen, health=4, moved=0, attacked=0):

        super().__init__(m_screen)

        self.all_sprites = pygame.sprite.Group()
        self.name = "archer_r"
        self.coord = coord
        self.damage = 1
        self.move = 2
        self.moved = moved
        self.cell = 3
        self.attacked = attacked
        self.atk_range = 2
        self.health = health
        self.max_health = 4
        self.image = load_image(self.name + ".png")

    def render(self, **kwargs):

        if self.par_image == 1:
            self.image = load_image(self.name + ".png")
            self.par_image = 0
        elif self.par_image == 2:
            self.image = load_image(self.name + "2.png")
            self.par_image = 1
        else:
            self.image = load_image(self.name + "1.png")
            self.par_image = 2

        archer_r = ArcherMgRed(self.all_sprites, self)
        archer_r.rect.x = self.coord[0] + 1
        archer_r.rect.y = self.coord[1] + 1


# священник синий загрузка
class PriestMgBlue(pygame.sprite.Sprite):

    def __init__(self, group, parent):

        super().__init__(group)

        self.image = parent.image
        self.rect = self.image.get_rect()


# священник синий
class PriestBlue(MainUnit):

    def __init__(self, coord, m_screen, health=4, moved=0, attacked=0):

        super().__init__(m_screen)

        self.all_sprites = pygame.sprite.Group()
        self.name = "priest_b"
        self.coord = coord
        self.damage = -1
        self.move = 1
        self.moved = moved
        self.cell = 5
        self.attacked = attacked
        self.atk_range = 2
        self.health = health
        self.max_health = 4
        self.image = load_image(self.name + ".png")

    def render(self, **kwargs):

        if self.par_image == 1:
            self.image = load_image(self.name + ".png")
            self.par_image = 0
        elif self.par_image == 2:
            self.image = load_image(self.name + "2.png")
            self.par_image = 1
        else:
            self.image = load_image(self.name + "1.png")
            self.par_image = 2

        priest_b = PriestMgBlue(self.all_sprites, self)
        priest_b.rect.x = self.coord[0] + 1
        priest_b.rect.y = self.coord[1] + 1


# священник красный загрузка
class PriestMgRed(pygame.sprite.Sprite):

    def __init__(self, group, parent):

        super().__init__(group)

        self.image = parent.image
        self.rect = self.image.get_rect()


# священник красный
class PriestRed(MainUnit):

    def __init__(self, coord, m_screen, health=4, moved=0, attacked=0):

        super().__init__(m_screen)

        self.all_sprites = pygame.sprite.Group()
        self.name = "priest_r"
        self.coord = coord
        self.damage = -1
        self.move = 1
        self.moved = moved
        self.cell = 5
        self.attacked = attacked
        self.atk_range = 2
        self.health = health
        self.max_health = 4
        self.image = load_image(self.name + ".png")

    def render(self, **kwargs):

        if self.par_image == 1:
            self.image = load_image(self.name + ".png")
            self.par_image = 0
        elif self.par_image == 2:
            self.image = load_image(self.name + "2.png")
            self.par_image = 1
        else:
            self.image = load_image(self.name + "1.png")
            self.par_image = 2

        priest_r = PriestMgRed(self.all_sprites, self)
        priest_r.rect.x = self.coord[0] + 1
        priest_r.rect.y = self.coord[1] + 1


# рудник красный загрузка
class MinerMgRed(pygame.sprite.Sprite):

    def __init__(self, group, parent):

        super().__init__(group)

        self.image = parent.image
        self.rect = self.image.get_rect()


# рудник красный
class MinerRed(MainUnit):
    def __init__(self, coord, m_screen, health=8, moved=0, attacked=0):

        super().__init__(m_screen)

        self.all_sprites = pygame.sprite.Group()
        self.name = "miner_r"
        self.coord = coord
        self.damage = 0
        self.move = 0
        self.moved = moved
        self.cell = 7
        self.atk_range = 0
        self.res_in_turn = 2
        self.attacked = attacked
        self.health = health
        self.max_health = 8
        self.image = load_image(self.name + ".png")

    def render(self, **kwargs):

        if self.par_image == 1:
            self.image = load_image(self.name + ".png")
            self.par_image = 0
        elif self.par_image == 2:
            self.image = load_image(self.name + "2.png")
            self.par_image = 1
        else:
            self.image = load_image(self.name + "1.png")
            self.par_image = 2

        miner_r = MinerMgRed(self.all_sprites, self)
        miner_r.rect.x = self.coord[0] + 1
        miner_r.rect.y = self.coord[1] + 1


# рудник синий загрузка
class MinerMgBlue(pygame.sprite.Sprite):

    def __init__(self, group, parent):

        super().__init__(group)

        self.image = parent.image
        self.rect = self.image.get_rect()


# рудник синий
class MinerBlue(MainUnit):

    def __init__(self, coord, m_screen, health=8, moved=0, attacked=0):

        super().__init__(m_screen)

        self.all_sprites = pygame.sprite.Group()
        self.name = "miner_b"
        self.coord = coord
        self.damage = 0
        self.move = 0
        self.moved = moved
        self.cell = 7
        self.res_in_turn = 2
        self.attacked = attacked
        self.atk_range = 0
        self.health = health
        self.max_health = 8
        self.image = None

    def render(self, **kwargs):

        if self.par_image == 1:
            self.image = load_image(self.name + ".png")
            self.par_image = 0
        elif self.par_image == 2:
            self.image = load_image(self.name + "2.png")
            self.par_image = 1
        else:
            self.image = load_image(self.name + "1.png")
            self.par_image = 2

        miner_r = MinerMgRed(self.all_sprites, self)
        miner_r.rect.x = self.coord[0] + 1
        miner_r.rect.y = self.coord[1] + 1
