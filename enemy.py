from rules import *


class Enemy(Game_rules):
	"""Classe para padronizar os inimigos
	   ele irá herdar atributos da classe Game_rules
	"""
	def __init__(self):
		pass
		

	def normal_attack(self):
		dice_value = self.roll_dice()
		if dice_value < 2:
			return [False, dice_value]


class Chimera(Enemy):
    def __init__():
        self.enemy_life = 15

    def beast_attack():
        dice_value = self.roll_dice()
		if dice_value < 3:
			return [False, dice_value]
		return [True, dice_value]
    
    def puff_of_fire():
        dice_value = self.roll_dice()
		if dice_value < 4:
			return [False, dice_value]
		return [True, dice_value]


class Troll(Enemy):
    def __init__():
        self.enemy_life = 7

    def violent_attack():
        dice_value = self.roll_dice()
		if dice_value < 3:
			return [False, dice_value]
		return [True, dice_value]
    
    def flay_live():
        dice_value = self.roll_dice()
		if dice_value < 4:
			return [False, dice_value]
		return [True, dice_value]


class Basilisk(Enemy):
     def __init__():
        self.enemy_life = 10

    def violent_attack():
        dice_value = self.roll_dice()
		if dice_value < 3:
			return [False, dice_value]
		return [True, dice_value]
    
    def flay_live():
        dice_value = self.roll_dice()
		if dice_value < 4:
			return [False, dice_value]
		return [True, dice_value]

