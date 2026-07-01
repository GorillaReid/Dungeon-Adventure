import random       #used to pick random numbers or words
import readchar     #used to help the player move around the map better
import sys          #used to help with some debugging and exiting the game upon some errors
import time         #used for pausing the program for a certain amount of time
import os           #used to clear the screen
from colorama import Fore, Back, Style, init        #used for color

init(autoreset=True)    #makes sure the colors reset after that print statement

#some of the variables used in the program  #v#
grid = []                                   #|#     the map
enemies = []                                #|#     the enemy locations
life = 5                                    #|#     the players amount of lives
gold = 0                                    #|#     the players amount of gold
height = 30                                 #|#     the maps height
width = 30                                  #|#     the maps width
level = 1                                   #|#     the dungeon level the player is on
size = 6                                    #|#     the size the rooms are that generate in the dungeon
key = 0                                     #|#     the amount of keys the player has
player_x = 0                                #|#     the players x coord (left, right)
player_y = 0                                #^#     the players y coord (up, down)
#------------------------------------------------------------------------------------------------------------------------------------
def move():     #the move function
    global gold, life, level, height, player_y, player_x, enemies, key       #initiates these variables as global so the values are kept between functions

    player_x = generate_map()       #generates the map
    player_y = 0                    #sets the players y coord to 0 which is the top of the map
    grid[player_y][player_x] = "*"  #places the player character at their designated x and y coords
    display_map()                   #displayes the map

    while player_y != height - 1:   #runs this loop until the player reachs the bottom of the map
        move = readchar.readkey().lower()       #takes the players input
        grid[player_y][player_x] = " "          #replaces the players old location with air so that their isnt multiple player icons

        if move == "s" and player_y + 1 < height and grid[player_y + 1][player_x] != "#":   #if the players pushs s it moves them down 1
            player_y += 1
        if move == "w" and grid[player_y - 1][player_x] != "#":     #if the player pushes w it moves them up 1
            player_y -= 1 
        if move == "d" and grid[player_y][player_x + 1] != "#" and player_x + 1 < width - 1:        #if the player pushes d it moves them right 1
            player_x += 1
        if move == "a" and grid[player_y][player_x - 1] != "#" and player_x - 1 > 0:        #if the player pushs a it moves them left 1
            player_x -= 1

        if grid[player_y][player_x] == "%":     #if the players goes over a piece of gold it gives them + 1-3 gold
            value = random.randint(1, 3)
            gold += value
        if grid[player_y][player_x] == "$":     #if the player goes over a key it gives them + 1 key
            key += 1
        grid[player_y][player_x] = "*"      #places the player icon in their new position
        if player_y == height - 1:      #checks if the player is at the bottom of the map, if they are it prints a statement letting them know they reached the end and then adds 1 to their level count
            print(Fore.GREEN + f"You made it through Level {level}!")
            display_map()
            time.sleep(1)       #waits 1 second
            level += 1
        enemy_move()        #lets the enemies move
        if life <= 0:       #if the player has 0 health it prints Game Over and ends the program
            display_map()
            print(Fore.RED + "Game Over! You lost all your life\n")
            sys.exit()

        display_map()       #displays the map
#------------------------------------------------------------------------------------------------------------------------------------
def generate_map():     #the map generation function
    global grid, size, enemies
    enemies = []        #declares the enemy string as empty
    grid = []           #declares the grid string as empty
    for y in range(height):     #makes the map all # (which are walls) dependent on the height and width of the map
        row = ["#"] * width
        grid.append(row)

    start_x = random.randint(2, width - 3)      #picks a random starting location for the player on their x coord

    player_x = start_x      #sets their starting x coord to the randomly picked number
    player_y = 0        #sets their y coord to 0

    while player_y < height - 1:    #runs until the players y coord is at the bottom of the map

        grid[player_y][player_x] = " "      #sets their current position to air
        direction = random.choices(["down","left","right","up"], weights=[15, 40, 40, 5])[0]        #picks a random direction (up, down, left, right)

        if direction == "down":     #if its down moves the player down 1
            player_y += 1
        elif direction == "left" and player_x > 1 and player_y > 1:     #if its left moves the player left 1
            player_x -= 1
        elif direction == "right" and player_x < width - 2 and player_y > 1:        #if its right moves the player right 1
            player_x += 1
        elif direction == "up" and player_y > 1:        #if its up moves the player up 1
            player_y -= 1
    grid[height -1][player_x] = " "     #sets the starting location to air

    amount = random.randint(1, 3)   #picks a random number between 1 and 3
    for x in range(amount):     #generates a certain amount of rooms dependent on the number generated for amount
        room()

