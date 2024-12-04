import pygame

class Pawn:
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
        if self.color == "white":
            if y > 0:
                possible_moves.append((x, y - 1))
            if y == 6:
                possible_moves.append((x, y - 2))
        elif self.color == "black":
            if y < 7:
                possible_moves.append((x, y + 1))
            if y == 1:
                possible_moves.append((x, y + 2))
        return possible_moves



