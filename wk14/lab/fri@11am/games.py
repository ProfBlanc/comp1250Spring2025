"""
create rock paper,scissors game.

    options: rock, paper, scissors
    method: choice:
                randomly choose one of the options
Player:
    name
Game:
    accept 2 players, 1 rock paper scissor arg
    method: play: determine who wins
"""
import random


class RockPaperScissors:
    def __init__(self):
        self.__options = ('rock', 'paper', 'scissors')

    def choose(self):
        return random.choice(self.__options)
    def manual_choose(self, option):
        if option not in self.__options:
            raise ValueError(option + ' is not a valid option')
        return option
    def which_option_wins(self, option1, option2):
        """
        Given two options, determine which option wins.
        Return a boolean value indicated if option1 BEATS option2
        """
        if option1 not in self.__options or option2 not in self.__options:
            raise ValueError('Not valid options')

        if option1 == option2:
            return "draw"

        if option1 == self.__options[0]:
            return option2 != self.__options[1]
        elif option1 == self.__options[1]:
            return option2 != self.__options[2]
        elif option1 == self.__options[2]:
            return option2 != self.__options[0]

rps = RockPaperScissors()

for _ in range(10):
    print(rps.choose())


print(""" 
hi
    there
""")