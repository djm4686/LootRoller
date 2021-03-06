from table_data.table_data import TableData

ARMOR = TableData("Armor", normalize=True, ext=True, final=True)
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

MATERIAL = TableData("Material", ext=True)
MATERIAL.add_item("Bone", 1, 20, [ARMOR])
MATERIAL.add_item("Darkwood", 21, 40, [ARMOR])
MATERIAL.add_item("Obsidian", 41, 55, [ARMOR])
MATERIAL.add_item("Mithral", 56, 65, [ARMOR])
MATERIAL.add_item("Gold", 66, 75, [ARMOR])
MATERIAL.add_item("Ethereal", 76, 80, [ARMOR])
MATERIAL.add_item("Adamantine", 81, 85, [ARMOR])
MATERIAL.add_item("Viridium", 86, 90, [ARMOR])
MATERIAL.add_item("Silversheen", 91, 100, [ARMOR])

CHECK_MATERIAL = TableData("Check Material")
CHECK_MATERIAL.add_item("Regular", 1, 80, [ARMOR])
CHECK_MATERIAL.add_item("Altered", 81, 100, [MATERIAL])

LESSER_MINOR = TableData("Lesser Minor Weapon", ext=True, normalize=True)
LESSER_MINOR.add_item("Benevolent", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Poison-resistant", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Balanced", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Bitter", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Bolstering", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Brawling", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Champion", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Dastard", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Deathless", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Defiant", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Light Fortification", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Grinding", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Impervious", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Mirrored", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Spell storing", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Stanching", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Warding", 0, 0, [CHECK_MATERIAL])

PLUS_ONE = TableData("+1", ext=True)
PLUS_ONE.add_item("+1", 1, 100, [CHECK_MATERIAL])

CHECK_LESSER_MINOR = TableData("Check +1")
CHECK_LESSER_MINOR.add_item("+1", 1, 50, [PLUS_ONE])
CHECK_LESSER_MINOR.add_item("Other", 51, 100, [LESSER_MINOR])

MAGIC_ARMOR = TableData("Magic Armor")
MAGIC_ARMOR.add_item("Lesser Minor Magic", 1, 200, [CHECK_LESSER_MINOR])
MAGIC_ARMOR.add_item("Greater Minor Magic", 201, 400, [])
MAGIC_ARMOR.add_item("Lesser Medium Magic", 401, 600, [])
MAGIC_ARMOR.add_item("Greater Medium Magic", 601, 800, [])
MAGIC_ARMOR.add_item("Lesser Major Magic", 801, 1000, [])
MAGIC_ARMOR.add_item("Greater Major Magic", 1001, 10000, [])

ARMOR_CHECK = TableData("Armor Mundane/Magic")
ARMOR_CHECK.add_item("Mundane", 1, 80, [CHECK_MATERIAL])
ARMOR_CHECK.add_item("Magic", 81, 100, [MAGIC_ARMOR])
