import os

from table_data.table_data import TableData

dir_path = os.path.dirname(os.path.realpath(__file__))

EQUIPMENT = TableData("Equipment", ext=True, final=True, normalize=True)
with open(dir_path + "/equipment_list", "r") as f:
    for line in f.readlines():
        EQUIPMENT.add_item(line.replace("\n", ""), 0, 0, [])
