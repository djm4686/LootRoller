import os

from table_data.table_data import TableData

dir_path = os.path.dirname(os.path.realpath(__file__))

SCROLL = TableData("Scroll", ext=True, normalize=True, final=True)
with open(dir_path + "/spells1-3", "r") as f:
    for line in f.readlines():
        SCROLL.add_item("Scroll of {}".format(line.replace("\n", "")), 0, 0, [])
