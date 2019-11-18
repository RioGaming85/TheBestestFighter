from math import ceil, floor

def displayMenu(array):
  print('-------------------------------------------')
  try:
    for i in range(len(array)):
      print(f'{i} {array[i].name}')
  except:
    for i in range(len(array)):
      print(f'{i} {array[i]}')
  print('-------------------------------------------')
  return input(' > ').upper()

class Player:
  def __init__(self, name, classType):
    print(classType)
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
    print(f"{self.name}'s Turn:\nHP: {self.health}, Ult Charge: {floor((self.ultCharge / 15) * 100)}%")
    selection = displayMenu(self.classType.moves)
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
