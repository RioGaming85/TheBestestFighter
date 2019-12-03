from math import ceil, floor

def displayMoves(moves):
	spacing = ['              ','            ','            ','           ','          ','         ','        ','       ','      ','     ','    ','	  ','  ',' ','']
	chanceSpace = ['   ',' ','']
	print('  | Move Name	    | Chance | Damage')
	print('-------------------------------------------')
	for i in range(0, len(moves)-1): print(f'{i} | {moves[i].name}{spacing[len(moves[i].name)-1]} |  {int(moves[i].chance*100)}%{chanceSpace[len(str(int(moves[i].chance*100)))-1]}  | {moves[i].dmgRange}')
	print('-------------------------------------------')
	return input(' > ').upper()

def displayMenu(array):
	print('-------------------------------------------')
	for i in range(len(array)):
		print(f'{i} {array[i]}')
	print('-------------------------------------------')
	return input(' > ').upper()

class Player:
	def __init__(self, name, classType):
		self.health = int(classType.HP)
		self.name = name
		self.classType = classType
		self.moves = classType.moves
		self.damageTaken = 1
		self.ultCharge = 0
		print(f"{self.name}: HP = {self.health}, Class = {self.classType.name}")

	def takeDamage(self, d):
		damTak = int(self.damageTaken)
		damage = d * damTak
		damage = ceil(damage)
		self.health -= damage
		self.damageTaken = 1
		self.ultCharge += floor(self.ultCharge + (damage / 1.5))
		if self.ultCharge >= 30:
			self.ultCharge = 30
		if self.health <= 0:
			self.health = 0
	
	def ultDamage(self, d):
		damTak = int(self.damageTaken)
		damage = d * damTak
		damage = ceil(damage)
		self.health -= damage
		self.damageTaken = 1
		if self.health <= 0:
			self.health = 0

	def doHeal(self):
		healAmnt = self.damageTaken
		healAmnt = ceil(healAmnt)
		self.health += healAmnt
		if self.health > self.classType.HP:
			self.health = self.classType.HP

	def log(self, text):
		print(f"{self.name}: {text}")

	def prompt(self):
		print('\n')
		if self.health <= 0:
			self.health = 0
		print(f"{self.name}'s Turn:\nHP: {self.health}, Ult Charge: {floor((self.ultCharge / 30) * 100)}%")
		selection = displayMoves(self.classType.moves)
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
