import pygame


# размеры поля в клетках
# ширина
BOARD_W = 23
# высота
BOARD_H = 17
# ширина и высота клетки в px
BOARD_S = 30

# размеры окошка в px
size = width, height = BOARD_W * BOARD_S + 250,\
                       BOARD_H * BOARD_S + 120

# инициализия музыки
pygame.mixer.init()

# инициализация времени
clock = pygame.time.Clock()

# главная тема игры
main_theme = pygame.mixer.music.load("music\\main3.mp3")


# другие звуки в игре
sound_change_turn = pygame.mixer.Sound("music\\button_end.wav")
archer_attack = pygame.mixer.Sound("music\\archer_attack.wav")
warrior_attack = pygame.mixer.Sound("music\\warrior_attack.wav")
heal = pygame.mixer.Sound("music\\heal.wav")
build = pygame.mixer.Sound("music\\build.wav")
spawn = pygame.mixer.Sound("music\\spawn.wav")
u_break = pygame.mixer.Sound("music\\break.wav")
death = pygame.mixer.Sound("music\\death.wav")
end_game_music = pygame.mixer.Sound("music\\end_game.wav")
button = pygame.mixer.Sound("music\\button.wav")
error = pygame.mixer.Sound("music\\error.wav")
button_unit = pygame.mixer.Sound("music\\button.wav")
move = pygame.mixer.Sound("music\\move.wav")
click = pygame.mixer.Sound("music\\click.wav")


# создание окошка
screen = pygame.display.set_mode(size)
# новое имя окошка
pygame.display.set_caption("The Best Strategy Game")
