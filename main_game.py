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
                self.enemy = Minotaur()
                print('\n')
                self.writer_effect("Você consegue encontrar uma porta .Ao abrir a porta você encontra uma criatura horrenda, com chifres e 2 metros de altura.")
                print("\nPreparese para lutar")
                print(enemys_arts[1])
                self.figthing()
                self.writer_effect("Após uma batalha intensa você consegue derrotar o minotaur")
                self.writer_effect(f"\n{self.name_hero}: Arg. Estou tonto...\n{self.name_hero}: Tenho que sair daqui de alguma maneira.\n")
                self.writer_effect(f"\nVocê desmaia")
                break
            
            elif action == 2:
                print("\n")
                self.writer_effect("Você grita e nada acontece.")
             
            else: 
                print("[!] OPÇÃO INVALIDA!")
        
        return self
    

    def fase2(self):
        self.writer_effect(f"\n Que lugar é esse ?")
        self.writer_effect(f"\n{self.name_hero}: Como eu vim parar aqui? ")
        self.writer_effect("\nVoçê acorda em um deserto")

        while True:
            print("[!] Escolha uma ação")
            print("[+] 1-Observar ao redor")
            print("[+] 2-Andar")
            
            option = int(input("ação --> "))

            if(option == 1):
               self.writer_effect("Você começa a observar.\nVocê encontra um grande numero ossada de espalhadas pelo deserto")
            
            elif(option == 2):
                print("")
            
            else:
                print("[!] OPÇÃO INVALIDA!")

        return self
            