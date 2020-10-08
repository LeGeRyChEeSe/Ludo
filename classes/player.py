from pygame import image
from pygame import transform, sprite


class Player(sprite.Sprite):
    red = 0
    blue = 0
    green = 0
    yellow = 0

    def __init__(self, game, color=None):
        super().__init__()
        self.game = game
        self.color = color
        self.image = image.load("assets/cheval.png")
        self.image = transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 290
        self.rect_decalage_x = 45
        self.rect_decalage_y = 45

    def get_position(self):
        if self.game.check_collision(self, self.game.plateau):
            print(self.rect)
