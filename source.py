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

    def __init__(self, values_x, values_y):
        self.values_y = sorted(values_y, key=lambda r: sum(r['numbers']) + len(r['numbers']) - 1, reverse=True)
        self.values_x = sorted(values_x, key=lambda r: sum(r['numbers']) + len(r['numbers']) - 1, reverse=True)
        self.zero_matrix = [[0 for a in self.values_x] for b in self.values_y]

    def print_matrix(self):
        for im in self.zero_matrix:
            print(im)

    def filling_in(self):
        pass


if __name__ == '__main__':
    result_matrix = Matrix(masX, masY)
    result_matrix.print_matrix()
    result_matrix.filling_in()
