from Board import *
from unit import *


board = Board(BOARD_W, BOARD_H, screen)
screen.fill((0, 0, 0))

pygame.display.set_icon(load_image('icon.png'))

running = True
par_space = 0
FPS = 20
res_r = 10
res_b = 10
par = 0
turn = 0

clock = pygame.time.Clock()
start_game = StartGame(all_sprites)
sap = 0

while running:
    if sap == 0:
        pygame.mixer.music.play(-1)
        sap = 1
    all_sprites.draw(screen)
    if par == 0 and turn > 0:
        board.render()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and turn >= 0:
            if turn != 0:
                if sap == 1:
                    sap = 2
                    # sound1.play()
                new_board_pos = ((event.pos[0] - 10) // 30,
                                 (event.pos[1] - 10) // 30)
                if event.button == 1:
                    board.get_click(event.pos)
                    if board.turn != turn:
                        print(turn)
                        turn = board.turn
                        par = 1
                    board.render()
                    if board.end == 1:
                        turn = -3
                    if board.end == 2:
                        turn = -4
                elif event.button == 3:
                    try:
                        map_units[new_board_pos].get_info()
                    except KeyError:
                        print("empty cell")
            else:
                turn = 1
                screen.fill((0, 0, 0))
                all_sprites.remove(start_game)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                pygame.mixer.music.set_volume(0)
            elif event.key == pygame.K_m:
                pygame.mixer.music.set_volume(1)
            elif event.key == pygame.K_b:
                pygame.mixer.music.set_volume(
                    pygame.mixer.music.get_volume() - 0.1)
            elif event.key == pygame.K_v:
                pygame.mixer.music.set_volume(
                    pygame.mixer.music.get_volume() + 0.1)

        if turn == -3:
            end_screen = EndGameBlue(all_sprites)
        if turn == -4:
            end_screen = EndGameRed(all_sprites)
    pygame.display.flip()
    clock.tick(FPS)
