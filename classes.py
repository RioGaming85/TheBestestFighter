from random import randint
from moves import Move

class Character:
  def __init__(self, moveList):
    moves = moveList # Linting shows that this is unused, but it is, so DON'T remove it


class Brawler(Character):
  def __init__(self):
    from moves import recoil, Block
    punch = Move('Punch', 1, lambda: randint(3, 6), 3)
    kick = Move('Kick', 0.70, lambda: randint(7, 9), 2)
    headbutt = recoil('Headbutt', 0.25, randint(15, 20), 1)
    block = Block(1, 5)
    
    self.moves = [punch, kick, block, headbutt]
    self.HP = 40

class Bard(Character):
  def __init__(self):
    from moves import Block, recoil
    punch = Move('Punch', 1, lambda: randint(3, 6), 3)
    song = Move('Rock', 0.65, lambda: randint(8, 11), 1)
    heavyMetal = recoil('Heavy Metal', 0.2, randint(18,22), 1)
    block = Block(1, 5)
    
    self.moves = [punch, song, block, heavyMetal]
    self.HP = 38

class Cleric(Character):
  def __init__(self):
    from moves import heal, Block
    punch = Move('Punch', 1, lambda: randint(3, 6), 3)
    smite = Move('Smite', 0.7, lambda: randint(8, 10), 2)
    heal = heal(0.95, randint(5, 8), 4)
    block = Block(1,5)
    self.moves = [punch, smite, block, heal]
    self.HP = 40

class Mage(Character):
  def __init__(self):
    from moves import mageShield
    punch = Move('Punch', 1, lambda: randint(3, 6), 3)
    fireball = Move('Fireball', 0.85, lambda: randint(5, 8), 2)
    lightningSpray = Move('Lightning Spray', 0.275, lambda: randint(11, 14), 1)
    shield = mageShield(1, 5)
    
    self.moves = [punch, fireball, shield, lightningSpray]
    self.HP = 43
    