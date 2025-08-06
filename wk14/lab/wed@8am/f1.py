from classes import Dice, Player, DiceGame

# game = Dice(6, 12)
# print(game.roll())

p1 = Player("Ben", 6, 32)
p2 = Player("Friend", 6, 32)
game = DiceGame(p1, p2)
game.play()