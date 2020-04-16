from Conversion_matrix_to_PNG import Converter


masX = [
    # {'position': 'x1', 'numbers': [3, 3, 1, 3, 1, 1]},
    # {'position': 'x2', 'numbers': [12, 3, 1, 3, 1]},
    # {'position': 'x3', 'numbers': [8, 4, 1, 3, 1, 1, 1, 1]},
    # {'position': 'x4', 'numbers': [2, 2, 2, 2, 3, 1, 1, 1]},
    # {'position': 'x5', 'numbers': [4, 1, 1, 2, 3, 2, 2, 1]},
    # {'position': 'x6', 'numbers': [7, 2, 1, 3, 2, 5, 1]},
    # {'position': 'x7', 'numbers': [2, 2, 1, 2, 2, 1, 1]},
    # {'position': 'x8', 'numbers': [1, 2, 1, 2, 5, 1, 1]},
    # {'position': 'x9', 'numbers': [1, 2, 5, 4, 3, 2]},
    # {'position': 'x10', 'numbers': [1, 3, 2, 3, 2, 2, 1, 2]},
    # {'position': 'x11', 'numbers': [2, 2, 2, 1, 2, 2, 1, 3]},
    # {'position': 'x12', 'numbers': [1, 1, 1, 2, 1, 1, 1, 2, 2, 3]},
    # {'position': 'x13', 'numbers': [2, 2, 2, 1, 4, 1, 3]},
    # {'position': 'x14', 'numbers': [3, 2, 2, 1, 2, 4]},
    # {'position': 'x15', 'numbers': [2, 2, 2, 4, 1]},
    # {'position': 'x16', 'numbers': [2, 3, 5, 1]},
    # {'position': 'x17', 'numbers': [4, 1, 1, 6, 1, 1]},
    # {'position': 'x18', 'numbers': [8, 6, 1, 1, 1]},
    # {'position': 'x19', 'numbers': [5, 7, 1, 2]},
    # {'position': 'x20', 'numbers': [7, 1, 1, 1, 2]},
    # {'position': 'x21', 'numbers': [1, 13, 1, 1, 5]},
    # {'position': 'x22', 'numbers': [8, 1, 7, 2, 1, 2, 2]},
    # {'position': 'x23', 'numbers': [6, 3, 4, 1, 1, 1, 2]},
    # {'position': 'x24', 'numbers': [1, 1, 1, 2, 4, 1, 1, 1, 2, 2]},
    # {'position': 'x25', 'numbers': [3, 1, 2, 3, 3, 2, 1, 3, 1]},
    # {'position': 'x26', 'numbers': [1, 2, 3, 3, 2, 1, 2, 1]},
    # {'position': 'x27', 'numbers': [1, 2, 6, 3, 2, 3, 1]},
    # {'position': 'x28', 'numbers': [2, 1, 4, 3, 1, 4, 2, 2]},
    # {'position': 'x29', 'numbers': [2, 3, 1, 4, 2, 2]},
    # {'position': 'x30', 'numbers': [6, 1, 4, 5]}
    {'position': 'x1', 'numbers': [3, ]},
    {'position': 'x2', 'numbers': [1, 2]},
    {'position': 'x3', 'numbers': [2, 2]},
    {'position': 'x4', 'numbers': [1, 1]},
    {'position': 'x5', 'numbers': [1, ]}
]
masY = [
    # {'position': 'y1', 'numbers': [2, 5, 2, 2, 2, 3]},
    # {'position': 'y2', 'numbers': [2, 2, 2, 2, 6]},
    # {'position': 'y3', 'numbers': [1, 2, 3, 2, 4, 1]},
    # {'position': 'y4', 'numbers': [2, 2, 2, 2, 2, 2, 3, 1]},
    # {'position': 'y5', 'numbers': [2, 2, 1, 1, 1, 2, 6, 1]},
    # {'position': 'y6', 'numbers': [2, 2, 2, 2, 2, 2, 3]},
    # {'position': 'y7', 'numbers': [2, 3, 3, 2, 9]},
    # {'position': 'y8', 'numbers': [3, 4, 2, 2, 6]},
    # {'position': 'y9', 'numbers': [1, 3, 9, 1, 3]},
    # {'position': 'y10', 'numbers': [2, 3, 6, 4, 1]},
    # {'position': 'y11', 'numbers': [3, 2, 2, 2, 2]},
    # {'position': 'y12', 'numbers': [3, 1, 2, 2, 1, 2, 3, 2]},
    # {'position': 'y13', 'numbers': [2, 1, 2, 2, 3, 2, 1]},
    # {'position': 'y14', 'numbers': [2, 4, 1, 1, 3, 3]},
    # {'position': 'y15', 'numbers': [9, 4, 2]},
    # {'position': 'y16', 'numbers': [1, 3, 6, 5, 6]},
    # {'position': 'y17', 'numbers': [2, 2, 6, 1]},
    # {'position': 'y18', 'numbers': [6, 1, 2, 1, 2, 5]},
    # {'position': 'y19', 'numbers': [6, 2, 1, 2, 1, 2, 3]},
    # {'position': 'y20', 'numbers': [5, 2, 4, 2]},
    # {'position': 'y21', 'numbers': [1, 2, 14]},
    # {'position': 'y22', 'numbers': [5, 2, 3, 1, 6]},
    # {'position': 'y23', 'numbers': [2, 6, 2, 2, 2, 3]},
    # {'position': 'y24', 'numbers': [2, 2, 4, 3, 1, 2, 3]},
    # {'position': 'y25', 'numbers': [3, 2, 4, 1]},
    # {'position': 'y26', 'numbers': [2, 2, 2, 17]},
    # {'position': 'y27', 'numbers': [4, 1, 3, 2, 7]},
    # {'position': 'y28', 'numbers': [1, 1, 4, 5, 1, 1]},
    # {'position': 'y29', 'numbers': [5, 2, 6, 5]},
    # {'position': 'y30', 'numbers': [12, 2, 5, 3]}

    {'position': 'y1', 'numbers': [4, ]},
    {'position': 'y2', 'numbers': [1, ]},
    {'position': 'y3', 'numbers': [1, ]},
    {'position': 'y4', 'numbers': [3, ]},
    {'position': 'y5', 'numbers': [4, ]}
]


