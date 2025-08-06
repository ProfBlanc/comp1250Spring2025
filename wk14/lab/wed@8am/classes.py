import random


class Dice:
    def __init__(self, num_sides_die_1, num_sides_die_2):
        self.num_sides_die_1 = num_sides_die_1
        self.num_sides_die_2 = num_sides_die_2

    @property
    def num_sides_die_1(self):
        return self.__num_sides_die_1

    @num_sides_die_1.setter
    def num_sides_die_1(self, value):
        if isinstance(value, int) and value in [6, 12, 32, 120]:
            self.__num_sides_die_1 = value
        else:
            raise ValueError("Invalid number of side value")

    @property
    def num_sides_die_2(self):
        return self.__num_sides_die_2
    @num_sides_die_2.setter
    def num_sides_die_2(self, value):
        if isinstance(value, int) and value in [6, 12, 32, 120]:
            self.__num_sides_die_2 = value
        else: raise ValueError("Invalid number of side value")

    def __str__(self): return f"Dice has sides of {self.__num_sides_die_1} " \
                              f"and {self.__num_sides_die_2}"
    def roll(self, number_of_dices=2):
        if isinstance(number_of_dices, int) and number_of_dices in [1,2]:
            roll_1 = random.randint(1, self.__num_sides_die_1)
            roll_2 = None
            if number_of_dices == 2:
                roll_2 = random.randint(1, self.__num_sides_die_2)
            return [roll_1, roll_2] if roll_2 is not None else [roll_1]
        else: return ValueError("Can only roll 1 or 2 dices")

class Player:
    def __init__(self, name, dice_1_num_sides, dice_2_num_sides):
        self.name = name
        self.dice = Dice(dice_1_num_sides, dice_2_num_sides)
    @property
    def name(self): return self.__name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self.__name = value
        else: raise ValueError("Invalid Player Name")
    def __str__(self): return f"Player {self.__name} is rolling with {self.dice}"


class DiceGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def __validate(self):
        return self.__player1.dice.num_sides_die_1 == self.player2.dice.num_sides_die_1 \
            and self.__player1.dice.num_sides_die_2 == self.player2.dice.num_sides_die_2
    @property
    def player1(self): return self.__player1
    @player1.setter
    def player1(self, value):
        if not isinstance(value, Player):
            raise ValueError("Please pass a player object")
        self.__player1 = value
    @property
    def player2(self): return self.__player2
    @player2.setter
    def player2(self, value):
        if not isinstance(value, Player):
            raise ValueError("Please pass a player object")
        self.__player2 = value
    def play(self):
        if not self.__validate(): raise ValueError("Both players are not playing with the same dice")

        p1_total = p2_total = 0
        for i in range(1, 4):
            p1_roll = self.player1.dice.roll()
            p2_roll = self.player2.dice.roll()

            p1_total += sum(p1_roll)
            p2_total += sum(p2_roll)
            print(f"Player1: {self.player1.name} rolled: {p1_roll}. Player 1 has a total roll of {p1_total}")
            print(f"Player2: {self.player2.name} rolled: {p2_roll}. Player 1 has a total roll of {p2_total}")

        if p1_total == p2_total:
            print("The game resulted in a draw")
        else:
            print(self.player1.name if p1_total > p2_total else self.player2.name + " has won" )