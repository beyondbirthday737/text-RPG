import random

class Game_rules(object):
	"""Aqui fica toda as regras do jogo"""
	def __init__(self):
		self.hero_life = 10
		self.enemy_life = 10

	def roll_dice(self):
		return random.randint(1,6)


class Hero(Game_rules):
	"""Classe para padronizar o heroi
	   ele irá herdar atributos da classe Game_rules
	"""
	def __init__(self, name):
		super().__init__()
		self.name_hero = name

	def normal_attack(self):
		if self.roll_dice() < 2:
			return False
		return True


class Mage(Hero):
	"""Class de mago que irá herdar atributos da classe hero"""
	def __init__(self, name_hero):
		super().__init__(name_hero)

	def freeze_attack(self):
		if self.roll_dice() < 3:
			return False
		return True

	def ultra_fire_boll(self):
		if self.roll_dice() < 4:
			return False
		return True


class Warrior(Hero):
	"""Class de guerreiro que irá herdar atributos da classe hero"""
	def __init__(self, name_hero):
		super().__init__(name_hero)

	def heavy_attack(self):
		if self.roll_dice() < 3:
			return False
		return True

	def brutal_attack(self):
		if self.roll_dice() < 4:
			return False
		return True


class Paladin(Hero):
	"""Class de paladino que irá herdar atributos da classe hero"""
	def __init__(self, name_hero):
		super().__init__(name_hero)

	def spiritual_attack(self):
		if self.roll_dice() < 3:
			return False
		return True

	def blast_attack(self):
		if self.roll_dice() < 4:
			return False
		return True


def init_game():
	print(""" ███▄ ▄███▓▓██   ██▓▄▄▄█████▓ ██░ ██     ▄▄▄      ▓█████▄  ██▒   █▓▓█████  ███▄    █ ▄▄▄█████▓ █    ██  ██▀███  ▓█████ 
▓██▒▀█▀ ██▒ ▒██  ██▒▓  ██▒ ▓▒▓██░ ██▒   ▒████▄    ▒██▀ ██▌▓██░   █▒▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒ ██  ▓██▒▓██ ▒ ██▒▓█   ▀ 
▓██    ▓██░  ▒██ ██░▒ ▓██░ ▒░▒██▀▀██░   ▒██  ▀█▄  ░██   █▌ ▓██  █▒░▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░▓██  ▒██░▓██ ░▄█ ▒▒███   
▒██    ▒██   ░ ▐██▓░░ ▓██▓ ░ ░▓█ ░██    ░██▄▄▄▄██ ░▓█▄   ▌  ▒██ █░░▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▓▓█  ░██░▒██▀▀█▄  ▒▓█  ▄ 
▒██▒   ░██▒  ░ ██▒▓░  ▒██▒ ░ ░▓█▒░██▓    ▓█   ▓██▒░▒████▓    ▒▀█░  ░▒████▒▒██░   ▓██░  ▒██▒ ░ ▒▒█████▓ ░██▓ ▒██▒░▒████▒
░ ▒░   ░  ░   ██▒▒▒   ▒ ░░    ▒ ░░▒░▒    ▒▒   ▓▒█░ ▒▒▓  ▒    ░ ▐░  ░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░░ ▒░ ░
░  ░      ░ ▓██ ░▒░     ░     ▒ ░▒░ ░     ▒   ▒▒ ░ ░ ▒  ▒    ░ ░░   ░ ░  ░░ ░░   ░ ▒░    ░    ░░▒░ ░ ░   ░▒ ░ ▒░ ░ ░  ░
░      ░    ▒ ▒ ░░    ░       ░  ░░ ░     ░   ▒    ░ ░  ░      ░░     ░      ░   ░ ░   ░       ░░░ ░ ░   ░░   ░    ░   
       ░    ░ ░               ░  ░  ░         ░  ░   ░          ░     ░  ░         ░             ░        ░        ░  ░
            ░ ░                                    ░           ░                                                       """)

	name_hero = input("[!] Digite o nome do heroi: ")

	print("\n")
	print("[!] Escolha sua classe")
	print("[+] (M)age")
	print("[+] (W)arrior")
	print("[+] (P)aladin\n")

	print("""         />_________________________________
[########[]_________________________________>
         \>
""")

	option = input("[!] Digite a inicial da classe: ")

	if option == "M" or option == "m":
		mage = Mage(name_hero)

	if option == "W" or option == "w":
		warrior = Warrior(name_hero)	

	if option == "P" or option == "p":
		paladin = Paladin(name_hero)
		

init_game()