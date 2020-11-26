from game_rules_proxy import Game_rules_proxy
from battle_system import Battle_system
from classes import *
from main_game import *


def init_game():
	print('''  ██████  █    ██  ██▀███   ██▒   █▓ ██▓ ██▒   █▓▓█████    ▄▄▄█████▓ ██░ ██ ▓█████     ███▄    █  ██▓ ▄████  ██░ ██ ▄▄▄█████▓ ███▄ ▄███▓ ▄▄▄       ██▀███  ▓█████ 
▒██    ▒  ██  ▓██▒▓██ ▒ ██▒▓██░   █▒▓██▒▓██░   █▒▓█   ▀    ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀     ██ ▀█   █ ▓██▒██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒▓██▒▀█▀ ██▒▒████▄    ▓██ ▒ ██▒▓█   ▀ 
░ ▓██▄   ▓██  ▒██░▓██ ░▄█ ▒ ▓██  █▒░▒██▒ ▓██  █▒░▒███      ▒ ▓██░ ▒░▒██▀▀██░▒███      ▓██  ▀█ ██▒▒██▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░▓██    ▓██░▒██  ▀█▄  ▓██ ░▄█ ▒▒███   
  ▒   ██▒▓▓█  ░██░▒██▀▀█▄    ▒██ █░░░██░  ▒██ █░░▒▓█  ▄    ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▓██▒  ▐▌██▒░██░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░ ▒██    ▒██ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄ 
▒██████▒▒▒▒█████▓ ░██▓ ▒██▒   ▒▀█░  ░██░   ▒▀█░  ░▒████▒     ▒██▒ ░ ░▓█▒░██▓░▒████▒   ▒██░   ▓██░░██░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░ ▒██▒   ░██▒ ▓█   ▓██▒░██▓ ▒██▒░▒████▒
▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░   ░ ▐░  ░▓     ░ ▐░  ░░ ▒░ ░     ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░ ▒░   ▒ ▒ ░▓  ░▒   ▒  ▒ ░░▒░▒  ▒ ░░   ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░
░ ░▒  ░ ░░░▒░ ░ ░   ░▒ ░ ▒░   ░ ░░   ▒ ░   ░ ░░   ░ ░  ░       ░     ▒ ░▒░ ░ ░ ░  ░   ░ ░░   ░ ▒░ ▒ ░ ░   ░  ▒ ░▒░ ░    ░    ░  ░      ░  ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░
░  ░  ░   ░░░ ░ ░   ░░   ░      ░░   ▒ ░     ░░     ░        ░       ░  ░░ ░   ░         ░   ░ ░  ▒ ░ ░   ░  ░  ░░ ░  ░      ░      ░     ░   ▒     ░░   ░    ░   
      ░     ░        ░           ░   ░        ░     ░  ░             ░  ░  ░   ░  ░            ░  ░       ░  ░  ░  ░                ░         ░  ░   ░        ░  ░
                                ░            ░                                                                                                                    ''')

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

	if(option == 'm' or option == 'M' or option == 'w' or option == 'W' or option == 'p' or option == 'P'):
		game = Main_game(name_hero, option)
		game.fase1().fase2()
		
	else:
		print("[!] OPÇÃO INVALIDA!")


init_game()

'''
def batalha():
	mage = Mage("jss")
	battle = Battle_system()

	atack = mage.freeze_attack()

	for i in range(1,10):
		battle.battle(6, 2)


batalha()
'''