import os
from screen import *

pygame.init()
time = pygame.time.Clock()

map_units = {}

unit_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()


def win(winner):
    screen.fill((0, 0, 0))
    end_game_music.play(-1)
    print(winner)
    pygame.mixer.music.stop()


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


class StartGame(pygame.sprite.Sprite):
    image = load_image("start_screen.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = StartGame.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class EndGameRed(pygame.sprite.Sprite):
    image = load_image("end_screen_r.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = EndGameRed.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class EndGameBlue(pygame.sprite.Sprite):
    image = load_image("end_screen_b.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = EndGameRed.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class CreateUnit(pygame.sprite.Sprite):
    image = load_image("create_unit.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = CreateUnit.image
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 538


class MoveUnit(pygame.sprite.Sprite):
    image = load_image("move_unit.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = MoveUnit.image
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 538


class DamageUnit(pygame.sprite.Sprite):
    image = load_image("damage_unit.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = DamageUnit.image
        self.rect = self.image.get_rect()
        self.rect.x = 390
        self.rect.y = 538


class WarriorUnitSelectB(pygame.sprite.Sprite):
    image = load_image("warrior_b.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = WarriorUnitSelectB.image
        self.rect = self.image.get_rect()
        self.rect.x = 90
        self.rect.y = 541


class WarriorUnitSelectR(pygame.sprite.Sprite):
    image = load_image("warrior_r.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = WarriorUnitSelectR.image
        self.rect = self.image.get_rect()
        self.rect.x = 124
        self.rect.y = 541


class ArcherUnitSelectB(pygame.sprite.Sprite):
    image = load_image("archer_b.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = ArcherUnitSelectB.image
        self.rect = self.image.get_rect()
        self.rect.x = 90
        self.rect.y = 576


class ArcherUnitSelectR(pygame.sprite.Sprite):
    image = load_image("archer_r.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = ArcherUnitSelectR.image
        self.rect = self.image.get_rect()
        self.rect.x = 124
        self.rect.y = 576


class PriestUnitSelectB(pygame.sprite.Sprite):
    image = load_image("priest_b.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = PriestUnitSelectB.image
        self.rect = self.image.get_rect()
        self.rect.x = 158
        self.rect.y = 541


class PriestUnitSelectR(pygame.sprite.Sprite):
    image = load_image("priest_r.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = PriestUnitSelectR.image
        self.rect = self.image.get_rect()
        self.rect.x = 193
        self.rect.y = 541


class MinerUnitSelectB(pygame.sprite.Sprite):
    image = load_image("miner_b.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = MinerUnitSelectB.image
        self.rect = self.image.get_rect()
        self.rect.x = 158
        self.rect.y = 576


class MinerUnitSelectR(pygame.sprite.Sprite):
    image = load_image("miner_r.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = MinerUnitSelectR.image
        self.rect = self.image.get_rect()
        self.rect.x = 193
        self.rect.y = 576


class MainUnit:
    def __init__(self, screen):
        self.name = ""
        self.damage = 0
        self.move = 0
        self.coord = [1, 1]
        self.x, self.y = self.coord[0] * BOARD_S + 10, self.coord[1] * BOARD_S + 10
        self.type = -1
        self.atk_range = 0
        self.health = 1
        self.max_health = 1
        self.screen = screen
        self.cell = 0
        self.moved = 0
        self.attacked = 0
        self.res_in_turn = 0

    def move(self):
        pass

    def get_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.dead()

    def put_damage(self, unit_damaged):
        x_1 = (self.coord[0] + 10) // 30
        y_1 = (self.coord[1] + 10) // 30
        x_2 = (unit_damaged.coord[0] + 10) // 30
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

    def dead(self):
        self.x, self.y = self.coord[0], self.coord[1]
        x_b, y_b = (self.coord[0] + 10) // 30, (self.coord[1] + 10) // 30
        map_units[(x_b, y_b)] = None
        map_units.pop((x_b, y_b))
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, 30, 30))
        pygame.display.flip()
        print("DEAD" + self.name)
        if "miner" in self.name:
            u_break.play()
            pygame.time.wait(int(u_break.get_length() * 1000))
        else:
            death.play()
            pygame.time.wait(int(death.get_length() * 1000))

    def get_info(self):
        print("INFO GET")
        button.play()
        pygame.time.wait(int(button.get_length() * 1000))
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


class WallMg(pygame.sprite.Sprite):
    def __init__(self, group, parent):
        super().__init__(group)
        self.image = parent.image
        self.rect = self.image.get_rect()


class Wall(MainUnit):
    def __init__(self, coord, screen):
        super().__init__(screen)
        self.all_sprites = pygame.sprite.Group()
        self.name = "wall"
        self.health = 900000
        self.coord = coord
        self.image = load_image(self.name + ".png")

    def render(self, **kwargs):
        m_wall = WallMg(self.all_sprites, self)
        m_wall.rect.x = self.coord[0]
        m_wall.rect.y = self.coord[1]


class CastleMgBlue(pygame.sprite.Sprite):
    def __init__(self, group, parent):
        super().__init__(group)
        self.image = parent.image
        self.rect = self.image.get_rect()


class CastleBlue(MainUnit):
    def __init__(self, coord, screen):
        super().__init__(screen)
        self.all_sprites = pygame.sprite.Group()
        self.name = "blue_castle"
        self.coord = coord
        #
        self.health = 15
        #
        self.max_health = 15
        self.image = load_image(self.name + ".png")

    def render(self, **kwargs):
        m_castle = CastleMgBlue(self.all_sprites, self)
        m_castle.rect.x = self.coord[0] + 1
        m_castle.rect.y = self.coord[1] + 1

    def dead(self):
        self.x, self.y = self.coord[0], self.coord[1]
        print(self.x, self.y)
        map_units[(0, 8)] = None
        map_units.pop((0, 8))
        print("DEAD")
        winner = "Red"
        win(winner)


class CastleMgRed(pygame.sprite.Sprite):
    def __init__(self, group, parent):
        super().__init__(group)
        self.image = parent.image
        self.rect = self.image.get_rect()


class CastleRed(MainUnit):
    def __init__(self, coord, screen):
        super().__init__(screen)
        self.all_sprites = pygame.sprite.Group()
        self.name = "red_castle"
        self.coord = coord
        #
        self.health = 15
        #
        self.max_health = 15
        self.image = load_image(self.name + ".png")

    def render(self, **kwargs):
        m_castle = CastleMgRed(self.all_sprites, self)
        m_castle.rect.x = self.coord[0] + 1
        m_castle.rect.y = self.coord[1] + 1

    def dead(self):
        self.x, self.y = self.coord[0], self.coord[1]
        pygame.draw.rect(self.screen, (150, 190, 16), (self.x, self.y, 30, 30))
        map_units[(22, 8)] = None
        map_units.pop((22, 8))
        pygame.display.flip()
        print("DEAD")
        win("Blue")


class WarriorMgRed(pygame.sprite.Sprite):
    def __init__(self, group, parent):
        super().__init__(group)
        self.image = parent.image
        self.rect = self.image.get_rect()


class WarriorRed(MainUnit):
    def __init__(self, coord, screen, health=5, moved=0, attacked=0):
        super().__init__(screen)
        self.all_sprites = pygame.sprite.Group()
        self.name = "warrior_r"
        self.coord = coord
        self.damage = 1
        self.move = 1
        self.moved = moved
        self.cell = 2
        self.attacked = attacked
        self.atk_range = 1
        #
        self.health = health
        #
        self.max_health = 5
        self.image = load_image(self.name + ".png")

    def render(self, **kwargs):
        warrior_r = CastleMgRed(self.all_sprites, self)
        warrior_r.rect.x = self.coord[0] + 1
        warrior_r.rect.y = self.coord[1] + 1


class WarriorMgRed(pygame.sprite.Sprite):
    def __init__(self, group, parent):
        super().__init__(group)
        self.image = parent.image
        self.rect = self.image.get_rect()


class WarriorBlue(MainUnit):
    def __init__(self, coord, screen, health=5, moved=0, attacked=0):
        super().__init__(screen)
        self.all_sprites = pygame.sprite.Group()
        self.name = "warrior_b"
        self.coord = coord
        self.damage = 1
        self.move = 1
        self.moved = moved
        self.cell = 2
        self.attacked = attacked
        self.atk_range = 1
        #
        self.health = health
        #
        self.max_health = 5
        self.image = load_image(self.name + ".png")

    def render(self, **kwargs):
        warrior_b = CastleMgRed(self.all_sprites, self)
        warrior_b.rect.x = self.coord[0] + 1
        warrior_b.rect.y = self.coord[1] + 1


class ArcherMgBlue(pygame.sprite.Sprite):
    def __init__(self, group, parent):
        super().__init__(group)
        self.image = parent.image
        self.rect = self.image.get_rect()


class ArcherBlue(MainUnit):
    def __init__(self, coord, screen, health=4, moved=0, attacked=0):
        super().__init__(screen)
        self.all_sprites = pygame.sprite.Group()
        self.name = "archer_b"
        self.coord = coord
        self.damage = 100
        self.move = 2
        self.moved = moved
        self.cell = 3
        self.attacked = attacked
        self.atk_range = 200
        #
        self.health = health
        #
        self.max_health = 4
        self.image = load_image(self.name + ".png")

    def render(self, **kwargs):
        archer_b = ArcherMgBlue(self.all_sprites, self)
        archer_b.rect.x = self.coord[0] + 1
        archer_b.rect.y = self.coord[1] + 1


class ArcherMgRed(pygame.sprite.Sprite):
    def __init__(self, group, parent):
        super().__init__(group)
        self.image = parent.image
        self.rect = self.image.get_rect()


class ArcherRed(MainUnit):
    def __init__(self, coord, screen, health=4, moved=0, attacked=0):
        super().__init__(screen)
        self.all_sprites = pygame.sprite.Group()
        self.name = "archer_r"
        self.coord = coord
        self.damage = 1
        self.move = 2
        self.moved = moved
        self.cell = 3
        self.attacked = attacked
        self.atk_range = 2
        #
        self.health = health
        #
        self.max_health = 4
        self.image = load_image(self.name + ".png")

    def render(self, **kwargs):
        archer_r = ArcherMgRed(self.all_sprites, self)
        archer_r.rect.x = self.coord[0] + 1
        archer_r.rect.y = self.coord[1] + 1


class PriestMgBlue(pygame.sprite.Sprite):
    def __init__(self, group, parent):
        super().__init__(group)
        self.image = parent.image
        self.rect = self.image.get_rect()


class PriestBlue(MainUnit):
    def __init__(self, coord, screen, health=4, moved=0, attacked=0):
        super().__init__(screen)
        self.all_sprites = pygame.sprite.Group()
        self.name = "priest_b"
        self.coord = coord
        self.damage = -1
        self.move = 1
        self.moved = moved
        self.cell = 5
        self.attacked = attacked
        self.atk_range = 2
        #
        self.health = health
        #
        self.max_health = 4
        self.image = load_image(self.name + ".png")

    def render(self, **kwargs):
        priest_b = PriestMgBlue(self.all_sprites, self)
        priest_b.rect.x = self.coord[0] + 1
        priest_b.rect.y = self.coord[1] + 1


class PriestMgRed(pygame.sprite.Sprite):
    def __init__(self, group, parent):
        super().__init__(group)
        self.image = parent.image
        self.rect = self.image.get_rect()


class PriestRed(MainUnit):
    def __init__(self, coord, screen, health=4, moved=0, attacked=0):
        super().__init__(screen)
        self.all_sprites = pygame.sprite.Group()
        self.name = "priest_r"
        self.coord = coord
        self.damage = -1
        self.move = 1
        self.moved = moved
        self.cell = 5
        self.attacked = attacked
        self.atk_range = 2
        #
        self.health = health
        #
        self.max_health = 4
        self.image = load_image(self.name + ".png")

    def render(self, **kwargs):
        priest_r = PriestMgRed(self.all_sprites, self)
        priest_r.rect.x = self.coord[0] + 1
        priest_r.rect.y = self.coord[1] + 1


class MinerMgRed(pygame.sprite.Sprite):
    def __init__(self, group, parent):
        super().__init__(group)
        self.image = parent.image
        self.rect = self.image.get_rect()


class MinerRed(MainUnit):
    def __init__(self, coord, screen, health=8, moved=0, attacked=0):
        super().__init__(screen)
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
        #
        self.health = health
        #
        self.max_health = 8
        self.image = load_image(self.name + ".png")

    def render(self, **kwargs):
        miner_r = MinerMgRed(self.all_sprites, self)
        miner_r.rect.x = self.coord[0] + 1
        miner_r.rect.y = self.coord[1] + 1


class MinerMgBlue(pygame.sprite.Sprite):
    def __init__(self, group, parent):
        super().__init__(group)
        self.image = parent.image
        self.rect = self.image.get_rect()


class MinerBlue(MainUnit):
    def __init__(self, coord, screen, health=8, moved=0, attacked=0):
        super().__init__(screen)
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
        #
        self.health = health
        #
        self.max_health = 8
        self.image = load_image(self.name + ".png")

    def render(self, **kwargs):
        miner_r = MinerMgRed(self.all_sprites, self)
        miner_r.rect.x = self.coord[0] + 1
        miner_r.rect.y = self.coord[1] + 1
