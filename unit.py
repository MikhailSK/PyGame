import os
from screen import *

pygame.init()
time = pygame.time.Clock()

map_units = {}

unit_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()


def win(winner):
    screen.fill((0, 0, 0))
    print(winner)


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


class CreateUnit(pygame.sprite.Sprite):
    image = load_image("create_unit.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = CreateUnit.image
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 538


class WarriorUnitSelectB(pygame.sprite.Sprite):
    image = load_image("warrior_b.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = WarriorUnitSelectB.image
        self.rect = self.image.get_rect()
        self.rect.x = 90
        self.rect.y = 538


class WarriorUnitSelectR(pygame.sprite.Sprite):
    image = load_image("warrior_r.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = WarriorUnitSelectR.image
        self.rect = self.image.get_rect()
        self.rect.x = 124
        self.rect.y = 538


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

    def move(self, coord):
        pass

    def get_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.dead()

    def put_damage(self, coord):
        pass

    def render(self, coord):
        pass

    def dead(self):
        print(self.x, self.y)
        pygame.draw.rect(self.screen, (150, 190, 16),
                         (self.x, self.y, 30, 30))
        pygame.display.flip()
        print("DEAD")

    def get_info(self):
        print("INFO GET")
        pygame.draw.rect(screen, (238, 160, 74),
                         (724, 25, 200, 230))
        font = pygame.font.Font(None, 28)

        text = font.render("Name: " + str(self.name),
                           1, (78, 22, 10))
        text_x = 745
        text_y = 40
        screen.blit(text, (text_x, text_y))

        text = font.render("Max Health: " + str(self.max_health),
                           1, (78, 22, 10))
        text_x = 745
        text_y = 70
        screen.blit(text, (text_x, text_y))

        text = font.render("Health: " + str(self.health),
                           1, (78, 22, 10))
        text_x = 745
        text_y = 100
        screen.blit(text, (text_x, text_y))

        text = font.render("Damage: " + str(self.damage),
                           1, (78, 22, 10))
        text_x = 745
        text_y = 130
        screen.blit(text, (text_x, text_y))

        text = font.render("Range: " + str(self.atk_range),
                           1, (78, 22, 10))
        text_x = 745
        text_y = 160
        screen.blit(text, (text_x, text_y))

        text = font.render("Move: " + str(self.move),
                           1, (78, 22, 10))
        text_x = 745
        text_y = 190
        screen.blit(text, (text_x, text_y))

        text = font.render("Coords: " + str(self.coord),
                           1, (78, 22, 10))
        text_x = 745
        text_y = 220
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
        pygame.draw.rect(self.screen, (150, 190, 16), (self.x, self.y, 30, 30))
        pygame.display.flip()
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
        pygame.display.flip()
        print("DEAD")
        win("Blue")


class WarriorMgRed(pygame.sprite.Sprite):
    def __init__(self, group, parent):
        super().__init__(group)
        self.image = parent.image
        self.rect = self.image.get_rect()


class WarriorRed(MainUnit):
    def __init__(self, coord, screen):
        super().__init__(screen)
        self.all_sprites = pygame.sprite.Group()
        self.name = "warrior_r"
        self.coord = coord
        self.damage = 1
        self.move = 1
        self.atk_range = 1
        #
        self.health = 5
        #
        self.max_health = 5
        self.image = load_image(self.name + ".png")

    def render(self, **kwargs):
        m_castle = CastleMgRed(self.all_sprites, self)
        m_castle.rect.x = self.coord[0] + 1
        m_castle.rect.y = self.coord[1] + 1

    def dead(self):
        self.x, self.y = self.coord[0], self.coord[1]
        pygame.draw.rect(self.screen, (150, 190, 16), (self.x, self.y, 30, 30))
        pygame.display.flip()
        print("DEAD" + self.name)


class WarriorMgRed(pygame.sprite.Sprite):
    def __init__(self, group, parent):
        super().__init__(group)
        self.image = parent.image
        self.rect = self.image.get_rect()


class WarriorBlue(MainUnit):
    def __init__(self, coord, screen):
        super().__init__(screen)
        self.all_sprites = pygame.sprite.Group()
        self.name = "warrior_b"
        self.coord = coord
        self.damage = 1
        self.move = 1
        self.atk_range = 1
        #
        self.health = 5
        #
        self.max_health = 5
        self.image = load_image(self.name + ".png")

    def render(self, **kwargs):
        m_castle = CastleMgRed(self.all_sprites, self)
        m_castle.rect.x = self.coord[0] + 1
        m_castle.rect.y = self.coord[1] + 1

    def dead(self):
        self.x, self.y = self.coord[0], self.coord[1]
        pygame.draw.rect(self.screen, (150, 190, 16), (self.x, self.y, 30, 30))
        pygame.display.flip()
        print("DEAD" + self.name)
