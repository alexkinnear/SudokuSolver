import pygame

pygame.init()
pygame.font.init()

font = pygame.font.SysFont(pygame.font.get_default_font(), 50)

DIS_WIDTH = 9 * 50
DIS_HEIGHT = 9 * 50
dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption("Sudoku Solver")
dis.fill((255, 255, 255))

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def draw_board():
    # num = font.render(str(9), False, (0, 0, 0))
    # dis.blit(num, (15, 10))
    for i in range(9):
        thickness = 1
        if i % 3 == 0 and i != 0:
            thickness = 4
        pygame.draw.line(dis, (0, 0, 0), (0, i*50), (DIS_WIDTH, i*50), thickness)
        pygame.draw.line(dis, (0, 0, 0), (i*50, 0), (i*50, DIS_HEIGHT), thickness)

    for i in range(0, 9):
        for j in range(0, 9):
            if not board[i][j] == 0:
                num = font.render(str(board[i][j]), False, (0, 0, 0))
                dis.blit(num, (15 + (50*j), 10 + (50*i)))
    pygame.display.update()

draw_board()
running = True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False


pygame.quit()
quit()
