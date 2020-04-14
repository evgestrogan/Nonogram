from tkinter import *


class MainUI(Tk):

    def take_size_rectangle(self, entry, window):
        self.size_rectangle = entry.get()
        self.create_matrix_frame()
        window.destroy()

    def create_second_window(self):
        window = Toplevel(self)
        data = IntVar()
        Entry(window, textvariable=data).grid(column=0, row=0)
        Button(window, text='Input size', command=lambda: self.take_size_rectangle(data, window)).grid(column=1, row=0)
        window.mainloop()

    def __init__(self):
        Tk.__init__(self)
        self.resizable(height=False, width=False)
        self.size_rectangle = 0
        self.side_length = 22

        """Menu bar"""
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Create work window", command=self.create_second_window)
        filemenu.add_command(label="Open saved nonogram", command=self.get_values)
        filemenu.add_command(label="Save nonogram", command=self.create_matrix_frame)
        filemenu.add_command(label="Solver nonogram", command=self.create_matrix_frame)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.destroy)
        menubar.add_cascade(label="File", menu=filemenu)
        self.config(menu=menubar)
        """End menu bar"""

        self.container = Frame(self, width=100, height=100)
        self.container.pack(fill=BOTH, expand=True)

    def create_matrix_frame(self):
        self.x_value = InputFrame(self.container, self.size_rectangle, 'top')
        self.x_value.grid(row=0, column=1, sticky="nsew")
        self.y_value = InputFrame(self.container, self.size_rectangle, 'left')
        self.y_value.grid(row=1, column=0, sticky="nsew")
        MatrixFrame(self.container, self.size_rectangle, self.side_length).grid(row=1, column=1, sticky="nsew")

    def get_values(self):
        self.y_value.take_input_value()
        self.x_value.take_input_value()


class MatrixFrame(Frame):

    def __init__(self, parent, size_rectangle, side_length):
        Frame.__init__(self, parent)
        start_x = start_y = 0
        self.canvas = Canvas(self, width=side_length * size_rectangle,
                             height=side_length * size_rectangle)
        for row in range(size_rectangle):
            for column in range(size_rectangle):
                CreateCanvasSquare(self.canvas, start_x, start_y, side_length, 'white')
                start_x += side_length
            start_y += side_length
            start_x = 0
        self.canvas.grid(row=0, column=0, sticky="ew")


class InputFrame(Frame):

    def __init__(self, parent, size_rectangle, pos):
        Frame.__init__(self, parent)
        self.list_entry = []
        self.entry = None
        for numb in range(size_rectangle):
            if pos == 'top':
                self.list_entry.append(CreateInput(self, 2, 7, 0, numb, font="Courier 10"))
            elif pos == 'left':
                self.list_entry.append(CreateInput(self, 16, 1, numb, 0, font="Courier 10"))

    def take_input_value(self):
        for entry in self.list_entry:
            entry.take_values_text()


class CreateCanvasSquare:
    def __init__(self, master, start_x, start_y, size_square, color):
        self.master = master
        self.square = self.master.create_rectangle(start_x, start_y, start_x + size_square, start_y + size_square,
                                                   fill=color)
        self.master.tag_bind(self.square, '<Button-1>', self.move)

    def move(self, event):
        self.master.itemconfig(self.square, fill='red')


class CreateInput(Text):
    def __init__(self, master, width, height, row, column, font="Courier 10"):
        Text.__init__(self, master, width=width, height=height, font=font)
        self.row = row
        self.column = column
        self.grid(row=self.row, column=self.column)

    def take_values_text(self):
        print('{}:{} - {}'.format(self.row, self.column, self.get("1.0", END)))


MainUIobj = MainUI()
MainUIobj.mainloop()
