import random


class Dice:
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides
    @property
    def number_of_sides(self):
        return self.__number_of_sides
    @number_of_sides.setter
    def number_of_sides(self, value):
        if isinstance(value, int) and value in [6, 12, 4, 10, 12, 20]:
            self.__number_of_sides = value
        else:
            raise ValueError(f"'{value}' is not a valid")
    def roll_dice(self):
        return random.randint(1, self.__number_of_sides)


# dice = Dice(6)
# for i in range(5):
#     print(dice.roll_dice())

"""
Create a class named Player
    name: string
    dice: Dice
    tostring: name is playing with a X-sided dice
Create a class called DiceGame
    2 Players
    play:
        each player will roll the dice 5 times.
        at the end, either 1 player will win or game will result in draw 

"""
class Player:
    def __init__(self, name, number_of_sides):
        self.name = name
        self.dice = Dice(number_of_sides)
    @property
    def name(self): return self.__name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self.__name = value
        else:
            raise ValueError(f"{value} is not valid")
    def __str__(self): return f"{self.__name} is playing with a {self.dice.number_of_sides}-sided dice"

class DiceGame:
    def __init__(self, player1_name, player1_dice_sides, player2_name, player2_dice_sides):
        self.player1 = Player(player1_name, player1_dice_sides)
        self.player2 = Player(player2_name, player2_dice_sides)
    def play(self):
        if self.player1.dice.number_of_sides != self.player2.dice.number_of_sides:
            raise ValueError("Hey! No cheating allowed! Both players must play with same dice values")

        player1_roll, player1_total, player2_roll, player2_total = 0,0,0,0
        for _ in range(5):
            player1_roll = self.player1.dice.roll_dice()
            player2_roll = self.player2.dice.roll_dice()

            player1_total += player1_roll
            player2_total += player2_roll

            print(f"Player 1 roll: {player1_roll}. Player 1 total: {player1_total}")
            print(f"Player 2 roll: {player2_roll}. Player 2 total: {player2_total}")

        if player1_total == player2_total:
            print("Draw!")
        else: print("Player", 1 if player1_roll > player2_roll else 2, "won")


game = DiceGame("John", 6, "Mary", 6)
game.play()