#used to generate the enemys in random locations on the map #v#
    for y in range(height - 1):                             #|# runs through the height of the map 
        for x in range(width):                              #|# runs through the width of the map
            if grid[y][x] == " ":                           #|# if its a empty space it will run to see if it will place a enemy there or not
                place = random.randint(1, 100)              #|# generates a random number between 1 and 100
                if place >= 98:                             #|# if the number is 98, 99, or 100 it places an enemy (3% chance)
                    grid[y][x] = "!"                        #^# places the enemy
                    enemies.append((y, x))

#used to generate the gold in random locations on the map   #v#
    for y in range(height - 1):                             #|# runs through the height of the map
        for x in range(width):                              #|# runs through the width of the map
            if grid[y][x] == " ":                           #|# if its a empty space it will run to see if it will place a peice of gold there or not
                place = random.randint(1, 100)              #|# generates a random number between 1 and 100
                if place >= 95:                             #|# if the number is 95, 96, 97, 98, 99, or 100 it generates a gold peice (6% chance)
                    grid[y][x] = "%"                        #^# generates the gold

#used to generate keys randomly on the map                  #v#
    for y in range(height):                                 #|#
        for x in range(width):                              #|#
            if grid[y][x] == " ":                           #|#
                place = random.randint(1, 1000)             #|# generates a random number between 1 and 1000
                if place > 999:                             #|# places a key if the number is above 999, (0.1% chance)
                    grid[y][x] = "$"                        #^#
    return start_x      #returns the start_x variable so it knows where to place the player in their x coord at the start
#------------------------------------------------------------------------------------------------------------------------------------
def display_map():      #the maps display function
    global life, enemies
    time.sleep(.1)
    new()       #clears the terminal to keep it from getting messy
    screen = "" #makes an empty string called screen
    for row in grid:    #runs through all the rows in the grid
        line = ""   #makes an empty string called line
        for char in row:    #runs through all the characters in the row
            if char == "#":     #if its a # (wall) it colors it and resizes it
                line += Fore.LIGHTBLACK_EX + Back.LIGHTBLACK_EX + "##"
            elif char == "*":   #if its a * (player) it colors it and resizes it
                line += Fore.BLUE + Back.LIGHTWHITE_EX + Style.BRIGHT + "[]" + Style.RESET_ALL
            elif char == "%":   #if its a % (gold) it colors it and resizes it
                line += Fore.LIGHTYELLOW_EX + Back.LIGHTYELLOW_EX + "%%"
            elif char == "!":   #if its a ! (enemy) it colors it and resizes it
                line += Fore.RED + Back.RED + "!!"
            elif char == "$":   #if its a $ (key) it colors it and resizes it
                line += Fore.GREEN + Back.GREEN + "$$"
            elif char == "&":   #if its a & (room) it colors it and resizes it
                line += Fore.MAGENTA + Back.MAGENTA + "&&"
            elif char == " ":   #if its a space it resizes it
                line += Back.WHITE + "  "
        screen += line + "\n"   #adds the line the the string variable
    screen += Back.RESET + Fore.RED + "Life: "  #adds the word life on the screen
    
    lives = ["!"] * life        #makes an array with ! times the number of lifes the player has
    for x in range(len(lives)):     #adds the amount of lifes to the screen variable and colors them so the player can see their lives
        line = Back.LIGHTRED_EX + Fore.LIGHTRED_EX + "!!" + Back.BLACK + Fore.BLACK + "!"
        screen += line
    screen += "   " + Fore.LIGHTYELLOW_EX + Back.RESET + f"\n\nGold: {gold}\n" + Fore.GREEN + f"Keys: {key}\n" + Fore.CYAN + f"Use W,A,S,D to move\n"       #adds the players gold, keys and a prompt to the creen variable
    print(screen, end="")       #prints everything in the screen variable onto the screen for the player to see
