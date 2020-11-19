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

	def get_enemy_life(self):
		return self.enemy_life

	def set_enemy_life(self, new_value):
		self.enemy_life = new_value


class Game_rules_proxy(object):
	def __init__(self):
		self.game_rules = Game_rules()
	
	def get_life_player(self):
		return self.game_rules.get_life_player()
	
	def set_life_player(self, value):
		self.game_rules.set_life_player(value)

	def get_enemy_life(self):
		return self.game_rules.get_enemy_life()

	def set_enemy_life(self, value):
		self.game_rules.set_enemy_life(value)
		

class Battle_system():
	"""sistema de batalha"""
	def __init__(self):
		self.grp = Game_rules_proxy()
		
	def battle(self, dice_player_value, dice_enemy_value):
		if(dice_player_value < dice_enemy_value):
			self.grp.set_life_player((self.grp.get_life_player() - 4))

		if(dice_player_value > dice_enemy_value):
			self.grp.set_enemy_life(self.grp.get_enemy_life() - 4)
			print(f"vida atual -> {self.grp.get_enemy_life()}")
