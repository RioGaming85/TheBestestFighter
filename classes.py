from random import randint
from moves import Move, recoil, Block, heal

class Character:
	def __init__(self, moveList):
		moves = moveList
		self.useless = moves # this is useless, it exists purely to make linting be quiet


class Monk(Character):
	def __init__(self):
		self.name = 'Bard'
		punch = Move('Punch', 1.00, lambda: randint(3, 6), 3, '3 - 6')
		kick = Move('Kick', 0.70, lambda: randint(7, 9), 2, '7 - 9')
		headbutt = recoil('Headbutt', 0.25, lambda: randint(15, 20), 1, '15, 20')
		block = Block(1.00, 5, 'N/A')
		
		self.moves = [punch, kick, block, headbutt]
		self.HP = 40

class Bard(Character):
	def __init__(self):
		self.name = 'Bard'
		punch = Move('Punch', 1.00, lambda: randint(3, 6), 3, '3 - 6')
		rock = Move('Rock', 0.65, lambda: randint(8, 11), 2, '8 - 11')
		heavyMetal = recoil('Heavy Metal', 0.20, lambda: randint(18,22), 1, '18 - 22')
		block = Block(1, 5, 'N/A')
		
		self.moves = [punch, rock, block, heavyMetal]
		self.HP = 38

class Cleric(Character):
	def __init__(self):
		self.name = 'Cleric'
		punch = Move('Punch', 1.00, lambda: randint(3, 6), 3, '3 - 6')
		smite = Move('Smite', 0.70, lambda: randint(8, 10), 2, '8 - 10')
		healMove = heal(0.95,lambda: randint(5, 8), 4, '5 - 8')
		block = Block(1.00, 5, 'N/A')
		
		self.moves = [punch, smite, healMove, block]
		self.HP = 40

class Mage(Character):
	def __init__(self):
		from moves import mageShield
		self.name = 'Mage'
		punch = Move('Punch', 1.00, lambda: randint(3, 6), 3, '3 - 6')
		fireball = Move('Fireball', 0.85, lambda: randint(5, 8), 2, '5 - 8')
		lightningSpray = Move('Lightning Spray', 0.25, lambda: randint(11, 14), 1, '11 - 14')
		shield = mageShield(1.00, 5, 'N/A')
		
		self.moves = [punch, fireball, shield, lightningSpray]
		self.HP = 43

class Goose(Character):
	def __init__(self):
		self.name = 'Goose'
		honk = Move('HONK', 0.5, lambda: randint(255, 255), 4, '255')

		self.moves = [honk, honk, honk, honk]
		self.HP = 7

class Ranger(Character):
	def __init__(self):
		self.name = 'Ranger'
		punch = Move('Punch', 1.00, lambda: randint(3, 6), 3, '3 - 6')
		arrow = Move('Arrow', 0.80, lambda: randint(4, 12), 2, '4 - 12')
		block = Block(1, 5, 'N/A')
		boomArrow = recoil('Explosive Arrow', 0.20, lambda: randint(16, 24), 1, '16 - 24')

		self.moves = [punch, arrow, block, boomArrow]
		self.HP = 39

class BS_Admin(Character):
	def __init__(self):
		self.name('F*** off, I win.')
		punch = Move('Punch', 1.00, lambda: randint(3, 6), 3, '3 - 6')
		hammer = Move('HAMMER OF GOD', 1.00, lambda: randint(20, 24), 2, '20 - 24')
		block = Block(1, 5, 'N/A')
		forceWin = Move('Win.exe', 1.00, lambda: randint(9999, 9999), 6, '9999')

		self.moves = [punch, hammer, block, forceWin]
		self.HP = 9999