#------------------------------------------------------------------------------------------------------------------------------------
def room():     #the room generation function
    global grid
    exist = "no"    #sets exist to no by default
    player_y = random.randint(1, height - (size + 1))   #sets the players y coord to a random location
    player_x = random.randint(1, width - (size + 1))        #sets the players x coord to a random location
    for y in range(size):       #generates the room dependent on the set size for them
        for x in range(size):
            if grid[player_y + y][player_x + x] == " ":     #if their is already a space path where the room is trying to generate it sets exist to yes
                exist = "yes"
            grid[player_y + y][player_x + x] = "&"      #makes the room & so it can know where the room is
    
    if exist != "yes":      #if exist does not = yes then it runs this
        player_y += random.randint(0, size)     #picks a random spot withen the room itself
        player_x += random.randint(0, size)     #^#
        grid[player_y][player_x] = "$"  #makes it a $ (doesnt affect the key generation i just used the same symbol for both of these cause i was lazy)
        i = 0   #sets i to 0 be default
        while player_x != width:    #if the players x coord doesnt = the width this runs
            if grid[player_y][player_x] != " ":     #tests if the players location is empty or not
                player_x += 1       #moves the player right 1
                i += 1  #adds 1 to the i variable
            elif grid[player_y][player_x] == " ":   #if the current player location does = a space " " it runs this
                while i > 0:    #if i is greater than 0 it makes it a path then resets i
                    grid[player_y][player_x - i] = "&"
                    i -= 1
                if i == 0:  #if i is 0 it does nothing
                    break
        player_x -= i   #resets the players x coord
        while grid[player_y][player_x] != " ":  #if the player isnt on a space it makes it a space then moves the player left and repeats
            grid[player_y][player_x] = " "
            player_x -= 1
    path()  #runs the path function
#------------------------------------------------------------------------------------------------------------------------------------
def path():     #the function that turns the room from being pink into white
    for y in range(height):
        for x in range(width):
            if grid[y][x] == "&":      #if their is a & then it makes it a space " "
                grid[y][x] = " "
#------------------------------------------------------------------------------------------------------------------------------------
def enemy_move():       #the function that lets enemies move
    global enemies, grid, life, player_y, player_x
    try:    #trys to run this function, it does this because of when i was trying to remove a enemy from the enemies string after they are eleminated by the player it would crash the program due to enemies length not being the same anymore (which i think is kinda dum)
        for z in range(len(enemies)):   #runs for the amount of times that there is enemies
            enemy_y, enemy_x = enemies[z]   #sets the enemy x and y coord to the ones saved in the z location of enemies
            direction = random.randint(1, 4)        #picks a random direction
            if direction == 1 and grid[enemy_y - 1][enemy_x] != "#" and grid[enemy_y - 1][enemy_x] != "!":      #if the direction is 1 and their isnt a wall or another enemy above them it moves them up 1
                grid[enemy_y][enemy_x] = " "
                enemy_y -= 1
            elif direction == 2 and grid[enemy_y + 1][enemy_x] != "#" and enemy_y + 1 != height - 1 and grid[enemy_y + 1][enemy_x] != "!":      #if the direction is 1 and their isnt a wall or another enemy below them it moves them down 1
                grid[enemy_y][enemy_x] = " "
                enemy_y += 1
            elif direction == 3 and grid[enemy_y][enemy_x - 1] != "#" and grid[enemy_y][enemy_x - 1] != "!":        #if the direction is 1 and their isnt a wall or another enemy next to them it moves them left 1
                grid[enemy_y][enemy_x] = " "
                enemy_x -= 1
            elif direction == 4 and grid[enemy_y][enemy_x + 1] != "#" and grid[enemy_y][enemy_x + 1] != "!":        #if the direction is 1 and their isnt a wall or another enemy next to them it moves them right 1
                grid[enemy_y][enemy_x] = " "
                enemy_x += 1
            
            if grid[enemy_y][enemy_x] == grid[player_y][player_x]:      #if the player runs into an enemy it removes 1 life from them and removes the enemy from the map
                life -= 1
                del enemies[z]
                grid[player_y][player_x] = "*"
            elif grid[enemy_y][enemy_x] != grid[player_y][player_x]:        #if the enemy isnt in the same spot as the player it moves them and updates its coords in the enemies variable
                grid[enemy_y][enemy_x] = "!"
                enemies[z] = enemy_y, enemy_x
    except:     #if the function comes up with an error it ignores it
        pass
