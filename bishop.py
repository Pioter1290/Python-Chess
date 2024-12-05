import pygame

class Bishop:
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

        # Ruchy w górę-lewo (lewa przekątna)
        for i in range(1, min(x, y) + 1):
            possible_moves.append((x - i, y - i))

        # Ruchy w górę-prawo (prawa przekątna)
        for i in range(1, min(8 - x, y) + 1):
            possible_moves.append((x + i, y - i))

        # Ruchy w dół-lewo (lewa przekątna)
        for i in range(1, min(x, 8 - y) + 1):
            possible_moves.append((x - i, y + i))

        # Ruchy w dół-prawo (prawa przekątna)
        for i in range(1, min(8 - x, 8 - y) + 1):
            possible_moves.append((x + i, y + i))

        return possible_moves
