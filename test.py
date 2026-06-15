import threading
import time

def loop_one():
	while True:
		print("Loop 1 is running...")
		time.sleep(1)

def loop_two():
	while True:
		print("Loop 2 is running...")
		time.sleep(1)

threading.Thread(target=loop_one, daemon=True).start()
threading.Thread(target=loop_two, daemon=True).start()

while True: time.sleep(1)
