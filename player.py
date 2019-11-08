from math import ceil, floor

class Player:
  def __init__(self, name, classType):
    self.health = int(classType.HP)
    self.name = name
    self.classType = classType
    self.moves = classType.moves
    self.damageTaken = 1
    self.ultCharge = 0
    print(f"{self.name} HP {self.health}")

  def takeDamage(self, d):
    damage = d * self.damageTaken
    damage = ceil(damage)
    self.health -= damage
    self.damageTaken = 1
    self.ultCharge += floor(self.ultCharge + (damage / 1.5))
    if self.health <= 0:
      self.health = 0

  def log(self, text):
    print(f"{self.name}: {text}")

  def prompt(self):
    print('\n')
    if self.health <= 0:
      self.health = 0
    print(f"{self.name}: HP {self.health}\n-------------------------------------------")
    for i in range(0, len(self.classType.moves)):
      print(f"{i} {self.classType.moves[i].name}")
    selection = input(f"-------------------------------------------\n{self.name} move choice:\n > ")
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
