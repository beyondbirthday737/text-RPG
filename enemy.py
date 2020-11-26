from rules import *


class Enemy(Game_rules):
	"""Classe para padronizar os inimigos
	   ele irá herdar atributos da classe Game_rules
	"""
	def __init__(self):
		super().__init__()

	def normal_attack(self):
		dice_value = self.roll_dice()
		if dice_value < 2:
			return dice_value
		return dice_value


class Chimera(Enemy):
    def __init__(self):
        super().__init__()
        self.__enemy_life = 15


    def __del__(self):
        print("A Chimera morreu!!!")


    def get_life(self):
        return self.__enemy_life


    def heavy_attack(self):
        dice_value = self.roll_dice()
        if dice_value < 3:
	        return dice_value
        return dice_value
    

    def super_attack(self):
        dice_value = self.roll_dice()
        if dice_value < 4:
           return dice_value
        return dice_value


class Minotaur(Enemy):
    def __init__(self):
        super().__init__()
        self.__enemy_life = 7

    def __del__(self):
        print("O minotaur morreu")


    def get_life(self):
        return self.__enemy_life


    def heavy_attack(self):
        dice_value = self.roll_dice()
        if dice_value < 3:
            return dice_value
        return dice_value


    def super_attack(self):
        dice_value = self.roll_dice()
        if dice_value < 4:
            return dice_value
        return dice_value


class Basilisk(Enemy):
    def __init__(self):
        super().__init__()
        self.__enemy_life = 10


    def __del__(self):
        print("O Basislisk morreu!!!")


    def get_life(self):
        return self.__enemy_life


    def heavy_attack(self):
        dice_value = self.roll_dice()
        if dice_value < 3:
           return dice_value
        return dice_value


    def super_attack(self):
        dice_value = self.roll_dice()
        if dice_value < 4:
            return dice_value
        return dice_value

