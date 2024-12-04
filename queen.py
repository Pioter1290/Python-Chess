import pygame

class Queen:
    def __init__(self, color, position, image_path):
        self.color = color
        self.position = position
        self.image = pygame.image.load(image_path)


    def draw(self, screen):
        x, y = self.position
        screen.blit(self.image, (x * 80, y * 80))