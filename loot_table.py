__author__ = 'dmadden'
from random import randrange


class LootTable:

    class TableItem:

        def __init__(self, min, max, item):
            self.min = min
            self.max = max
            self.item = item

        def check(self, roll):
            return self.min <= roll <= self.max

        def get_item(self):
            return self.item

    def __init__(self, table_data, multiplier):
        self.items = []
        self.table_name = table_data["name"]
        self.multiplier = multiplier

        for item in table_data["items"]:
            min = item["roll_range"][0]
            max = item["roll_range"][1]
            name = item["name"]
            self.items.append(LootTable.TableItem(min, max, name))

    def roll(self):
        r = randrange(1, 100) * self.multiplier
        for item in self.items:
            if item.check(r):
                return item.get_item()
