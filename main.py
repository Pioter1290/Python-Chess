import pygame
from pawn import Pawn
from queen import Queen
from king import King
from rook import Rook
from knight import Knight
from bishop import Bishop

pygame.init()

size = (640, 640)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chess")
block_size = 80
selected_square = None

white = (255, 255, 255)
black = (0, 0, 0)
light_brown = (240, 217, 181)
dark_brown = (181, 136, 99)




pieces = []

for col in range(8):
    pieces.append(Pawn("white", (col, 6), 'main/images/white_pawn.png'))

for col in range(8):
    pieces.append(Pawn("black", (col, 1), 'main/images/black_pawn.png'))

pieces.append(Queen("balck", (3,0),'main/images/black_queen.png'))
pieces.append(Queen("white", (4,7),'main/images/white_queen.png'))
pieces.append(King("white", (3,7),'main/images/white_king.png'))
pieces.append(King("black", (4,0),'main/images/black_king.png'))
pieces.append(Rook("black", (0,0),'main/images/black_rook.png'))
pieces.append(Rook("black", (7,0),'main/images/black_rook.png'))
pieces.append(Rook("white", (0,7),'main/images/white_rook.png'))
pieces.append(Rook("white", (7,7),'main/images/white_rook.png'))
pieces.append(Knight("white", (1,7),'main/images/white_knight.png'))
pieces.append(Knight("white", (6,7),'main/images/white_knight.png'))
pieces.append(Knight("black", (1,0),'main/images/black_knight.png'))
pieces.append(Knight("black", (6,0),'main/images/black_knight.png'))
pieces.append(Bishop("black", (5,0),'main/images/black_bishop.png'))
pieces.append(Bishop("black", (2,0),'main/images/black_bishop.png'))
pieces.append(Bishop("white", (5,7),'main/images/white_bishop.png'))
pieces.append(Bishop("white", (2,7),'main/images/white_bishop.png'))
def draw_board():
    for row in range(8):
        for col in range(8):
            color = light_brown if (row + col) % 2 == 0 else dark_brown
            pygame.draw.rect(screen, color, pygame.Rect(col * block_size, row * block_size, block_size, block_size))

    if selected_square is not None:
        row1, col1 = selected_square
        pygame.draw.rect(screen, black, pygame.Rect(col1 * block_size, row1 * block_size, block_size, block_size), 2)

    for pawn in pieces:
        pawn.draw(screen)

def get_square(pos):
    x, y = pos
    col = x // block_size
    row = y // block_size
    return row, col

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row, col = get_square(pos)
            selected_square = row, col

    draw_board()
    pygame.display.flip()

pygame.quit()
