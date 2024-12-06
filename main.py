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
icon = pygame.image.load('main/images/black_king.png')
pygame.display.set_icon(icon)
block_size = 80
selected_square = None
selected_piece = None
possible_moves = []

white = (255, 255, 255)
black = (0, 0, 0)
light_brown = (240, 217, 181)
dark_brown = (181, 136, 99)
green = (60, 165, 60)

pieces = []

for col in range(8):
    pieces.append(Pawn("white", (col, 6), 'main/images/white_pawn.png'))

for col in range(8):
    pieces.append(Pawn("black", (col, 1), 'main/images/black_pawn.png'))

pieces.append(Queen("black", (3, 0), 'main/images/black_queen.png'))
pieces.append(Queen("white", (3, 7), 'main/images/white_queen.png'))
pieces.append(King("white", (4, 7), 'main/images/white_king.png'))
pieces.append(King("black", (4, 0), 'main/images/black_king.png'))
pieces.append(Rook("black", (0, 0), 'main/images/black_rook.png'))
pieces.append(Rook("black", (7, 0), 'main/images/black_rook.png'))
pieces.append(Rook("white", (0, 7), 'main/images/white_rook.png'))
pieces.append(Rook("white", (7, 7), 'main/images/white_rook.png'))
pieces.append(Knight("white", (1, 7), 'main/images/white_knight.png'))
pieces.append(Knight("white", (6, 7), 'main/images/white_knight.png'))
pieces.append(Knight("black", (1, 0), 'main/images/black_knight.png'))
pieces.append(Knight("black", (6, 0), 'main/images/black_knight.png'))
pieces.append(Bishop("black", (5, 0), 'main/images/black_bishop.png'))
pieces.append(Bishop("black", (2, 0), 'main/images/black_bishop.png'))
pieces.append(Bishop("white", (5, 7), 'main/images/white_bishop.png'))
pieces.append(Bishop("white", (2, 7), 'main/images/white_bishop.png'))

# śledzenie czyj jest ruch:
current_turn = "white"

def draw_board():
    for row in range(8):
        for col in range(8):
            color = white if (row + col) % 2 == 0 else green
            pygame.draw.rect(screen, color, pygame.Rect(col * block_size, row * block_size, block_size, block_size))

    if selected_square:
        row, col = selected_square
        pygame.draw.rect(screen, black, pygame.Rect(col * block_size, row * block_size, block_size, block_size), 2)

    for piece in pieces:
        piece.draw(screen)

    for move in possible_moves:
        x, y = move
        pygame.draw.circle(screen, (0, 0, 0), (x * block_size + block_size // 2, y * block_size + block_size // 2), 8)

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
            if selected_piece is None:
                selected_square = None
                for piece in pieces:
                    if piece.position == (col, row) and piece.color == current_turn:
                        selected_square = (row, col)
                        selected_piece = piece
                        possible_moves = piece.get_possible_moves(pieces)
                        break
            else:
                if (col, row) in possible_moves:
                    selected_piece.position = (col, row)
                    if current_turn == "white":
                        current_turn = "black"
                    elif current_turn == "black":
                        current_turn = "white"
                selected_piece = None
                selected_square = None
                possible_moves = []

    draw_board()
    pygame.display.flip()

pygame.quit()
