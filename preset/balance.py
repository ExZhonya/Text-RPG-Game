import random as r
from preset.utils import cost

CAP_DAY = 50

HEALTH_START = 100
HEALTH_UPG = 10
HEALTH_CAP = 300

def _tier(day):
    return (min(day, CAP_DAY) - 1) //5
    # increase by 1 everry 5 days, caps at 50 which is tier 9

# ---- gathering and money obtained amoun t ----
def gather_amount(day):
    t = _tier(day)
    return r.randint(1 + t, 3 + 2 * t)

def money_amount(day):
    t = _tier(day)
    return r.randint(1 + 3 * t, 3 + 6 * t)

# ---- camp neccesity -----
def fuel_needed(day):
    return 1 + _tier(day)

def food_needed(day):
    return 1 + (min(day, CAP_DAY) - 1) // 7

def shortage_dmg(shortage):
    return min(30, 10 * shortage)

# ----- blacksmith? temporary function tho -----:
def health_level(max_health):
    return (max_health - HEALTH_START) // HEALTH_UPG

def health_upg_price(max_health):
    return cost(bronze=50 * (health_level(max_health) + 1))

def health_max(max_health):
    return max_health >= HEALTH_CAP
