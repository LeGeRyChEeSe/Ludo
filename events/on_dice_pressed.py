

class OnDicePressed:

    def __init__(self, dice):
        self.dice = dice

    def dice_pressed(self):
        dice = self.dice.dice()
        print(dice)
        if dice == 6:
            self.dice.game.add_horse("red")
        print(self.dice.game.all_players)
