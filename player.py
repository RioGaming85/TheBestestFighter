from random import randint

def getMaxHealth():
  return randint(20, 30)

class Player:
  def __init__(self, name, moves):
    self.health = getMaxHealth()
    self.name = name
    self.moves = moves
    self.damageTaken = 1
    self.ultCharge = 0
    print(f"Player {self.name} HP {self.health}")

  def takeDamage(self, d):
    damage = d * self.damageTaken
    self.health -= damage
    self.damageTaken = 1
    self.ultCharge = min(1, self.ultCharge + (damage / 50))
    if self.health <= 0:
      self.health = 0
    print(f"Player {self.name}: Took {damage}, HP {self.health}")

  def log(self, text):
    print(f"Player {self.name}: {text}")

  def prompt(self):
    if self.health <= 0:
      self.health = 0
    print(f"Player {self.name}: HP {self.health}")
    for i, move in enumerate(self.moves):
      print(f"{i} {move.name}")
    selection = input('> ')
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
