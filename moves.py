from random import randint
from player import Player

class Move:
  def __init__(self, name, chance, getDamage, getSpeed):
    self.name = name
    self.chance = chance
    self.getDamage = getDamage
    self.getSpeed = getSpeed

  def miss(self, target, player):
    print(f'{player.name}\'s {self.name} missed!')
    pass

  def hit(self, target, player):
    dmg = self.getDamage()
    target.takeDamage(dmg)
    print(f"{player.name}'s {self.name} hits!")
    print(f"{target.name} took {dmg} damage! {target.health} HP remaining")

  def run(self, target, player):
    if randint(1, 100) / 100 <= self.chance:
      self.hit(target, player)
    else:
      self.miss(target, player)


class recoil(Move):
  def __init__(self, name, chance, getDamage, getSpeed):
    super(recoil, self).__init__(name, chance, getDamage(), getSpeed)
  
  def miss(self, target, player):
  # player.health = player.health * (2 / 3)
    player.damageTaken = 1.5
    print(f'{player.name}\'s {self.name} missed!')



class heal(Move):
  def __init__(self, chance, getDamage, getSpeed):
    super(heal, self).__init__('Heal', chance, getDamage(), getSpeed)
  def hit(self, player, target):
    target.takeDamage(self.getDamage() - (2 * self.getDamage()))
    print(f'{target.name} healed {self.getDamage()} HP! {target.health} HP remaining!')


class Ult(Move):
  def __init__(self, name, chance, getDamage, getSpeed):
    super(Ult, self).__init__(name, chance, getDamage(), getSpeed)
    Player.ultCharge = 0
  def hit(self, player, target):
    target.ultDamage(self.getDamage)


class Block(Move):
  def __init__(self, chance, getSpeed):
    super(Block, self).__init__('Block', chance, lambda: 0, getSpeed)
  
  def hit(self, target, player):
    Player.damageTaken = randint(3, 7) / 10
    print(f'{player.name} blocks!')


class mageShield(Move):
  def __init__(self, chance, getSpeed):
    super(mageShield, self).__init__('Shield', chance, lambda: 0, getSpeed)
  
  def hit(self, target, player):
    Player.damageTaken = randint(2, 4) / 10
    print(f'{player.name} casts Shield!')
