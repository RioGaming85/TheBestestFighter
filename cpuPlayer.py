from math import ceil, floor
from random import choice
class cpuPlayer:
  def __init__(self, name, classType):
    self.health = int(classType.HP)
    self.name = name
    self.classType = classType
    self.moves = classType.moves
    self.damageTaken = 1
    self.ultCharge = 0
    print(f"{self.name}: HP = {self.health}, Class = {self.classType.name}")

  def takeDamage(self, d):
    damage = d * self.damageTaken
    damage = ceil(damage)
    self.health -= damage
    self.damageTaken = 1
    self.ultCharge += floor(self.ultCharge + (damage / 1.5))
    if self.ultCharge >= 15:
      self.ultCharge = 15
    if self.health <= 0:
      self.health = 0
  
  def ultDamage(self, d):
    damage = d * self.damageTaken
    damage = ceil(damage)
    self.health -= damage
    self.damageTaken = 1
    if self.health <= 0:
      self.health = 0

  def log(self, text):
    print(f"{self.name}: {text}")

  def prompt(self):
    print('\n')
    if self.health <= 0:
      self.health = 0
    if self.ultCharge == 15:
      selection = '4' # If ult available, use ult
    elif self.health <= (0.75 * self.classType.HP):
      selection = choice(['0','1']) # punch or kick/fireball/rock/smite
    elif self.health <= (0.5 * self.classType.HP):
      selection = choice(['0','1','2']) # same as above but can also block/heal
    elif self.health <= (0.1 * self.classType.HP):
      selection = choice(['2','3']) # in a pinch, block/heal or 'All-or-Nothing'
    else:
      selection = '0' # if no other case applies, punch
    
    mid = 0
    try:
      mid = int(selection)
    except:
      print('Invalid move!')
      return self.prompt()
    if mid >= len(self.moves) or mid < 0:
      print('Invalid move!')
      return self.prompt()
    return self.moves[mid]