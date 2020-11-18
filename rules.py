import random

class Game_rules(object):
	"""Aqui fica toda as regras do jogo"""
	def __init__(self):
		self.hero_life = 10
		self.enemy_life = 10

	def roll_dice(self):
		return random.randint(1,6)

	def get_life_player(self):
		return self.hero_life

	def set_life_player(self, new_value):
		self.hero_life = new_value

	def get_enemy_life(self, new_value):
		return self.enemy_life

	def set_enemy_life(self, new_value):
		self.enemy_life = new_value



class Battle_system(Game_rules):
	"""sistema de batalha"""
	def __init__(self):
		super().__init__()
		
	def battle(self, dice_player_value, dice_enemy_value):
		if(dice_player_value < dice_enemy_value):
			self.set_life_player((self.get_life_player() - 4))

		if(dice_player_value > dice_enemy_value):
			self.set_enemy_life(self.get_enemy_life() - 4)
