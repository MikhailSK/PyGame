from Board import *
from unit import *


board = Board(BOARD_W, BOARD_H, screen)
screen.fill((0, 0, 0))

# новая иконка
pygame.display.set_icon(load_image('icon.png'))

running = True
FPS = 20
par = 0
turn = 0
poq = 0

start_game = StartGame(all_sprites)
sap = 0

while running:
    poq += 1
    if sap == 0:
        pygame.mixer.music.play(-1)
        sap = 1
    all_sprites.draw(screen)
    unit_sprites.draw(screen)
    if par == 0 and turn > 0:
        board.render()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and turn >= 0:
            if turn != 0:
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
                        if warrior_select_b.rect.collidepoint(event.pos):
                            unit = WarriorBlue((0, 0), screen)
                            unit.get_info()
                        elif warrior_select_r.rect.collidepoint(event.pos):
                            unit = WarriorRed((0, 0), screen)
                            unit.get_info()
                        elif archer_select_b.rect.collidepoint(event.pos):
                            unit = ArcherBlue((0, 0), screen)
                            unit.get_info()
                        elif archer_select_r.rect.collidepoint(event.pos):
                            unit = ArcherRed((0, 0), screen)
                            unit.get_info()
                        elif priest_select_b.rect.collidepoint(event.pos):
                            unit = PriestBlue((0, 0), screen)
                            unit.get_info()
                        elif priest_select_r.rect.collidepoint(event.pos):
                            unit = PriestRed((0, 0), screen)
                            unit.get_info()
                        elif miner_select_b.rect.collidepoint(event.pos):
                            unit = MinerBlue((0, 0), screen)
                            unit.get_info()
                        elif miner_select_r.rect.collidepoint(event.pos):
                            unit = MinerRed((0, 0), screen)
                            unit.get_info()
                        else:
                            print("empty cell")
            else:
                turn = 1
                click.play()
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
    if poq == 15:
        for i in map_units.keys():
            map_units[i].render()
            map_units[i].all_sprites.draw(screen)
        pygame.display.flip()
        poq = 0
    clock.tick(FPS)
