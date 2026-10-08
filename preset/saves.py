import json, os, time
from pathlib import Path
from preset import utils as u
from plr.player import player

SAVES_DIR = Path(__file__).resolve().parent.parent / "saves"
SAVE_VERSION = 1
SLOTS = 3

def _path(slot):
	return SAVES_DIR / f"slot {slot}.json"

def _read(slot): # parse a slot file, raise valueerror if it's missing or broken
	with open(_path(slot), encoding="utf-8") as f:
		payload = json.load(f)
	if not isinstance(payload, dict) or not isinstance(payload.get("player"), dict):
		raise ValueError("Not a save file!")
	return payload

def _summary(slot): # kind of like desc shown in slot menu
	if not _path(slot).exists():
		return "Empty"
	try:
		p = _read(slot)["player"]
		return f"Day: {p['day']} | Health: {p['health']} | {u.money_text(p['money'])}"
	except (OSError, ValueError, TypeError, KeyError):
		return "Corrupted"

def save_game(slot):
	payload = {
		"version": SAVE_VERSION,
		"saved_at": time.strftime("%Y-%m-%d %H:%M:%S"),
		"player": player.to_dict(),
	}
	tmp = _path(slot).with_suffix(".tmp")
	try:
		SAVES_DIR.mkdir(exist_ok=True)
		with open(tmp, "w", encoding="utf-8") as f:
			json.dump(payload, f, indent=4)
		os.replace(tmp, _path(slot))
	except OSError as e:
		return False, f"Error. Could not save: {e}"
	return True, f"Game saved to slot {slot}"

def load_game(slot):
	if not _path(slot).exists():
		return False, "That slot is empty"
	try:
		payload = _read(slot)
		if payload.get("version" , 1) > SAVE_VERSION:
			return False, "That save is from a newer version of the game."
		player.load_dict(payload["player"])
	except (OSError, ValueError):
		return False, "Error! That save file is corrupted."
	return True, f"Loaded slot {slot}"

def slot_menu():
	pass
