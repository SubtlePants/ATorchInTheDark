from Item import *


# returns a dictionary of all items in CSV (lies, semi-colon separated) file, item name is the key
def readitems(file):
    items = {}
    with open(file, "r") as filestream:
        next(filestream)
        for line in filestream:
            line.strip()
            currentline = line.split(';')
            items.update({currentline[0].lower(): Item(currentline[0], int(currentline[1]), currentline[2])})

    return items

