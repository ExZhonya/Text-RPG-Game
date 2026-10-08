class Player:
	MAX_HEALTH = 100

	# SAVE FILES NECCESITIES
	SAVE_TYPES = {
		"day": int,
		"fuel": int,
		"food": int,
		"health": int,
		"max_health": int,
		"money": int,
		"trader": bool,
		"hunter": bool,
		"lumberjack": bool,
		"base": bool,
		"weapon": (str, type(None)),
		"armor": (str, type(None)),
		"inventory": dict,
	}

	def __init__(self):
		self.reset()

	def reset(self):
		self.day = 1
		self.fuel = 0
		self.food = 0
		self.max_health = self.MAX_HEALTH
		self.health = self.max_health
		self.money = 30
		self.trader = False
		self.hunter = False
		self.lumberjack = False
		self.base = True
		self.weapon = None
		self.armor = None
		self.inventory = {"weapon": [], "armor": []}
	
	def change_health(self, amount):
		original = self.health
		self.health = max(0, min(self.max_health, original + amount))
		return self.health - original

	def is_alive(self):
		return self.health > 0

	def to_dict(self):
		return {
			"day": self.day,
			"fuel": self.fuel,
			"food": self.food,
			"health": self.health,
			"max_health": self.max_health,
			"money": self.money,
			"trader": self.trader,
			"hunter": self.hunter,
			"lumberjack": self.lumberjack,
			"base": self.base,
			"weapon": self.weapon,
			"armor": self.armor,
			"inventory": {k: list(v) for k, v in self.inventory.items()},
		}

	def load_dict(self, data):
		new = {}
		for key, kind in self.SAVE_TYPES.items():
			if key not in data:
				continue
			value = data[key]
			if not isinstance(value, kind) or (kind is int and isinstance(value, bool)):
				raise ValueError(f"bad falue for '{key}'")
			new[key] = value

		inv = {"weapon": [], "armor": []}
		saved_inv = new.get("inventory", {})
		for category in inv:
			items = saved_inv.get(category, [])
			if not isinstance(items, list) or not all(isinstance(i, str) for i in items):
				raise ValueError(f"bad inventory '{category}'")
			inv[category] = list(items)
		new["inventory"] = inv

		self.reset()
		for key, value in new.items():
			setattr(self, key, value)
		self.health = max(0, min(self.health, self.max_health))


player = Player()