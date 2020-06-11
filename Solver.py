import pygame

pygame.init()
pygame.font.init()

font = pygame.font.SysFont(pygame.font.get_default_font(), 50)

# 9 rows/cols of 50 pixels
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
    for i in range(9):
        thickness = 1
        if i % 3 == 0 and i != 0:
            thickness = 4
        pygame.draw.line(dis, (0, 0, 0), (0, i * 50), (DIS_WIDTH, i * 50), thickness)
        pygame.draw.line(dis, (0, 0, 0), (i * 50, 0), (i * 50, DIS_HEIGHT), thickness)

    for i in range(0, 9):
        for j in range(0, 9):
            if not board[i][j] == 0:
                num = font.render(str(board[i][j]), False, (0, 0, 0))
                dis.blit(num, (15 + (50 * j), 10 + (50 * i)))
    pygame.display.update()


def place_num(x, y):
    if event.key == pygame.K_BACKSPACE:
        board[int(x / 50)][int(y / 50)] = 0
    if event.key == pygame.K_1:
        board[int(x / 50)][int(y / 50)] = 1
    if event.key == pygame.K_2:
        board[int(x / 50)][int(y / 50)] = 2
    if event.key == pygame.K_3:
        board[int(x / 50)][int(y / 50)] = 3
    if event.key == pygame.K_4:
        board[int(x / 50)][int(y / 50)] = 4
    if event.key == pygame.K_5:
        board[int(x / 50)][int(y / 50)] = 5
    if event.key == pygame.K_6:
        board[int(x / 50)][int(y / 50)] = 6
    if event.key == pygame.K_7:
        board[int(x / 50)][int(y / 50)] = 7
    if event.key == pygame.K_8:
        board[int(x / 50)][int(y / 50)] = 8
    if event.key == pygame.K_9:
        board[int(x / 50)][int(y / 50)] = 9
    if event.key == pygame.K_SPACE:
        solve()
    draw_board()
    pygame.display.update()


def find_empty():
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None


def is_valid(row, col, num):
    for i in range(9):
        # check row
        if board[row][i] == num:
            return False

        # check col
        if board[i][col] == num:
            return False

    # check 3x3 square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if board[i][j] == num:
                return False
    return True


def solve():
    if find_empty() is None:
        return True
    row, col = find_empty()
    for i in range(1, 10):
        if is_valid(row, col, i):
            board[row][col] = i
            draw_board()
            pygame.event.pump()
            if solve():
                return True
            board[row][col] = 0
    return False


class Box:
    def __init__(self):
        self.box_X = 0
        self.box_Y = 0
        self.box = (0, 0, 0, 0)

    def select_box(self):
        dis.fill((255, 255, 255))
        draw_board()
        pos = pygame.mouse.get_pos()
        self.box_X = pos[0]
        self.box_Y = pos[1]
        while not self.box_X % 50 == 0:
            self.box_X -= 1
        while not self.box_Y % 50 == 0:
            self.box_Y -= 1
        self.box = (self.box_X, self.box_Y, 50, 50)
        pygame.draw.rect(dis, (30, 180, 40), (self.box_X, self.box_Y, 50, 50), 3)


draw_board()
running = True
Box = Box()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Box.select_box()
        if event.type == pygame.KEYDOWN:
            place_num(Box.box_Y, Box.box_X)
    pygame.draw.rect(dis, (30, 180, 40), Box.box, 3)
    Box.select_box()
    pygame.display.update()
pygame.quit()
quit()