#------------------------------------------------------------------------------------------------------------------------------------
def inventory():        #the inventory funtion
    inv = ""        #creates a empty string called inv
    while inv != "q":   #runs this loop until inv = q
        clear()     #clears the screen
        print(Fore.YELLOW + "Gold:" + Fore.WHITE, gold, Fore.GREEN + "\nKeys:" + Fore.WHITE, key, Fore.LIGHTRED_EX + "\nLife:" + Fore.WHITE, life, Fore.LIGHTBLUE_EX + "\nPress Q to exit the inventory")       #displays what the user has in their inventory
        inv = readchar.readkey().lower()    #takes user input
    time.sleep(0.5)     #waits 0.5 seconds
#------------------------------------------------------------------------------------------------------------------------------------
def shop():     #the shop function
    global gold, life, key
    shop = ""       #creates a empty string called shop
    while shop != "q":      #runs this loop until shop = q
        clear()     #clears the screen
        print(Fore.LIGHTBLUE_EX + "Press the corresponding button to what you want to buy:" + Fore.YELLOW + "\nGold:", gold, Fore.GREEN + "\nKeys:", key, Fore.LIGHTRED_EX + "\nM: Extra Life" + Fore.WHITE + "    100 Gold" + Fore.LIGHTRED_EX + "\nC: Open Chest" + Fore.WHITE + "    1 Key" + Fore.LIGHTRED_EX + "\nQ: Leave the shop")    #prints info about the shop and some prompts
        shop = readchar.readkey().lower()
        if shop == "c":         #if the player pushes c it runs this if statement
            if key >= 1:    #if they have a key this runs
                key -= 1        #takes a key from the player
                amount = random.randint(50, 200)    #generates a random number from 50 - 200
                gold += amount  #adds the randomly generated amount to the players gold count
                print(Fore.LIGHTBLUE_EX + "You have Opened a chest using a key, and gained" + Fore.WHITE, amount, Fore.LIGHTBLUE_EX + "Gold from it")   #tells them they opened a chest and how much gold they got
                time.sleep(1.5) #waits 1.5 seconds
            else:   #if they dont have a key this runs
                print(Fore.RED + f"You dont have enough keys for that, you need", 1 - key, Fore.RED + "more keys")  #lets the player know they need more keys to buy this
        if shop == "m":     #if the player pushes m it runs this if statement
            if gold >= 100:    #if the player has more than 99 gold it runs
                gold -= 100     #takes 100 gold from the player
                print(Fore.LIGHTBLUE_EX + "You have succsessfully bought another Life!")    #tells them they bought another life
                life += 1   #gives the player another life
            else:   #if the player has less than 100 gold it tells them they need more and how much more they need
                print(Fore.RED + f"You dont have enough gold for that, you need", 100 - gold, Fore.RED + "more gold")
        time.sleep(1.5)     #waits 1.5 seconds
#------------------------------------------------------------------------------------------------------------------------------------
def info():     #the info function
    info = ""   #sets a empty string called info
    while info != "q":      #if info isnt q it keeps running the loop
        clear()     #clears the screen
        print(Fore.MAGENTA + "Dungeon:\nYou can travel through a randomly generated dungeon to collect gold and keys, and fight enemies\nBe warned if you run out of life you lose the game\n\nInventory:\nYou can view your gold, keys, and life here\n\nShop:\nYou can buy extra lifes or open a chest that has a chance of giving you 50-200 gold\n" + Fore.LIGHTBLUE_EX + "\nPress Q to exit the inventory")        #prints info about the game
        info = readchar.readkey().lower()   #takes the user input
    time.sleep(0.5)     #waits 0.5 seconds before continuing
#------------------------------------------------------------------------------------------------------------------------------------
def clear():    #completly clears the screen of all text
    os.system('cls' if os.name == 'nt' else 'clear')
#------------------------------------------------------------------------------------------------------------------------------------
def new():      #overides the current text so that it doesnt cause flashing on the screen when done quickly
    print("\033[H", end="")
#------------------------------------------------------------------------------------------------------------------------------------