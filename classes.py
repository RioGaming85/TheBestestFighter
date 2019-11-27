from random import randint
from moves import *


global punch
global block
global baseUlt

punch = Move('Punch', 1.00, lambda: randint(3, 6), 3, '3 - 6')
block = Block(1.00, 5, 'N/A')
baseUlt = Ult('Ultimate', 1, lambda: randint(18, 26), 6, '18 - 26')

class Character:
	def __init__(self, moveList, name, ult):
		self.moves = moveList
		self.name = name
		self.ult = ult


class Monk(Character):
	def __init__(self):
		self.name = 'Bard'

		kick = Move('Kick', 0.70, lambda: randint(7, 9), 2, '7 - 9')
		headbutt = recoil('Headbutt', 0.25, lambda: randint(15, 20), 1, '15, 20')
		ult = Ult('Ki Strike (Ult)', 1, lambda: randint(25, 30), 6, '25 - 30')
		
		self.moves = [punch, kick, block, headbutt]
		self.ult = ult
		self.HP = 40

class Barbarian(Character):
	def __init__(self):
		self.name = 'Barbarian'

		rage = recoil('Rage Punch', 0.80, lambda: randint(9, 12), 2, '9 - 12')
		axeWhirl = recoil('Axe Whirl', 0.25, lambda: randint(20, 24), 1, '20 - 24')
		holderheck = Ult('HOLDERHECC (Ult)', 1, lambda: randint(30, 33), 6, '30 - 33')

		self.moves = [punch, rage, block, axeWhirl]
		self.ult = holderheck
		self.HP = 50

class Bard(Character):
	def __init__(self):
		self.name = 'Bard'

		rock = Move('Rock', 0.65, lambda: randint(8, 11), 2, '8 - 11')
		heavyMetal = recoil('Heavy Metal', 0.20, lambda: randint(18,22), 1, '18 - 22')
		ult = Ult('Wonderwall', 1, lambda: randint(28, 32), 6, '28 - 32')
		
		self.moves = [punch, rock, block, heavyMetal]
		self.ult = ult
		self.HP = 38

class Cleric(Character):
	def __init__(self):
		self.name = 'Cleric'

		smite = Move('Smite', 0.70, lambda: randint(8, 10), 2, '8 - 10')
		healMove = heal(0.95,lambda: randint(5, 8), 4, '5 - 8')
		ult = Ult('God Blow', 1, lambda: randint(23, 25), 6, '23 - 25')
		
		self.moves = [punch, smite, healMove, block]
		self.ult = ult
		self.HP = 40

class Mage(Character):
	def __init__(self):
		self.name = 'Wizard'

		fireball = Move('Fireball', 0.85, lambda: randint(5, 8), 2, '5 - 8')
		lightningSpray = Move('Lightning Spray', 0.25, lambda: randint(11, 14), 1, '11 - 14')
		shield = mageShield(1.00, 5, 'N/A')
		ult = ('Meteor Swarm', 1, lambda: randint(25, 35), 6, '25 - 35')

		self.moves = [punch, fireball, shield, lightningSpray]
		self.ult = ult
		self.HP = 43

class Goose(Character):
	def __init__(self):
		self.name = 'Goose'
		
		honk = Move('HONK', 0.5, lambda: randint(255, 255), 4, '255')
		ult = Ult('NOOT NOOT', 1, lambda: randint(511, 511), 6, '511')

		self.moves = [honk, honk, honk, honk]
		self.ult = ult
		self.HP = 7

class Ranger(Character):
	def __init__(self):
		self.name = 'Ranger'

		arrow = Move('Arrow', 0.80, lambda: randint(4, 12), 2, '4 - 12')
		boomArrow = recoil('Explosive Arrow', 0.20, lambda: randint(16, 24), 1, '16 - 24')
		ult = Ult('Dragon Strike', 1, lambda: randint(22, 35), 6, '22 - 35')

		self.moves = [punch, arrow, block, boomArrow]
		self.ult = ult
		self.HP = 39

class BS_Admin(Character):
	def __init__(self):
		self.name('F*** off, I win.')

		hammer = Move('HAMMER OF GOD', 1.00, lambda: randint(30, 34), 2, '20 - 24')
		forceWin = Move('Power Abuse', 1.00, lambda: randint(9999, 9999), 6, '9999')
		ult = Ult('ForceWin.exe', 1.00, lambda: randint(99999, 99999), 6, '99999')

		self.moves = [punch, hammer, block, forceWin]
		self. ult = ult
		self.HP = 9999