class Solver:
    def __init__(self, values_x, values_y):
        self.values_y = values_y
        self.values_x = values_x
        self.zero_matrix = [[0] * len(values_x) for i in values_y]

    def permutations(self, values, row, n=0):
        if values and values[0]:
            current, *other = values
            for i in range(len(row) - sum(other) - len(other) + 1 - current):
                if 1 not in row[i:i + current]:
                    for j in self.permutations(other, row[i + current + 1:], 1):
                        yield [1] * (i + n) + [2] * current + j
        else:
            yield []

    def solve_row(self, values, row):
        valid_permutations = []
        for permutation in self.permutations(values, row):
            permutation += [1] * (len(row) - len(permutation))
            for n1, n2 in zip(row, permutation):
                if n1 > 0 and n1 != n2:
                    break
            else:
                valid_permutations.append(permutation)

        new_row = valid_permutations[0]
        for permutation in valid_permutations[1:]:
            new_row = [n if n == r else 0 for n, r in zip(new_row, permutation)]
        return new_row

    def solve(self):
        changed = True
        while changed:
            changed = False
            for y, row_value in enumerate(self.values_y):
                row = self.solve_row(row_value, self.zero_matrix[y])
                for x, cell in enumerate(row):
                    if cell and self.zero_matrix[y][x] != cell:
                        changed = True
                    self.zero_matrix[y][x] = cell

            for x, col_value in enumerate(self.values_x):
                col = self.solve_row(col_value, [row[x] for row in self.zero_matrix])
                for y, cell in enumerate(col):
                    if cell and self.zero_matrix[y][x] != cell:
                        changed = True
                    self.zero_matrix[y][x] = cell


if __name__ == '__main__':
    result_matrix = Solver(masX, masY)
    result_matrix.solve()

    convert_matrix = Converter(result_matrix.zero_matrix)
    convert_matrix.create_points()

    # work_win = ResultWindow(result_matrix.zero_matrix)
    # work_win.drawing_result_matrix()
