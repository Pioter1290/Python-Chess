# main.py
import pygame
from pawn import Pawn

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

# Load and scale the king image
white_king = pygame.image.load('main/images/white_king.png')
white_king = pygame.transform.scale(white_king, (block_size, block_size))

pawns = []

# Białe pionki
for col in range(8):
    pawns.append(Pawn("white", (col, 6), 'main/images/white_pawn.png'))

# Czarne pionki
for col in range(8):
    pawns.append(Pawn("black", (col, 1), 'main/images/black_pawn.png'))

def draw_board():
    for row in range(8):
        for col in range(8):
            color = light_brown if (row + col) % 2 == 0 else dark_brown
            pygame.draw.rect(screen, color, pygame.Rect(col * block_size, row * block_size, block_size, block_size))

    if selected_square is not None:
        row1, col1 = selected_square
        pygame.draw.rect(screen, black, pygame.Rect(col1 * block_size, row1 * block_size, block_size, block_size), 1)

    for pawn in pawns:
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
