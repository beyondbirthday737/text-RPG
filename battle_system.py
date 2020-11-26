from game_rules_proxy import Game_rules_proxy


class Battle_system():
	"""sistema de batalha"""
	def __init__(self):
		self.grp = Game_rules_proxy()
		
		
	def battle(self, dice_player_value, dice_enemy_value, player_damange, enemy_damange):
		print(f"\n\n[x] Player life: {self.grp.get_life_player()}")
		print(f"[x] Enemy life: {self.grp.get_enemy_life()}")

		if(dice_player_value < dice_enemy_value):
			print("Voce atacou")
			self.grp.set_life_player((self.grp.get_life_player() - enemy_damange))

		if(dice_player_value > dice_enemy_value):
			self.grp.set_enemy_life(self.grp.get_enemy_life() - player_damange)
		
		if(self.grp.get_life_player() <= 0):
			print("Você perdeu!!!!")

		if(self.grp.get_enemy_life() <= 0):
			print("O inimigo morreu!!!")
			
