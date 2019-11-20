from random import randint

class Move:
	def __init__(self, name, chance, getDamage, getSpeed, dmgRange):
		self.name = name
		self.chance = chance
		self.getDamage = getDamage
		self.getSpeed = getSpeed
		self.dmgRange = dmgRange

	def miss(self, target, player):
		print(f'{player.name}\'s {self.name} missed!')
		pass

	def hit(self, target, player):
		try:
			self.dmg = self.getDamage()
		except:
			self.dmg = self.getDamage
		target.takeDamage(self.dmg)
		print(f"{player.name}'s {self.name} hits!")
		print(f"{target.name} took {self.dmg} damage! {target.health} HP remaining")

	def run(self, target, player):
		if randint(1, 100) / 100 <= self.chance:
			self.hit(target, player)
		else:
			self.miss(target, player)


class recoil(Move):
	def __init__(self, name, chance, getDamage, getSpeed, dmgRange):
		super(recoil, self).__init__(name, chance, getDamage(), getSpeed, dmgRange)
	
	def miss(self, target, player):
	# player.health = player.health * (2 / 3)
		player.damageTaken = 1.5
		print(f'{player.name}\'s {self.name} missed!')



class heal(Move):
	def __init__(self, chance, getDamage, getSpeed, dmgRange):
		super(heal, self).__init__('Heal', chance, getDamage(), getSpeed, dmgRange)
	def hit(self, player, target):
		dmg = self.getDamage
		target.doHeal(dmg)
		print(f'{target.name} heals!')
		print(f'{target.name} healed {dmg} HP! {target.health} HP remaining!')
	def miss(self, target, player):
		print(f'{player.name}\'s heal failed!')


class Ult(Move):
	def __init__(self, name, chance, getDamage, getSpeed, dmgRange):
		super(Ult, self).__init__(name, chance, getDamage(), getSpeed, dmgRange)
	def hit(self, target, player):
		dmg = self.getDamage
		target.ultDamage(dmg)
		player.ultCharge = 0
		print(f'{player.name} uses their Ultimate!')
		print(f'{target.name} took {dmg} damage! {target.health} HP remaining!')


class Block(Move):
	def __init__(self, chance, getSpeed, dmgRange):
		super(Block, self).__init__('Block', chance, lambda: 0, getSpeed, 'N/A')
	
	def hit(self, target, player):
		player.damageTaken = randint(3, 7) / 10
		print(f'{player.name} blocks!')


class mageShield(Move):
	def __init__(self, chance, getSpeed, dmgRange):
		super(mageShield, self).__init__('Shield', chance, lambda: 0, getSpeed, 'N/A')
	
	def hit(self, target, player):
		player.damageTaken = randint(2, 4) / 10
		print(f'{player.name} casts Shield!')
