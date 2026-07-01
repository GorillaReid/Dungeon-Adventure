import random       #imports for different libarys
import time
import sys
from colorama import Fore, Back , Style, init
import readchar
import menus

while 1:
    menus.clear()
    print(Fore.GREEN + "Press the corresponding button for what you would like to do:" + Fore.LIGHTBLUE_EX + "\nL: Enter a Dungeon\nK: Open your inventory\nJ: Open the Shop\nI: Info about the game\nQ: quit the game")
    menu = readchar.readkey().lower()
    time.sleep(1)
    if menu == "k":
        menus.inventory()
    if menu == "l":
        menus.move()         
    if menu == "j":
        menus.shop()
    if menu == "i":
        menus.info()
    if menu == "q":
        sys.exit()