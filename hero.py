import pygame

class Hero:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y

    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (210, 250, 251),
                         pygame.Rect(self.x, self.y, 8, 5))