from table_data.table_data import TableData

WEAPON = TableData("Weapon", ext=True, normalize=True, final=True)
WEAPON.add_item("Dagger", 0, 0, [])
WEAPON.add_item("Quarterstaff", 0, 0, [])
WEAPON.add_item("Spear", 0, 0, [])
WEAPON.add_item("Longspear", 0, 0, [])
WEAPON.add_item("Blowgun", 0, 0, [])
WEAPON.add_item("Heavy Crossbow", 0, 0, [])
WEAPON.add_item("Light Crossbow", 0, 0, [])
WEAPON.add_item("Dart x10", 0, 0, [])
WEAPON.add_item("Javelin", 0, 0, [])
WEAPON.add_item("Sling", 0, 0, [])
WEAPON.add_item("Gauntlet", 0, 0, [])
WEAPON.add_item("Cestus", 0, 0, [])
WEAPON.add_item("Punching Dagger", 0, 0, [])
WEAPON.add_item("Spiked Gauntlet", 0, 0, [])
WEAPON.add_item("Light Mace", 0, 0, [])
WEAPON.add_item("Sickle", 0, 0, [])
WEAPON.add_item("Club", 0, 0, [])
WEAPON.add_item("Heavy Mace", 0, 0, [])
WEAPON.add_item("Morningstar", 0, 0, [])
WEAPON.add_item("Shortspear", 0, 0, [])
WEAPON.add_item("Gladius", 0, 0, [])
WEAPON.add_item("Handaxe", 0, 0, [])
WEAPON.add_item("Jutte", 0, 0, [])
WEAPON.add_item("Kerambit", 0, 0, [])
WEAPON.add_item("Kukri", 0, 0, [])
WEAPON.add_item("Light hammer", 0, 0, [])
WEAPON.add_item("Light pick", 0, 0, [])
WEAPON.add_item("Sap", 0, 0, [])
WEAPON.add_item("Shortsword", 0, 0, [])
WEAPON.add_item("Throwing axe", 0, 0, [])
WEAPON.add_item("Battleaxe", 0, 0, [])
WEAPON.add_item("Heavy Pick", 0, 0, [])
WEAPON.add_item("Light Flail", 0, 0, [])
WEAPON.add_item("Longsword", 0, 0, [])
WEAPON.add_item("Broadsword", 0, 0, [])
WEAPON.add_item("Rapier", 0, 0, [])
WEAPON.add_item("Scimitar", 0, 0, [])
WEAPON.add_item("Scizore", 0, 0, [])
WEAPON.add_item("Trident", 0, 0, [])
WEAPON.add_item("Warhammer", 0, 0, [])
WEAPON.add_item("Bardiche", 0, 0, [])
WEAPON.add_item("Falchion", 0, 0, [])
WEAPON.add_item("Glaive", 0, 0, [])
WEAPON.add_item("Greataxe", 0, 0, [])
WEAPON.add_item("Greatclub", 0, 0, [])
WEAPON.add_item("Greatsword", 0, 0, [])
WEAPON.add_item("Halberd", 0, 0, [])
WEAPON.add_item("Heavy Flail", 0, 0, [])
WEAPON.add_item("Lance", 0, 0, [])
WEAPON.add_item("Scythe", 0, 0, [])
WEAPON.add_item("Chakram", 0, 0, [])
WEAPON.add_item("Composite Longbow", 0, 0, [])
WEAPON.add_item("Composite Shortbow", 0, 0, [])
WEAPON.add_item("Longbow", 0, 0, [])
WEAPON.add_item("Shortbow", 0, 0, [])
WEAPON.add_item("Pilum", 0, 0, [])
WEAPON.add_item("Atlatl", 0, 0, [])
WEAPON.add_item("Fighting Fan", 0, 0, [])
WEAPON.add_item("Sai", 0, 0, [])
WEAPON.add_item("Aklys", 0, 0, [])
WEAPON.add_item("Scorpion Whip", 0, 0, [])
WEAPON.add_item("Nunchaku", 0, 0, [])
WEAPON.add_item("Swordbreaker", 0, 0, [])
WEAPON.add_item("Bastard Sword", 0, 0, [])
WEAPON.add_item("Dwarven Waraxe", 0, 0, [])
WEAPON.add_item("Hooked Axe", 0, 0, [])
WEAPON.add_item("Katana", 0, 0, [])
WEAPON.add_item("Whip", 0, 0, [])
WEAPON.add_item("Dire Flail", 0, 0, [])
WEAPON.add_item("Dwarven urgrosh", 0, 0, [])
WEAPON.add_item("Elven curve blade", 0, 0, [])
WEAPON.add_item("Harpoon", 0, 0, [])
WEAPON.add_item("Orc double axe", 0, 0, [])
WEAPON.add_item("Spiked chain", 0, 0, [])
WEAPON.add_item("Net", 0, 0, [])
WEAPON.add_item("Two Bladed Sword", 0, 0, [])
WEAPON.add_item("Gnome hooked hammer", 0, 0, [])
WEAPON.add_item("Boomerang", 0, 0, [])
WEAPON.add_item("Bolas", 0, 0, [])
WEAPON.add_item("Hand crossbow", 0, 0, [])
WEAPON.add_item("Lasso", 0, 0, [])
WEAPON.add_item("Repeating heavy crossbow", 0, 0, [])
WEAPON.add_item("Repeating light crossbow", 0, 0, [])
WEAPON.add_item("Shuriken x5", 0, 0, [])


