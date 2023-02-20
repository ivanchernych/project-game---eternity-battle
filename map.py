from item import Item
import sqlite3


class Map:
    def __init__(self, number_map, item_group, all_sprite_group):
        self.all_sprite_group = all_sprite_group
        self.item_group = item_group
        self.number_map = number_map

    def statistic(self):
        statistics = Item(0, 750, 'statistics')
        self.all_sprite_group.add(statistics)
        self.item_group.add(statistics)

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
            for block in range(34):
                x += 50
                if line[block] == 'x':
                    pl = Item(x, y, 'platform')
                    self.all_sprite_group.add(pl)
                    self.item_group.add(pl)
        cur.close()

    def draw(self):
        self.map()
        self.statistic()
