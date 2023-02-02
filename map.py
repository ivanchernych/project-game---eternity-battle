from item import Item


class Map:
    def __init__(self, number_map=1, *group):
        self.all_sprite_group = group[1]
        self.item_group = group[0]
        self.number_map = number_map

    def statistic(self):
        st = Item(0, 930, 'st')
        self.all_sprite_group.add(st)
        self.item_group.add(st)

    def map1(self):
        x = 0
        for i in range(39):
            pl = Item(x, 0, 'p1')
            self.all_sprite_group.add(pl)
            self.item_group.add(pl)
            x += 50
        x = 0
        for i in range(39):
            pl = Item(x, 780, 'p1')
            self.all_sprite_group.add(pl)
            self.item_group.add(pl)
            x += 50

        y = 50
        for i in range(22):
            pl = Item(0, y, 'p1')
            self.all_sprite_group.add(pl)
            self.item_group.add(pl)
            y += 50

        y = 50
        for i in range(22):
            pl = Item(1870, y, 'p1')
            self.all_sprite_group.add(pl)
            self.item_group.add(pl)
            y += 50

        pl = Item(550, 750, 'p1')
        self.all_sprite_group.add(pl)
        self.item_group.add(pl)

    def map2(self):
        pass

    def draw(self):
        if self.number_map == 1:
            self.map1()
        if self.number_map == 2:
            self.map2()
        self.statistic()
