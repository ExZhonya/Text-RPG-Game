from preset import utils as u
from preset import npc_dia as n
from preset import balance as b
from preset import saves
from plr.player import player

UNLOCKS = {
	3: ("lumberjack", "A lumberjack wandered into camp and offers his services."),
	6: ("hunter", "A Hunter has set up a tent near your camp."),
	10:("trader", "A humble trader has come to your peaceful camp.")
}

def _consume(resource, need, msg):
	have = getattr(player, resource)
	if have >= need:
		setattr(player, resource, have - need)
		return True
	setattr(player, resource, 0)
	damage = b.shortage_dmg(need - have)
	player.change_health(-damage)
	u.slow_print(f"{msg} (-{damage} Health)")
	return False

def _rest_heal(fed, warm):
	if fed and warm:
		healed = player.change_health(10)
		u.slow_print(f"You slept well. | +{healed} Health" if healed else "You slept well")

def _check_unlock():
	if player.day in UNLOCKS:
		attr, text = UNLOCKS[player.day]
		setattr(player, attr, True)
		u.slow_print(text)

class Base:
	@staticmethod
	def camp():
		u.clear()
		print(rf"""
		You are in the Camp. | Day: {player.day}
		Fuel: {player.fuel}  Food: {player.food}  Health: {player.health} Money: {u.money_text(player.money)}
		1. Find Fuel
		2. Find Food
		3. Explore
		4. Rest (End the day.)
		5. NPC
		9. Save/Load Menu
		0. Quit (unsaved progress is lost!)
		""")
		x = u.getch()
		if x == "1":
			Base.chop_wood()
		elif x == "2":
			Base.find_food()
		elif x == "3":
			Base.explore()
		elif x =="4":
			Base.rest()
		elif x == "5":
			Base.NPC()
		elif x == "9":
			Base.save_menu()
		elif x == "0":
			return False
		return player.health > 0

	@staticmethod
	def save_menu():
		while True:
			u.clear()
			print("""

	1. Save Game
	2. Load Game
	0. Go Back
""")
			x = u.getch()
			if x == "1":
				saves.slot_menu("save")
			elif x == "2":
				saves.slot_menu("load")
			elif x == "0":
				return

	@staticmethod
	def rest():
		u.clear()
		fed = _consume("food", b.food_needed(player.day), "You went to sleep hungry")
		warm = _consume("fuel", b.fuel_needed(player.day), "You are cold.")
		player.day += 1
		_rest_heal(fed, warm)
		u.getch()
		if not player.is_alive():
			u.clear()
			u.slow_print("You didn't survive the night...")
			return
		_check_unlock()
		u.getch()

	@staticmethod
	def chop_wood():
		u.clear()
		gained = b.gather_amount(player.day)
		player.fuel += gained
		u.fast_print(f"You gain {gained} fuel.")
		u.getch()

	@staticmethod
	def find_food():
		u.clear()
		gained = b.gather_amount(player.day)
		player.food += gained
		u.fast_print(f"You gain {gained} food.")
		u.getch()

	@staticmethod
	def explore():
		u.clear()
		gained = b.gather_amount(player.day)
		player.money += gained
		u.fast_print(f"You gained {gained} money.")
		u.getch()

	@staticmethod
	def NPC():
		while True:
			u.clear()
			print("===== NPC =====")
			if player.trader:
				print("1. Trader")
			if player.hunter:
				print("2. Hunter")
			if player.lumberjack:
				print("3. Lumberjack")
			print("0. Back")

			x = u.getch()
			if x == "1" and player.trader:
				n.NPC.Trader()
			elif x == "2" and player.hunter:
				n.NPC.Hunter()
			elif x == "3" and player.lumberjack:
				n.NPC.Lumberjack()
			elif x == "0":
				return

if __name__ == '__main__':
	while Base.camp():
		pass