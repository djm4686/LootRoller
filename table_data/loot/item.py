__author__ = 'dmadden'
from weapon import WEAPON_CHECK, MAGIC_WEAPON
from armor import ARMOR_CHECK, MAGIC_ARMOR
from equipment import EQUIPMENT
from potion import POTION
from scroll import SCROLL
from table_data.table_data import TableData

ITEM = TableData("Item Type")
ITEM.add_item("Weapon", 1, 20, [WEAPON_CHECK])
ITEM.add_item("Armor", 21, 40, [ARMOR_CHECK])
ITEM.add_item("Equipment", 41, 70, [EQUIPMENT])
ITEM.add_item("Potion", 71, 85, [POTION])
ITEM.add_item("Scroll", 86, 100, [SCROLL])
#ITEM.add_item("Special", 91, 100, [SPECIAL])

MAGIC_ITEM = TableData("Magic Item", normalize=True)
MAGIC_ITEM.add_item("Weapon", 0, 0, [MAGIC_WEAPON])
MAGIC_ITEM.add_item("Armor", 0, 0, [MAGIC_ARMOR])
MAGIC_ITEM.add_item("Potion", 0, 0, [POTION])
MAGIC_ITEM.add_item("Scroll", 0, 0, [SCROLL])
