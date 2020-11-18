from rules import *

class Hero(Game_rules):
	"""Classe para padronizar o heroi
	   ele irá herdar atributos da classe Game_rules
	"""
	def __init__(self, name):
		super().__init__()
		self.name_hero = name

	def normal_attack(self):
		dice_value = self.roll_dice()
		if dice_value < 2:
			return [False, dice_value]


class Mage(Hero):
	"""Class de mago que irá herdar atributos da classe hero"""
	def __init__(self, name_hero):
		super().__init__(name_hero)

	def freeze_attack(self):
		dice_value = self.roll_dice()
		if dice_value < 3:
			return [False, dice_value]
		return [True, dice_value]

	def ultra_fire_boll(self):
		dice_value = self.roll_dice()
		if dice_value < 4:
			return [False, dice_value]
		return [True, dice_value]


class Warrior(Hero):
	"""Class de guerreiro que irá herdar atributos da classe hero"""
	def __init__(self, name_hero):
		super().__init__(name_hero)

	def heavy_attack(self):
		dice_value = self.roll_dice()
		if dice_value < 3:
			return [False, dice_value]
		return [True, dice_value]

	def brutal_attack(self):
		dice_value = self.roll_dice()
		if dice_value < 4:
			return [False, dice_value]
		return [True, dice_value]


class Paladin(Hero):
	"""Class de paladino que irá herdar atributos da classe hero"""
	def __init__(self, name_hero):
		super().__init__(name_hero)

	def spiritual_attack(self):
		dice_value = self.roll_dice()
		if dice_value < 3:
			return [False, dice_value]
		return [True, dice_value]

	def blast_attack(self):
		dice_value = self.roll_dice()
		if dice_value < 4:
			return [False, dice_value]
		return [True, dice_value]
