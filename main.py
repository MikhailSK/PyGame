from Board import *
from unit import *


board = Board(BOARD_W, BOARD_H, screen)
screen.fill((0, 0, 0))

running = True
par_space = 0
FPS = 20
par = 0
turn = 1
clock = pygame.time.Clock()


while running:
    if par == 0:
        board.render()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            new_board_pos = ((event.pos[0] - 10) // 30, (event.pos[1] - 10) // 30)
            if event.button == 1:
                board.get_click(event.pos, turn)
                if board.turn != turn:
                    print(turn)
                    turn = board.turn
                    par = 1
            elif event.button == 3:
                try:
                    map_units[new_board_pos].get_info()
                except KeyError:
                    print("empty cell")
    pygame.display.flip()
    clock.tick(FPS)
