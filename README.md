Dungeon Adventure
	This is a dungeon based game that you run in your devices terminal or shell

	IMAGE

	DEMO LINK

required python libarys/packages:
	sudo apt install python3
	python3 -m pip install colorama		or		sudo apt install python-colorama
	python3 -m pip install readchar		or		sudo apt install python-readchar

- Randomly generating dungeon levels
- Colored text and map
- A Shop to buy more lifes or open chests
- An inventory to view your items and lives
- A Info section to explain a little about the game

	To generate random dungeons each time I created a function that basicly starts at the players starting position and then picks a random direction up, down, left, or right to generate a path to. Each direction has a different weight so that its more likely to go down than up, they also have statements to check and make sure its not trying to generate a path outside the map. After it reaches the bottom it stops and resets the players position the the start and lets them play the game.

Credits:
	I used the readchar and random libarys the most out of all of them.
	I used Grok to help with debugging or learing a new skill I didnt know how to do like how to use the readchar libary so that the player just has to push the button and not need to click enter everytime they want to move.
	The creater of the ysws prgram Rift, I joined their program because I thought it sounded like fun, and one of the projects I got given to work on was called "maze maybe", it was just a simple program to generate a basic random map of " " and "#" and I modified it a bit adding a player and player movement. I then thought it was a cool project idea and decided to make a Stardance project out of it. So thanks alot for helping give me the idea for my project even if you didnt know it at the time.