MATERIAL = TableData("Material", ext=True)
MATERIAL.add_item("Bone", 1, 20, [WEAPON])
MATERIAL.add_item("Darkwood", 21, 40, [WEAPON])
MATERIAL.add_item("Obsidian", 41, 55, [WEAPON])
MATERIAL.add_item("Mithral", 56, 65, [WEAPON])
MATERIAL.add_item("Gold", 66, 75, [WEAPON])
MATERIAL.add_item("Ethereal", 76, 80, [WEAPON])
MATERIAL.add_item("Adamantine", 81, 85, [WEAPON])
MATERIAL.add_item("Viridium", 86, 90, [WEAPON])
MATERIAL.add_item("Silversheen", 91, 100, [WEAPON])

CHECK_MATERIAL = TableData("Check Material")
CHECK_MATERIAL.add_item("Regular", 1, 80, [WEAPON])
CHECK_MATERIAL.add_item("Altered", 81, 100, [MATERIAL])

LESSER_MINOR = TableData("Lesser Minor Weapon", ext=True, normalize=True)
LESSER_MINOR.add_item("Impervious", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Glamered", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Allying", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Bane", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Benevolent", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Called", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Conductive", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Corrosive", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Countering", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Courageous", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Cruel", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Cunning", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Deadly", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Defending", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Dispelling", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Flaming", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Frost", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Furious", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Ghost touch", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Grayflame", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Grounding", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Guardian", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Heartseeker", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Huntsman", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Jurist", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Keen", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Menacing", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Merciful", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Mighty cleaving", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Mimetic", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Neutralizing", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Ominous", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Planar", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Quenching", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Seaborne", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Shock", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Spell storing", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Thawing", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Throwing", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Thundering", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Valiant", 0, 0, [CHECK_MATERIAL])
LESSER_MINOR.add_item("Vicious", 0, 0, [CHECK_MATERIAL])

PLUS_ONE = TableData("+1", ext=True)
PLUS_ONE.add_item("+1", 1, 100, [CHECK_MATERIAL])

CHECK_LESSER_MINOR = TableData("Check +1")
CHECK_LESSER_MINOR.add_item("+1", 1, 50, [PLUS_ONE])
CHECK_LESSER_MINOR.add_item("Other", 51, 100, [LESSER_MINOR])


MAGIC_WEAPON = TableData("Magic Weapon")
MAGIC_WEAPON.add_item("Lesser Minor Magic", 1, 200, [CHECK_LESSER_MINOR])
MAGIC_WEAPON.add_item("Greater Minor Magic", 201, 400, [])
MAGIC_WEAPON.add_item("Lesser Medium Magic", 401, 600, [])
MAGIC_WEAPON.add_item("Greater Medium Magic", 601, 800, [])
MAGIC_WEAPON.add_item("Lesser Major Magic", 801, 1000, [])
MAGIC_WEAPON.add_item("Greater Major Magic", 1001, 10000, [])

WEAPON_CHECK = TableData("Weapon Magic/Mundane")
WEAPON_CHECK.add_item("Mundane", 1, 90, [CHECK_MATERIAL])
WEAPON_CHECK.add_item("Magic", 91, 100, [MAGIC_WEAPON])
