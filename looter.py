__author__ = 'dmadden'
from argparse import ArgumentParser

from table_data.loot.weapon import CHECK_MATERIAL, MAGIC_WEAPON
from table_data.loot.loot_type import LOOT_TYPE
from table_data.loot.armor import ARMOR, MAGIC_ARMOR
from table_data.loot.equipment import EQUIPMENT
from table_data.loot.gold import GOLD, set_gold_multiplier
from table_data.loot.potion import POTION
from table_data.loot.scroll import SCROLL
from table_data.loot.special import SPECIAL
from loot_table import LootTable


def roll_specific(num, table):
    l = LootTable(table)
    results = []
    for _ in range(num):
        l.recursive_roll(results)
    return results

def roll_main(num):
    return roll_specific(num, LOOT_TYPE)

def print_results(res):
    gold = 0
    for r in res:
        try:
            gold += float(r)
        except:
            print r
    print "{} gold".format(gold)

if __name__ == "__main__":
    parser = ArgumentParser(description="A CLI entrypoint for pathfinder loot tables.")
    parser.add_argument(dest='num_items', action='store', default=1, help="The number of items to be generated.", type=int)
    c = ["weapon", "magic_weapon", "armor", "magic_armor", "potion", "scroll", "equipment", "gold", "special"]
    parser.add_argument("--table", dest="table", action="store", choices=c)
    parser.add_argument("--gold-mult", dest="gold_mult", action="store", default=2.12, type=float)
    args = parser.parse_args()
    table_map = {
        "weapon": CHECK_MATERIAL,
        "magic_weapon": MAGIC_WEAPON,
        "armor": ARMOR,
        "magic_armor": MAGIC_ARMOR,
        "potion": POTION,
        "scroll": SCROLL,
        "equipment": EQUIPMENT,
        "gold": GOLD,
        "special": SPECIAL,
    }
    set_gold_multiplier(args.gold_mult)
    if args.table is not None:
        results = roll_specific(args.num_items, table_map[args.table])
    else:
        results = roll_main(args.num_items)
    print_results(results)
