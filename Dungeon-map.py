import random
import time
import sys
import os
from colorama import Fore, Back , Style, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

grid = []
gold = 0
width = 30
height = 12
timeout = 5

start_time = time.time()

for y in range(height):
    row = ["#"] * width
    grid.append(row)

start_x = random.randint(2, width - 3)

player_x = start_x
player_y = 0

while player_y < height - 1:
    if time.time() - start_time > timeout:   
        sys.exit("Map generation timed out. Try again")

    grid[player_y][player_x] = " "
    direction = random.choices(["down","left","right","up"], weights=[20, 30, 30, 20])[0]

    if direction == "down":
        if player_y + 1 == " ":
            direction = "left"
        else:
            player_y += 1
    elif direction == "left" and player_x > 1:
        if player_x - 1 == " ":
            direction = "right"
        else:
            player_x -= 1
    elif direction == "right" and player_x < width - 2:
        if player_x + 1 == " ":
            direction = "up"
        else:
            player_x += 1
    elif direction == "up" and player_y > 1:
        if player_y - 1 == " ":
            print("Error")
            break
        else:
            player_y -= 1

grid[height -1][player_x] = " "

player_x = start_x
player_y = 0
grid[player_y][player_x] = "*"

for row in grid:
        print("".join(row))
while player_y != height - 1:
    print("Gold: ", gold)
    move = input("w = up, s = down, d = right, a = left: ").lower()
    grid[player_y][player_x] = " "

    if move == "s" and player_y + 1 < height and grid[player_y + 1][player_x] != "#":
        player_y += 1
    if move == "w" and grid[player_y - 1][player_x] != "#":
        player_y -= 1 
    if move == "d" and grid[player_y][player_x + 1] != "#":
        player_x += 1
    if move == "a" and grid[player_y][player_x - 1] != "#":
        player_x -= 1

    if grid[player_y][player_x] == "%":
        value = random.randint(1, 5)
        gold += value
    clear_screen()
    grid[player_y][player_x] = "*"
    for row in grid:
        line = ""
        for char in row:
            if char == "#":
                line += Fore.GREEN + Back.GREEN + "#"
            elif char == "*":
                line += Fore.RED + Back.LIGHTBLACK_EX + "*"
            else:
                line += Back.LIGHTBLACK_EX + char
        print(line)

    if player_y == height - 1:
        print("Congratulations you won!")