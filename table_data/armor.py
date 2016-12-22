from table_data import TableData

ARMOR = TableData("Armor", normalize=True)
ARMOR.add_item("Armored Coat", 0, 0, [])
ARMOR.add_item("Breastplate", 0, 0, [])
ARMOR.add_item("Scale Mail", 0, 0, [])
ARMOR.add_item("Chain Mail", 0, 0, [])
ARMOR.add_item("Hide", 0, 0, [])
ARMOR.add_item("Banded Mail", 0, 0, [])
ARMOR.add_item("Splint Mail", 0, 0, [])
ARMOR.add_item("Half-plate", 0, 0, [])
ARMOR.add_item("Full-plate", 0, 0, [])
ARMOR.add_item("Buckler", 0, 0, [])
ARMOR.add_item("Light wooden shield", 0, 0, [])
ARMOR.add_item("Light steel shield", 0, 0, [])
ARMOR.add_item("Heavy wooden shield", 0, 0, [])
ARMOR.add_item("Heavy steel shield", 0, 0, [])
ARMOR.add_item("Tower shield", 0, 0, [])

MAGIC_ARMOR = TableData("Magic Armor", magic=True, normalize=True)

ARMOR_CHECK = TableData("Armor Mundane/Magic")
ARMOR_CHECK.add_item("Mundane", 1, 90, [ARMOR])
ARMOR_CHECK.add_item("Magic", 91, 100, [MAGIC_ARMOR])
