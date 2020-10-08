from pygame import Color, sprite, draw
from pygame import Surface


class Case(sprite.Sprite):

    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.image = Surface([40, 40])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def add_case(self):
        self.game.plateau.add(self)
