__author__ = 'dmadden'
from table_data.weapon import WEAPON, MAGIC_WEAPON
from table_data.loot_type import LOOT_TYPE
from loot_table import LootTable



if __name__ == "__main__":
    l = LootTable(LOOT_TYPE)
    results = []
    for _ in range(10):
        l.roll(results)
    gold = 0
    for r in results:
        if isinstance(r, int):
            gold += r
        else:
            print r
    print "and {} gold".format(gold)