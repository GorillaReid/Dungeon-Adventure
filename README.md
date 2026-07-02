Dungeon Adventure:
	This is a dungeon based game that you run in your devices terminal or shell

<img width="222.1" height="257.1" alt="IMG_0144" src="https://github.com/user-attachments/assets/749126a1-2c5b-4367-833f-d952bfb28b2c" />

https://github.com/GorillaReid/Dungeon-Adventure/releases/tag/v1.0.0
	
*Note: Currently this only works with Linux devices Windows and Mac cant run it at the moment, sorry if this is a inconvenience. I hope to get versions campatible with all devices soon.*
- To play the game click the link above then download the Dungeon-Adventure file, after you do that open your terminal and go to the folder with the file (ex. cd ~/Downloads) and run **chmod +x Dungeon-Adventure**, after running that command you should just need to type the command **./Dungeon-Adventure** and it should start the game. Hope you guys enjoy!

Required python libraries/packages:
(*YOU DONT NEED THESE TO PLAY IF YOU DOWNLOAD THE Dungeon-Adventure FILE BUT OPTIONAL IF YOU WANT TO RUN IT WITHOUT THE FILE (NOT RECCOMENDED)*)
- python3: sudo apt install python3
- colorama: python3 -m pip install colorama	  or	  sudo apt install python-colorama
- readchar: python3 -m pip install readchar	  or	  sudo apt install python-readchar

Features:
- Randomly generating dungeon levels
- Colored text and map
- A Shop to buy more lifes or open chests
- An inventory to view your items and lives
- A Info section to explain a little about the game

Explanation of how the random dungeon generation works:
- To generate random dungeons each time I created a function that basicly starts at the players starting position and then picks a random direction up, down, left, or right to generate a path to. Each direction has a different weight so that its more likely to go down than up, they also have statements to check and make sure its not trying to generate a path outside the map. After it reaches the bottom it stops and resets the players position the the start and lets them play the game.

Credits:
- I used the readchar and random libraries the most out of all of them.
- I used Grok to help with debugging or learning a new skill I didnt know how to do like how to use the readchar library so that the player just has to push the button and not need to click enter every time they want to move.
- The creator of the ysws program Rift, I joined their program because I thought it sounded like fun, and one of the projects I got given to work on was called "maze maybe", it was just a simple program to generate a basic random map of " " and "#" and I modified it a bit adding a player and player movement. I then thought it was a cool project idea and decided to make a Stardance project out of it. So thanks a lot for helping give me the idea for my project even if you didn't know it at the time.
