__author__ = 'dmadden'
from random import randrange


class LootTable:

    class TableItem:

        def __init__(self, min, max, item, next_tables):
            self.min = min
            self.max = max
            self.item = item
            self.next_tables = next_tables

        def check(self, roll):
            return self.min <= roll <= self.max

        def get_item(self):
            return self.item

    def __init__(self, table_data):
        self.items = []
        self.table_name = table_data.name
        self.magic = table_data.magic

        for item in table_data.items:
            min = item.min
            max = item.max
            name = item.name
            next_tables = item.next_tables
            self.items.append(LootTable.TableItem(min, max, name, next_tables))

    def roll_magic(self):
        r = randrange(1, 100)
        for item in self.items:
            if item.check(r):
                temp_table = LootTable()

    def roll(self):
        if self.magic:
            name = self.roll_magic() + " "
        r = randrange(1, 100)
        for item in self.items:
            if item.check(r):
                return item.get_name()
