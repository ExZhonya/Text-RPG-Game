from preset import utils as u
from preset.utils import cost, money_text
from plr.player import player

WEAPONS = {
	"1": ("Wooden Sword",  cost(bronze=10)),
	"2": ("Stone Sword",   cost(bronze=40)),
	"3": ("Bronze Sword",  cost(silver=1)),
	"4": ("Iron Sword",    cost(silver=5)),
	"5": ("Diamond Sword", cost(silver=35)),
}

ARMOR = {
	"1": ("Leather Armor", cost(bronze=20)),
	"2": ("Iron Armor",    cost(silver=3)),
}

def _browse(category, items):
	msg = ""
	while True:
		u.clear()
		print(f"===== {category.title()} Shop =====   Money: {money_text(player.money)}")
		for key, (name, price) in items.items():
			if name in player.inventory[category]:
				tag = "Owned (Equipped)" if getattr(player, category) == name else "Owned"
			else:
				tag = money_text(price)
			print(f"{key}. {name:<15}| {tag}")
		print("0. Back")
		if msg:
			print(f"\n{msg}")

		x = u.getch()
		if x == "0":
			return
		if x not in items:
			msg = ""
			continue

		name, price = items[x]
		if name in player.inventory[category]:
			setattr(player, category, name)				# already owned > just equip
			msg = f"You equipped {name}."
		elif player.money < price:
			msg = "You don't have enough money."
		else:
			player.money -= price
			player.inventory[category].append(name)
			setattr(player, category, name)				# auto-equip what you buy
			msg = f"You bought {name}!"

class shop:
	@staticmethod
	def Weapon():
		_browse("weapon", WEAPONS)

	@staticmethod
	def Armor():
		_browse("armor", ARMOR)