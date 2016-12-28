from table_data.table_data import GoldData
from item import MAGIC_ITEM

MULTIPLIER = 8
GOLD = GoldData(MULTIPLIER)
GOLD.add_item(1, 1, 10, [])
GOLD.add_item(5, 11, 20, [])
GOLD.add_item(10, 21, 30, [])
GOLD.add_item(15, 31, 40, [])
GOLD.add_item(20, 41, 50, [])
GOLD.add_item(25, 51, 60, [])
GOLD.add_item(30, 61, 70, [])
GOLD.add_item(40, 71, 80, [])
GOLD.add_item(50, 81, 90, [])
GOLD.add_item(75, 91, 98, [])
GOLD.add_item(100, 99, 100, [MAGIC_ITEM])

def set_gold_multiplier(mult):
    GOLD.update_multiplier(mult)
