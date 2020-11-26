from rules import *


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
		