import random

class Game_rules(object):
	"""Aqui fica toda as regras do jogo"""
	def __init__(self):
		self.__hero_life = 10
		self.__enemy_life = 10

	def roll_dice(self):
		return random.randint(1,6)

	def get_life_player(self):
		return self.__hero_life

	def set_life_player(self, new_value):
		self.__hero_life = new_value

	def get_enemy_life(self):
		return self.__enemy_life

	def set_enemy_life(self, new_value):
		self.__enemy_life = new_value
