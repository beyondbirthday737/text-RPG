from rules import *
from classes import *


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

''''
def batalha():
	mage = Mage("jss")
	battle = Battle_system()

	atack = mage.freeze_attack()

	for i in range(1,10):
		battle.battle(6, 2)


batalha()
''''
