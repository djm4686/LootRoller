__author__ = 'dmadden'
from random import randrange, choice


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
        self.ext = table_data.ext
        self.final = table_data.final

        for item in table_data.items:
            min = item.min
            max = item.max
            name = item.name
            next_tables = item.next_tables
            self.items.append(LootTable.TableItem(min, max, name, next_tables))

    def recursive_roll(self, container, name=""):
        item = None
        if len(self.items) > 100:
            item = choice(self.items)
        else:
            r = randrange(1, 100)
            for i in self.items:
                if i.check(r):
                    item = i
        if item is None:
            return
        if self.ext:
            name += " " + str(item.get_item())
        if self.final:
            container.append(name)
        for n in item.next_tables:
            n.recursive_roll(container, name)



    def roll_ext(self, container, name=""):
        r = randrange(1, 100)
        if len(self.items) > 100:
            item = choice(self.items)
            name = item.get_item()
            temp_table = item.next_tables[0]
            name += " " + temp_table.roll_for_name()
            container.append(name)
        else:
            for item in self.items:
                if item.check(r):
                    name = item.get_item()
                    temp_table = item.next_tables[0]
                    name += " " + temp_table.roll_for_name()
                    container.append(name)

    def roll_for_name(self):
        if len(self.items) > 100:
            return choice(self.items).get_item()
        r = randrange(1, 100)
        for item in self.items:
            if item.check(r):
                return item.get_item()

    def roll(self, container, name=""):
        if len(self.items) > 100:
            if not self.ext and self.final:
                choice(self.items)
            elif self.ext:
                self.roll_ext(container)
            else:
                for table in choice(self.items).next_tables:
                    table.roll(container)
        else:
            r = randrange(1, 100)
            for item in self.items:
                if item.check(r):
                    if not self.ext and self.final:
                        container.append(item.get_item())
                    elif self.ext:
                        self.roll_ext(container)
                    else:
                        for table in item.next_tables:
                            table.roll(container)



