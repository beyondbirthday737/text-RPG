from rules import *
import sys


class Hero(Game_rules):
	"""Classe para padronizar o heroi
	   ele irá herdar atributos da classe Game_rules
	"""
	def __init__(self, name):
		super().__init__()
		self.name_hero = name

	def __del__(self):
		print("GAME OVER!!!")

	def normal_attack(self):
		dice_value = self.roll_dice()
		if dice_value < 2:
			print("Você errou o atack")
			return dice_value
		return dice_value


class Mage(Hero):
	"""Class de mago que irá herdar atributos da classe hero"""
	def __init__(self, name_hero):
		super().__init__(name_hero)

	def heavy_attack(self):
		dice_value = self.roll_dice()
		if dice_value < 3:
			print("Você errou o atack")
			return dice_value
		return dice_value

	def super_attack(self):
		dice_value = self.roll_dice()
		if dice_value < 4:
			print("Você errou o atack")
			return dice_value
		return dice_value


class Warrior(Hero):
	"""Class de guerreiro que irá herdar atributos da classe hero"""
	def __init__(self, name_hero):
		super().__init__(name_hero)

	def heavy_attack(self):
		dice_value = self.roll_dice()
		if dice_value < 3:
			print("Você errou o atack")
			return dice_value
		return dice_value

	def super_attack(self):
		dice_value = self.roll_dice()
		if dice_value < 4:
			print("Você errou o atack")
			return dice_value
		return dice_value


class Paladin(Hero):
	"""Class de paladino que irá herdar atributos da classe hero"""
	def __init__(self, name_hero):
		super().__init__(name_hero)

	def heavy_attack(self):
		dice_value = self.roll_dice()
		if dice_value < 3:
			print("Você errou o atack")
			return dice_value
		return dice_value

	def heavy_attack(self):
		dice_value = self.roll_dice()
		if dice_value < 4:
			print("Você errou o atack")
			return dice_value
		return dice_value
