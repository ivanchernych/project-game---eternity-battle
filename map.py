from item import Item
import sqlite3


class Map:
    def __init__(self, number_map, *group):
        self.all_sprite_group = group[1]
        self.item_group = group[0]
        self.number_map = number_map

    def statistic(self):
        st = Item(0, 750, 'st')
        self.all_sprite_group.add(st)
        self.item_group.add(st)

    def map(self):
        con = sqlite3.connect('cards.db')
        cur = con.cursor()
        y = -50
        for row in range(1, 16):
            x = -50
            y += 50
            line = cur.execute("""SELECT * FROM cards
            WHERE name_map = ? AND row = ? """, (self.number_map, row)).fetchall()
            line = line[0][2:]
            for c in range(34):
                x += 50
                if line[c] == 'x':
                    pl = Item(x, y, 'p1')
                    self.all_sprite_group.add(pl)
                    self.item_group.add(pl)
        cur.close()

    def draw(self):
        self.map()
        self.statistic()
