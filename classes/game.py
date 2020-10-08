from pygame import display, sprite

from classes.bot import Bot
from classes.case import Case
from classes.dice import Dice
from classes.player import Player


class Game(sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.is_playing = False
        self.is_dice_pressed = False
        self.screen_height = 700
        self.screen_width = 700
        self.screen = display.set_mode((self.screen_height, self.screen_width))
        self.player = Player(self)
        self.all_players = sprite.Group()
        self.bot = Bot(self)
        self.plateau = sprite.Group()
        self.min = 20
        self.max = 651
        self.middle_up = 290
        self.middle_down = 425
        self.step = 45
        self.dice = Dice(self)

    def start(self):
        self.all_players.empty()
        self.plateau.empty()
        self.set_plateau()

    def set_plateau(self):
        for x in range(self.min, self.max, self.step):
            for y in range(self.min, self.max, self.step):
                if not ((x in range(self.min, self.middle_up, self.step)) or (
                        x in range(self.middle_down, self.max, self.step))) and (
                        (y in range(self.min, self.middle_up, self.step)) or (
                        y in range(self.middle_down, self.max, self.step))) or (
                        x in range(self.min, self.max, self.step)) and (
                        y in range(self.middle_up, self.middle_down, self.step)):
                    case = Case(self, x, y)
                    case.add_case()

    def update(self):
        self.dice.dice()

    def add_horse(self, color="red", max=4):
        print(self.player[color])
        self.all_players.add(Player(self, color))

    def check_collision(self, sprite_player, group):
        return sprite.spritecollideany(sprite_player, group, sprite.collide_mask)
