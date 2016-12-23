__author__ = 'dmadden'
from random import randrange


class LootTable:

    class TableItem:

        def __init__(self, min, max, item, next_tables):
            self.min = min
            self.max = max
            self.item = item
            self.next_tables = []
            for td in next_tables:
                self.next_tables.append(LootTable(td))

        def check(self, roll):
            return self.min <= roll <= self.max

        def get_item(self):
            return self.item

        def __str__(self):
            return "{} {} {}".format(self.item, self.min, self.max)

        def __repr__(self):
            return self.__str__()

    def __init__(self, table_data):
        self.items = []
        self.table_name = table_data.name
        self.magic = table_data.magic
        self.final = table_data.final

        for item in table_data.items:
            min = item.min
            max = item.max
            name = item.name
            next_tables = item.next_tables
            self.items.append(LootTable.TableItem(min, max, name, next_tables))

    def roll_magic(self, container):
        r = randrange(1, 100)
        for item in self.items:
            if item.check(r):
                name = item.get_item()
                temp_table = item.next_tables[0]
                name += " " + temp_table.roll_for_name()
                container.append(name)

    def roll_for_name(self):
        r = randrange(1, 100)
        for item in self.items:
            if item.check(r):
                return item.get_item()

    def roll(self, container):
        print "ROLLING: {}".format(self.table_name)
        r = randrange(1, 100)
        for item in self.items:
            if item.check(r):
                if not self.magic and self.final:
                    container.append(item.get_item())
                elif self.magic:
                    self.roll_magic(container)
                else:
                    for table in item.next_tables:
                        table.roll(container)



