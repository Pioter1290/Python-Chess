import pygame


class Knight:
    def __init__(self, color, position, image_path):
        self.color = color
        self.position = position
        self.image = pygame.image.load(image_path)

    def draw(self, screen):
        x, y = self.position
        screen.blit(self.image, (x * 80, y * 80))

    def get_possible_moves(self):
        possible_moves = []
        x, y = self.position

        # Dodajemy wszystkie możliwe ruchy skoczka
        if 0 <= x + 1 < 8 and 0 <= y - 2 < 8:
            possible_moves.append((x + 1, y - 2))
        if 0 <= x + 2 < 8 and 0 <= y - 1 < 8:
            possible_moves.append((x + 2, y - 1))
        if 0 <= x + 2 < 8 and 0 <= y + 1 < 8:
            possible_moves.append((x + 2, y + 1))
        if 0 <= x + 1 < 8 and 0 <= y + 2 < 8:
            possible_moves.append((x + 1, y + 2))
        if 0 <= x - 1 < 8 and 0 <= y + 2 < 8:
            possible_moves.append((x - 1, y + 2))
        if 0 <= x - 2 < 8 and 0 <= y + 1 < 8:
            possible_moves.append((x - 2, y + 1))
        if 0 <= x - 2 < 8 and 0 <= y - 1 < 8:
            possible_moves.append((x - 2, y - 1))
        if 0 <= x - 1 < 8 and 0 <= y - 2 < 8:
            possible_moves.append((x - 1, y - 2))

        return possible_moves
