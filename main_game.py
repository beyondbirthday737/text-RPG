import time
import sys
from random import randrange
from battle_system import *
from classes import *
from enemy import *
from artes import enemys_arts


class Main_game:
    def __init__(self, name, classe):
        self.name_hero = name
        self.battle_sys = Battle_system()

        if classe == 'm' or classe == 'M':
            self.player = Mage(self.name_hero)

        elif classe == 'w' or classe == 'W':
            self.player = Warrior(self.name_hero)
            
        elif classe == 'p' or classe == 'P':
            self.player = Paladin(self.name_hero)
        
        
    def writer_effect(self, string):
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            seconds = "0." + str(randrange(1, 4, 1))
            seconds = float(seconds)
            time.sleep(seconds)


    def figthing(self):
        while True:
            print("\n[!] Escolha o Ataque")
            print("[+] 1-Ataque normal")
            print("[+] 2-Ataque forte")
            print("[+] 3-Super Ataque")

            option = int(input("Digite o ataque: "))

            if(option == 1):
                player_dice = self.player.normal_attack()
                enemy_dice = self.enemy.normal_attack()
                self.battle_sys.battle(player_dice, enemy_dice, 2, 2)
                
            elif(option == 2):
                player_dice = self.player.heavy_attack()
                enemy_dice = self.enemy.heavy_attack()
                self.battle_sys.battle(player_dice, enemy_dice, 4, 4)

            elif(option == 3):
                play_dice = self.player.super_attack()
                enemy_dice = self.enemy.super_attack()
                self.battle_sys.battle(player_dice, enemy_dice, 6, 6)
            

            if(self.battle_sys.grp.get_enemy_life() <= 0):
                del self.enemy
                break
            
            elif(self.battle_sys.grp.get_life_player() <= 0):
                del self.player
                sys.exit()
                break


    def fase1(self):
        self.enemy = Minotaur()
        self.battle_sys.grp.set_enemy_life(self.enemy.get_life())

        text = f"""{self.name_hero}: ...
Você acorda em lugar escuro.
{self.name_hero}: arggh. Onde estou?"""

        self.writer_effect(text)

        while True:
            print("\n\n[!] Escolha uma ação")
            print("[+] 1-Procurar por algo")
            print("[+] 2-Gritar")

            action = int(input("ação --> "))

            if action == 1:
                print('\n')
                self.writer_effect("Você consegue encontrar uma porta .Ao abrir a porta você encontra uma criatura horrenda, com chifres e 2 metros de altura.")

                print(enemys_arts[1])
                print("\nPreparese para lutar")
                self.figthing()

                self.writer_effect("Após uma batalha intensa você consegue derrotar o minotaur")
                self.writer_effect(f"\n{self.name_hero}: Arg. Estou tonto...\n{self.name_hero}: Tenho que sair daqui de alguma maneira.\n")
                self.writer_effect(f"\nVocê desmaia")
                break
            
            elif action == 2:
                print("\n")
                self.writer_effect("\nVocê grita e nada acontece.")
             
            else: 
                print("[!] OPÇÃO INVALIDA!")
        
        return self
    

    def fase2(self):
        self.enemy = Basilisk()
        self.battle_sys.grp.set_enemy_life(self.enemy.get_life())
        self.battle_sys.grp.set_life_player(10)

        self.writer_effect(f"\n\n\n{self.name_hero}: Que lugar é esse ?")
        self.writer_effect(f"\n{self.name_hero}: Como eu vim parar aqui? ")
        self.writer_effect("\nVoçê acorda em um deserto")

        while True:
            print("\n\n[!] Escolha uma ação")
            print("[+] 1-Observar ao redor")
            print("[+] 2-Andar")
            
            option = int(input("ação --> "))

            if(option == 1):
                self.writer_effect("\n\nVocê começa a observar.\nVocê encontra um grande numero ossada de espalhadas pelo deserto")
                self.writer_effect(f"\n{self.name_hero}: Parece que teve uma grande batalha por aqui...")

            elif(option == 2):
                self.writer_effect("\n\nApós um bom tempo de caminhada. Você sente um leve tremor no chão")
                self.writer_effect(f"\n{self.name_hero}: Oque foi isso?\n{self.name_hero}: Tem algo grande passando por aqui")
                self.writer_effect("\n\nO tremor começa a ficar cada fez mais intenso")
                self.writer_effect("\nUma serpente extremamente grande e faminta começa a sair de dentro da areia")

                print("\nPreparese para lutar")
                print(enemys_arts[2])

                self.figthing()
                
                self.writer_effect("\n\nVocê consegue subir na cabeça da serpente e corta-la. Fazendo a serpente se desaparecer por completo")
                self.writer_effect("\n\nDerrepente você começa a ser sugado pela areia")
                self.writer_effect(f"\n\n{self.name_hero}: ohh não... Não consigo me mecher")
                self.writer_effect("\n\nVocê é sugado pela areia...")
                break
            
            else:
                print("[!] OPÇÃO INVALIDA!")

        return self
    

    def fase3(self):
        self.enemy = Chimera()
        self.battle_sys.grp.set_enemy_life(self.enemy.get_life())
        self.battle_sys.grp.set_life_player(10)
        
        self.writer_effect(f"\n\n{self.name_hero}: hmpf...")
        self.writer_effect("\n\nApós ser engolida pela a areia do deserto voçe acorda em uma ruina")
        self.writer_effect("\nE uma voz rouca ecoa pelo lugar")
        
        self.writer_effect("\n\nChimera: haahaah Vejo que você chegou até aqui...")
        self.writer_effect("\nChimera: Você sair daqui sem me derrotar.")
        self.writer_effect("\nChimera: O pesadelo é eterno...")
        
        self.writer_effect(f"\n\n{self.name_hero}: Apareça!!!")
        self.writer_effect(f"\n{self.name_hero}: Onde está você!!!!")

        self.writer_effect(f"\nChimera: hahahahah O Seu desejo é uma ordem!!!")

        self.writer_effect("\nUma chimera aparece na sua frente.")
        print(enemys_arts[0])

        self.figthing()

        self.writer_effect("\n\nDepois de uma longa e exaustiva batalha você consegue destruir a chimera com um golpe em seu coração")
        self.writer_effect(f"\n\n{self.name_hero}: humpf... humpf...")
        
        self.writer_effect("\n\nTodo o pesadelo começa a ser destruido...")
        self.writer_effect(f"\n\n{self.name_hero}: humm!!!")
        self.writer_effect(f"\n\nVocê acorda do pesadelo")

        print(
'''  ██████  █    ██  ██▀███   ██▒   █▓ ██▓ ██▒   █▓▓█████ ▓█████▄ 
▒██    ▒  ██  ▓██▒▓██ ▒ ██▒▓██░   █▒▓██▒▓██░   █▒▓█   ▀ ▒██▀ ██▌
░ ▓██▄   ▓██  ▒██░▓██ ░▄█ ▒ ▓██  █▒░▒██▒ ▓██  █▒░▒███   ░██   █▌
  ▒   ██▒▓▓█  ░██░▒██▀▀█▄    ▒██ █░░░██░  ▒██ █░░▒▓█  ▄ ░▓█▄   ▌
▒██████▒▒▒▒█████▓ ░██▓ ▒██▒   ▒▀█░  ░██░   ▒▀█░  ░▒████▒░▒████▓ 
▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░   ░ ▐░  ░▓     ░ ▐░  ░░ ▒░ ░ ▒▒▓  ▒ 
░ ░▒  ░ ░░░▒░ ░ ░   ░▒ ░ ▒░   ░ ░░   ▒ ░   ░ ░░   ░ ░  ░ ░ ▒  ▒ 
░  ░  ░   ░░░ ░ ░   ░░   ░      ░░   ▒ ░     ░░     ░    ░ ░  ░ 
      ░     ░        ░           ░   ░        ░     ░  ░   ░ ''')
   
        return self
