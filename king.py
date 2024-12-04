import pygame

class King:
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
        # ruchy poziome i pionowe
        if y > 0:
            possible_moves.append((x, y - 1))
        if y < 7:
            possible_moves.append((x, y + 1))
        if x > 0:
            possible_moves.append((x - 1, y))
        if x < 7:
            possible_moves.append((x + 1, y))

        # ruchy na przekątne
        if x > 0 and y > 0:
            possible_moves.append((x - 1, y - 1))
        if x < 7 and y > 0:
            possible_moves.append((x + 1, y - 1))
        if x > 0 and y < 7:
            possible_moves.append((x - 1, y + 1))
        if x < 7 and y < 7:
            possible_moves.append((x + 1, y + 1))

        return possible_moves
