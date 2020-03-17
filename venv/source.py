masX = [
    {'position': 'x1', 'numbers': (2, 1)},
    {'position': 'x2', 'numbers': (1, 2, 3)},
    {'position': 'x3', 'numbers': (9,)},
    {'position': 'x4', 'numbers': (7, 1)},
    {'position': 'x5', 'numbers': (4, 5)},
    {'position': 'x6', 'numbers': (5,)},
    {'position': 'x7', 'numbers': (4,)},
    {'position': 'x8', 'numbers': (2, 1)},
    {'position': 'x9', 'numbers': (1, 2, 2)},
    {'position': 'x10', 'numbers': (4,)}
]
masY = [
    {'position': 'y1', 'numbers': (1, 1)},
    {'position': 'y2', 'numbers': (4,)},
    {'position': 'y3', 'numbers': (1, 3, 1)},
    {'position': 'y4', 'numbers': (5, 1)},
    {'position': 'y5', 'numbers': (3, 2)},
    {'position': 'y6', 'numbers': (4, 2)},
    {'position': 'y7', 'numbers': (5, 1)},
    {'position': 'y8', 'numbers': (6, 1)},
    {'position': 'y9', 'numbers': (2, 3, 2)},
    {'position': 'y10', 'numbers': (2, 6)}
]


class Matrix:

    def __init__(self):
        self.sort_masY = sorted(masY, key=lambda r: sum(r['numbers']) + len(r['numbers']) - 1, reverse=True)
        self.sort_masX = sorted(masX, key=lambda r: sum(r['numbers']) + len(r['numbers']) - 1, reverse=True)
        self.matrix = [[0 for a in masX] for b in masY]

    def print(self):
        for im in self.matrix:
            print(im)


    def fillingIn(self):
        for x in self.sort_masX:
            pass


test = Matrix()
test.print()
test.fillingIn()
