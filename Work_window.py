from tkinter import Tk, Canvas


class ResultWindow:
    def __init__(self, matrix):
        self.matrix = matrix
        self._root = Tk()
        self._c = Canvas(self._root, width=len(self.matrix.values_x) * 20, height=len(self.matrix.values_y) * 20,
                         bg='white')
        self._size_rectangle = 20

    def draw_raw(self, raw, start_y, end_y):
        start_x = 0
        end_x = self._size_rectangle
        for value in raw:
            if value == 2:
                self._c.create_rectangle(start_x, start_y, end_x, end_y, fill='red')
            else:
                self._c.create_rectangle(start_x, start_y, end_x, end_y)
            start_x += self._size_rectangle
            end_x += self._size_rectangle

    def drawing_result_matrix(self):
        self._c.pack()
        start_y = 0
        end_y = self._size_rectangle
        for raw in self.matrix.zero_matrix:
            self.draw_raw(raw, start_y, end_y)
            start_y += self._size_rectangle
            end_y += self._size_rectangle
        self._root.mainloop()
