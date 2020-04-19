class Solver:
    def __init__(self, values, zero_matrix):
        self.values_x, self.values_y = values
        self.zero_matrix = zero_matrix
        self.solve()

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
