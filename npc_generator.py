__author__ = 'dmadden'
from subprocess import check_output
from random import randrange
import os


dir_path = os.path.dirname(os.path.realpath(__file__))

class NPC(object):

    def __init__(self, name, cls, race, backstory=""):
        self.name = name
        self.cls = cls
        self.race = race
        self.backstory = backstory
        self.weapons = []
        self.armor = []
        self.gold = 0
        self.generate_weapons()
        self.generate_armor()
        self.generate_gold()

    def __str__(self):
        s = "\n{} the {} {}\n".format(self.name, self.race, self.cls)
        s += "WEAPONS: {}\n".format(self.weapons)
        s += "ARMOR: {}\n".format(self.armor)
        s += "GOLD: {}\n".format(self.gold)
        return s

    def __repr__(self):
        return self.__str__()

    def generate_weapons(self, max_weaps=3):
        self.weapons = [w.lstrip(" ") for w in check_output("python {}/looter.py {} --table weapon".format(dir_path, randrange(1, max_weaps)), shell=True).split("\n") if "gold" not in w and w != '']


    def generate_armor(self):
        self.armor = [a.lstrip(" ") for a in check_output("python {}/looter.py {} --table armor".format(dir_path, 1), shell=True).split("\n") if "gold" not in a and a != '']

    def generate_gold(self, mult=1.2843):
        self.gold = check_output("python {}/looter.py {} --table gold --gold-mult {}".format(dir_path, randrange(1, 2), mult), shell=True).rstrip("\n")



if __name__ == "__main__":
    from name_generator import gen_name
    from argparse import ArgumentParser
    from table_data.npc.cls import CLASS
    from table_data.npc.race import RACE
    from loot_table import LootTable

    print dir_path
    clt = LootTable(CLASS)
    rlt = LootTable(RACE)
    parser = ArgumentParser(description="The CLI entrypoint for creating NPCs")
    parser.add_argument("-n", dest="num", default=1, action="store", type=int)
    args = parser.parse_args()
    for name in gen_name(args.num):
        print NPC(name, clt.roll_for_name(), rlt.roll_for_name())