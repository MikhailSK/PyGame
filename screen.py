import pygame


BOARD_W = 23
BOARD_H = 17
BOARD_S = 30

size = width, height = BOARD_W * BOARD_S + 250,\
                       BOARD_H * BOARD_S + 120
pygame.mixer.init()

main_theme = pygame.mixer.music.load("music\\main3.mp3")

# main_theme = pygame.mixer.music.load("music\\main2.wav")

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


screen = pygame.display.set_mode(size)
pygame.display.set_caption("The Best Strategy Game")
