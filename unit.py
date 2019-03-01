import pygame
import os
from screen import *

End_game = 0
pygame.init()
time = pygame.time.Clock()

unit_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()


def win(winer):
    screen.fill((0, 0, 0))
    print(winer)


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


class MainUnit:
    def __init__(self, screen):
        self.name = ""
        self.atk = 0
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
        pygame.draw.rect(self.screen, (150, 190, 16), (self.x, self.y, 30, 30))
        pygame.display.flip()
        print("DEAD")


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
        # sprite = pygame.sprite.Sprite()
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
        win("Red")


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
