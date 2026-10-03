import sys, os, time

def clear():
	os.system("cls" if sys.platform == "win32" else "clear")

if sys.platform == "win32":
	import msvcrt
	def getch():
		ch = msvcrt.getch()
		if ch == b'\x03':
			raise KeyboardInterrupt
		if ch in (b'\x00', b'\xe0'):
			msvcrt.getch()
			return ""
		return ch.decode('utf-8', errors='ignore')
else:
	import tty, termios
	def getch():
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setcbreak(fd)
			return sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def _delay_print(text, delay):
	for c in text:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(delay)
	print()

def v_fast_print(text): _delay_print(text, 0.01)
def fast_print(text):   _delay_print(text, 0.03)
def slow_print(text):   _delay_print(text, 0.05)

SILVER = 100          # 1 Silver = 100 Bronze
GOLD = 100 * SILVER   # 1 Gold = 100 Silver = 10,000 Bronze

def cost(gold=0, silver=0, bronze=0):
	return gold * GOLD + silver * SILVER + bronze

def money_text(bronze):
	g, rest = divmod(bronze, GOLD)
	s, b = divmod(rest, SILVER)
	parts = []
	if g: parts.append(f"{g} Gold")
	if s: parts.append(f"{s} Silver")
	if b or not parts: parts.append(f"{b} Bronze")
	return " ".join(parts)