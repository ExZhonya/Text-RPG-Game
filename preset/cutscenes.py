import time, os, sys
from preset import utils as u

def _dots(n=3, delay = 1.5):
	for _ in range(n):
		print(".")
		time.sleep(delay)

def start():
	u.clear()
	_dots()
	u.slow_print("It's dark. You don't know where you are.")
	time.sleep(2)
	_dots()
	u.slow_print("You slowly open your eyes and see that you're in some kind of camp.")
	u.getch()


