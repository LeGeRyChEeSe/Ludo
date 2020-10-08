from pygame import image, transform, display
from random import randint

global image_choice

class Dice:

    def __init__(self, game):
        self.game = game
        self.images = {1: image.load("assets/1_dice.png"),
                       2: image.load("assets/2_dice.png"),
                       3: image.load("assets/3_dice.png"),
                       4: image.load("assets/4_dice.png"),
                       5: image.load("assets/5_dice.png"),
                       6: image.load("assets/6_dice.png")
                       }
        self.image = None
        self.rect = None

    def dice(self):
        if self.game.is_dice_pressed:
            for i in range(0, 100):
                image_choice = randint(1, 6)
                self.image = self.images.get(image_choice)
                self.image = transform.scale(self.image, [200, 200])
                self.rect = self.image.get_rect()
                self.rect.center = (self.game.screen.get_height() /
                                    2, self.game.screen.get_width() / 2)
                self.game.screen.blit(self.image, self.rect)
                display.flip()
            print(image_choice)
            return image_choice
        else:
            image_choice = randint(1, 6)
            self.image = self.images.get(image_choice)
            self.image = transform.scale(self.image, [200, 200])
            self.rect = self.image.get_rect()
            self.rect.center = (self.game.screen.get_height() /
                                2, self.game.screen.get_width() / 2)
            self.game.screen.blit(self.image, self.rect)
            print(image_choice)
            return image_choice
