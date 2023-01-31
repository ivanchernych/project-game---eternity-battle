from item import Item


class Map:
    def __init__(self, number_map, *group):
        self.all_sprite_group = group[1]
        self.platform_sprite_group = group[0]
        self.number_map = number_map
        print(group[1], group[0])

    def statistic(self):
        st = Item(0, 930, 'st')
        self.all_sprite_group.add(st)
        self.platform_sprite_group.add(st)

    def map1(self):
        x = 0
        for i in range(10):
            pl = Item(x, 0, 'p1')
            self.all_sprite_group.add(pl)
            self.platform_sprite_group.add(pl)
            x += 192
        x = 0
        for i in range(10):
            pl = Item(x, 880, 'p1')
            self.all_sprite_group.add(pl)
            self.platform_sprite_group.add(pl)
            x += 192

        y = 50
        for i in range(5):
            pl = Item(0, y, 'p2')
            self.all_sprite_group.add(pl)
            self.platform_sprite_group.add(pl)
            y += 196

        y = 50
        for i in range(5):
            pl = Item(1870, y, 'p2')
            self.all_sprite_group.add(pl)
            self.platform_sprite_group.add(pl)
            y += 196

    def map2(self):
        pass

    def draw(self):
        if self.number_map == 1:
            self.map1()
        if self.number_map == 2:
            self.map2()
        self.statistic()
