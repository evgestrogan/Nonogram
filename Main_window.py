from tkinter import *

from Conversion_matrix_to_PNG import Converter
from Nonogram_solver import Solver


class MainUI(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.resizable(height=False, width=False)
        self.filename = ''
        self.side_length = 22
        self.result_matrix = []

        """Menu bar"""
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Create work window", command=lambda: self.create_second_window('Input size'))
        filemenu.add_command(label="Solver nonogram", command=self.solution_nonogram)
        filemenu.add_command(label="Save nonogram", command=lambda: self.create_second_window('Input file name'))
        filemenu.add_command(label="Open nonogram", command=lambda: self.create_second_window('Select file'))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.destroy)
        menubar.add_cascade(label="File", menu=filemenu)
        self.config(menu=menubar)
        """End menu bar"""

        self.container = Frame(self, width=100, height=100)
        self.container.pack(fill=BOTH, expand=True)

        self.square_matrix = None
        self.y_value = None
        self.x_value = None

    def take_input_value(self, entry, window, text):
        input_value = entry.get()
        if text == 'Input size':
            self.result_matrix = [[0] * int(input_value) for i in range(int(input_value))]
            self.create_matrix_frame()
        elif text == 'Input file name':
            self.filename = input_value + '.txt'
            self.save_values()
        elif text == 'Select file':
            self.filename = input_value
            self.open_nonogram()
        window.destroy()

    def create_second_window(self, text):
        import os
        window = Toplevel(self)
        data = Entry(window)
        data.grid(column=0, row=0)
        Button(window, text=text, command=lambda: self.take_input_value(data, window, text)).grid(column=1, row=0)
        if text == 'Select file':
            def set_text(event):
                data.delete(0, END)
                data.insert(0, lbox.get(lbox.curselection()[0]))
                return

            lbox = Listbox(window)
            lbox.grid(row=2, columnspan=2)
            for item in os.listdir():
                if item.endswith('.txt'):
                    lbox.insert(END, item)
            lbox.bind("<<ListboxSelect>>", set_text)
        window.mainloop()

    def create_matrix_frame(self):
        size_rectangle = len(self.result_matrix)
        self.square_matrix = MatrixFrame(self.container, size_rectangle, self.side_length)
        self.y_value = InputFrame(self.container, size_rectangle, 'left')
        self.x_value = InputFrame(self.container, size_rectangle, 'top')
        self.x_value.grid(row=0, column=1, sticky="nsew")
        self.y_value.grid(row=1, column=0, sticky="nsew")
        self.square_matrix.grid(row=1, column=1, sticky="nsew")

    def solution_nonogram(self):
        solver = Solver([self.x_value.take_input_value(), self.y_value.take_input_value()], self.result_matrix)
        self.result_matrix = solver.zero_matrix
        Converter(self.result_matrix)
        self.print_square()

    def print_square(self):
        for itemls_valuels in zip(self.result_matrix, self.square_matrix.square_list):
            for item_value in zip(itemls_valuels[0], itemls_valuels[1]):
                if item_value[0] == 2:
                    item_value[1].move(None)
                elif item_value[0] == 1:
                    item_value[1].clear()

    def save_values(self):
        import json
        self.create_result_matrix()
        with open(self.filename, 'w') as fp:
            json.dump([self.x_value.take_input_value(), self.y_value.take_input_value(), self.result_matrix], fp)

    def create_result_matrix(self):
        for x, row in enumerate(self.square_matrix.square_list):
            for y, obj in enumerate(row):
                self.result_matrix[x][y] = obj.button_state

    def open_nonogram(self):
        import json
        with open(self.filename, 'r') as fp:
            x_val, y_val, self.result_matrix = json.load(fp)
        self.create_matrix_frame()
        self.print_square()
        for item_value in zip(x_val, self.x_value.list_entry):
            for item in item_value[0]:
                item_value[1].insert(END, str(item) + '\n')
        for item_value in zip(y_val, self.y_value.list_entry):
            item_value[1].delete(END, END)
            item_value[1].insert(END, item_value[0])

class MatrixFrame(Frame):

    def __init__(self, parent, size_rectangle, side_length):
        Frame.__init__(self, parent)
        start_x = start_y = 0
        self.canvas = Canvas(self, width=side_length * size_rectangle,
                             height=side_length * size_rectangle)
        self.square_list = []
        for row in range(size_rectangle):
            self.square_list.append([])
            for column in range(size_rectangle):
                self.square_list[row].append(CreateCanvasSquare(self.canvas, start_x, start_y, side_length, 'white'))
                start_x += side_length
            start_y += side_length
            start_x = 0
        self.canvas.grid(row=0, column=0, sticky="ew")


class InputFrame(Frame):

    def __init__(self, parent, size_rectangle, pos):
        Frame.__init__(self, parent)
        self.list_entry = []
        if pos == 'top':
            for numb in range(size_rectangle):
                self.list_entry.append(CreateInput(self, 2, 7, 0, numb))
        elif pos == 'left':
            for numb in range(size_rectangle):
                self.list_entry.append(CreateInput(self, 16, 1, numb, 0))

    def take_input_value(self):
        return [entry.take_values_text() for entry in self.list_entry]


class CreateCanvasSquare:
    def __init__(self, master, start_x, start_y, size_square, color):
        self.master = master
        self.square = self.master.create_rectangle(start_x, start_y, start_x + size_square, start_y + size_square,
                                                   fill=color)
        self.master.tag_bind(self.square, '<Button-1>', self.move)
        self.button_state = 1

    def move(self, event):
        self.master.itemconfig(self.square, fill='black')
        self.button_state = 2

    def clear(self):
        self.master.itemconfig(self.square, fill='white')


class CreateInput(Text):
    def __init__(self, master, width, height, row=0, column=0):
        Text.__init__(self, master, width=width, height=height, font="Courier 10")
        self.row = row
        self.column = column
        self.grid(row=self.row, column=self.column)

    def take_values_text(self):
        return [int(s) for s in self.get("1.0", END).split() if s.isdigit()]


if __name__ == "__main__":
    MainUIobj = MainUI()
    MainUIobj.mainloop()
