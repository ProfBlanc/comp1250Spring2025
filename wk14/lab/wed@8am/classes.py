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