from random import randint
from moves import Move, recoil, Block, heal

class Character:
  def __init__(self, moveList):
    moves = moveList
    self.useless = moves # this is useless, it exists purely to make linting be quiet


class Monk(Character):
  def __init__(self):
    self.name = 'Bard'
    punch = Move('Punch', 1, lambda: randint(3, 6), 3)
    kick = Move('Kick', 0.70, lambda: randint(7, 9), 2)
    headbutt = recoil('Headbutt', 0.25, lambda: randint(15, 20), 1)
    block = Block(1, 5)
    
    self.moves = [punch, kick, block, headbutt]
    self.HP = 40

class Bard(Character):
  def __init__(self):
    self.name = 'Bard'
    punch = Move('Punch', 1, lambda: randint(3, 6), 3)
    rock = Move('Rock', 0.65, lambda: randint(8, 11), 2)
    heavyMetal = recoil('Heavy Metal', 0.2, lambda: randint(18,22), 1)
    block = Block(1, 5)
    
    self.moves = [punch, rock, block, heavyMetal]
    self.HP = 38

class Cleric(Character):
  def __init__(self):
    self.name = 'Cleric'
    punch = Move('Punch', 1, lambda: randint(3, 6), 3)
    smite = Move('Smite', 0.7, lambda: randint(8, 10), 2)
    healMove = heal(0.95,lambda:  randint(5, 8), 4)
    block = Block(1,5)
    self.moves = [punch, smite, healMove, block]
    self.HP = 40

class Mage(Character):
  def __init__(self):
    from moves import mageShield
    self.name = 'Mage'
    punch = Move('Punch', 1, lambda: randint(3, 6), 3)
    fireball = Move('Fireball', 0.85, lambda: randint(5, 8), 2)
    lightningSpray = Move('Lightning Spray', 0.25, lambda: randint(11, 14), 1)
    shield = mageShield(1, 5)
    
    self.moves = [punch, fireball, shield, lightningSpray]
    self.HP = 43

class Goose(Character):
  def __init__(self):
    self.name = 'Goose'
    honk = Move('HONK', 0.5, lambda: randint(255, 255), 4)
    block = Block(1, 5)

    self.moves = [honk, honk, block, honk]
    self.HP = 1
