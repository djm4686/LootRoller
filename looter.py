__author__ = 'dmadden'
from table_data.weapon import WEAPON
from loot_table import LootTable



if __name__ == "__main__":
    l = LootTable(WEAPON)
    for _ in range(10):
        print l.roll()
