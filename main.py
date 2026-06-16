import random       #imports for different libarys
import time
import threading
import sys
from colorama import Fore, Back , Style, init
import readchar
import menus

while 1:
    menus.clear()
    print(Fore.BLUE + "Press the corresponding button to what you want to do:" + Fore.LIGHTBLUE_EX + "\nL: Enter a Dungeon\nI: Open your inventory\nJ: Open the Shop\nQ: quit the game")
    menu = readchar.readkey().lower()
    time.sleep(1)
    if menu == "i":
        menus.inventory()
    if menu == "l":
        threading.Thread(target=menus.move).start()
        threading.Thread(target=menus.enemy_move).start()

        while True:
            time.sleep(0.8)
            if menus.player_y == menus.height - 1:
                break            
    if menu == "j":
        menus.shop()
    if menu == "q":
        sys.exit()