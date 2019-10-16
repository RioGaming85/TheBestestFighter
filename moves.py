from random import randint
from player import Player

class Move:
  def __init__(self, name, chance, getDamage, getSpeed):
    self.name = name
    self.chance = chance
    self.getDamage = getDamage
    self.getSpeed = getSpeed

  def miss(self, target, player):
    print(f'Player {player.name}\'s {self.name} missed!')
    pass

  def hit(self, target, player):
    target.takeDamage(self.getDamage())

  def run(self, target, player):
    if randint(1, 100) / 100 <= self.chance:
      self.hit(target, player)
    else:
      self.miss(target, player)


class Headbutt(Move):
  def __init__(self, chance, getDamage, getSpeed):
    super(Headbutt, self).__init__('headbutt', chance, getDamage, getSpeed)

  def miss(self, target, player):
  # player.health = player.health * (2 / 3)
    player.damageTaken = 1.5

class Ult(Move):
  def __init__(self, chance, getDamage, getSpeed):
    super(Ult, self).__init__(self, chance, getDamage, getSpeed)
    Player.ultCharge = 0

class Block(Move):
  def __init__(self, chance, getSpeed):
    super(Block, self).__init__('block', chance, lambda: 0, getSpeed)

  def hit(self, target, player):
    Player.damageTaken = randint(3, 7) / 10
