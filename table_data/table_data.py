from __future__ import division
__author__ = 'dmadden'


class TableData:
    class TableItem:

        def __init__(self, name, min, max, next_tables):
            self.name = name
            self.min = min
            self.max = max
            self.next_tables = next_tables

    def __init__(self, name, magic=False, normalize=False, roll_mult=1, final=False):
        self.name = name
        self.items = []
        self.roll_multiplier = roll_mult
        self.magic = magic
        self.normalize = normalize
        self.final = final

    def add_item(self, name, min, max, next_tables):
        self.items.append(TableData.TableItem(name, min, max, next_tables))
        if self.normalize:
            total = len(self.items)
            step = 100/total
            curr = 1
            for i in self.items:
                i.min = curr
                curr += step
                i.max = curr

class GoldData(TableData):

    def __init__(self, multiplier):
        TableData.__init__(self, "Gold", final=True)
        self.multiplier = multiplier

    def add_item(self, amount, min, max, next_tables):
        self.items.append(TableData.TableItem(amount * self.multiplier, min, max, next_tables))