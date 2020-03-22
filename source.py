import numpy as np

masX = np.array([
    # {'position': 'x1', 'numbers': (2, 1)},
    # {'position': 'x2', 'numbers': (1, 2, 3)},
    # {'position': 'x3', 'numbers': (9,)},
    # {'position': 'x4', 'numbers': (7, 1)},
    # {'position': 'x5', 'numbers': (4, 5)},
    # {'position': 'x6', 'numbers': (5,)},
    # {'position': 'x7', 'numbers': (4,)},
    # {'position': 'x8', 'numbers': (2, 1)},
    # {'position': 'x9', 'numbers': (1, 2, 2)},
    # {'position': 'x10', 'numbers': (4,)}
    {'position': 'x1', 'numbers': (3,)},
    {'position': 'x2', 'numbers': (1, 2)},
    {'position': 'x3', 'numbers': (2, 2)},
    {'position': 'x4', 'numbers': (1, 1)},
    {'position': 'x5', 'numbers': (1,)}
])
masY = np.array([
    # {'position': 'y1', 'numbers': (1, 1)},
    # {'position': 'y2', 'numbers': (4,)},
    # {'position': 'y3', 'numbers': (1, 3, 1)},
    # {'position': 'y4', 'numbers': (5, 1)},
    # {'position': 'y5', 'numbers': (3, 2)},
    # {'position': 'y6', 'numbers': (4, 2)},
    # {'position': 'y7', 'numbers': (5, 1)},
    # {'position': 'y8', 'numbers': (6, 1)},
    # {'position': 'y9', 'numbers': (2, 3, 2)},
    # {'position': 'y10', 'numbers': (2, 6)}
    {'position': 'y1', 'numbers': (4,)},
    {'position': 'y2', 'numbers': (1,)},
    {'position': 'y3', 'numbers': (1,)},
    {'position': 'y4', 'numbers': (3,)},
    {'position': 'y5', 'numbers': (4,)}
])


class Matrix:

    def __init__(self, values_x, values_y):
        self.values_y = values_y
        self.values_x = values_x
        self.zero_matrix = np.zeros((len(self.values_x), len(self.values_y)), int)
        self.create_result(self.values_y)
        self.create_result(self.values_x)

    def end_point(self, line):
        for pos, x in enumerate(line):
            if int(x) == 0:
                line[pos] = 0

    def print_matrix(self):
        for im in self.zero_matrix:
            print(im)
        print('-' * 30)

    def take_position(self, position):
        position_number = int(position[1:]) - 1
        return position_number

    def create_result(self, values):
        for value in values:
            position_number = self.take_position(value['position'])  # номер строки или столбца
            del_number = len(values) - (sum(value['numbers']) + len(
                value['numbers']) - 1)  # количество нулей которое будет в конце, кол-во единиц которые нужно удалить
            if value['position'][0] == 'y':
                zero_line = self.zero_matrix[position_number]
            else:
                zero_line = self.zero_matrix.transpose()[position_number]
            step = 0
            for number in value['numbers']:
                if number > del_number:
                    for a in range(del_number):
                        step += 1
                    for a in range(number - del_number):
                        zero_line[step] = 1
                        step += 1
                    step += 1
                else:
                    for a in range(number):
                        step += 1
                    step += 1
            if sum(zero_line) == sum(value['numbers']):
                self.end_point(zero_line)


if __name__ == '__main__':
    result_matrix = Matrix(masX, masY)
    result_matrix.print_matrix()
