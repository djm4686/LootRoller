from gold import GOLD
from item import ITEM
from table_data import TableData


LOOT_TYPE = TableData("Loot Type")
LOOT_TYPE.add_item("Gold", 1, 30, [GOLD])
LOOT_TYPE.add_item("Item", 31, 70, [ITEM])
LOOT_TYPE.add_item("Both", 71, 100, [GOLD, ITEM])

