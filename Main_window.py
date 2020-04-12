from Event_handler import *


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
        filemenu.add_command(label="Open saved nonogram", command=self.create_matrix_frame)
        filemenu.add_command(label="Save nonogram", command=self.create_matrix_frame)
        filemenu.add_command(label="Solver nonogram", command=self.create_matrix_frame)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.destroy)
        menubar.add_cascade(label="File", menu=filemenu)
        self.config(menu=menubar)
        """End menu bar"""

        self.container = Frame(self, width=100, height=100)
        self.container.pack(fill=BOTH, expand=True)
        self.frameslist = {}

    def create_matrix_frame(self):
        for column, F in enumerate((ButtonFrame, TopInputFrame, LeftInputFrame, MatrixFrame)):
            frame = F(self.container, self.size_rectangle, self.side_length)
            frame.grid(row=column // 2, column=column % 2, sticky="nsew")
            self.frameslist[F] = frame

        self.show_frame(MatrixFrame)
        self.show_frame(LeftInputFrame)
        self.show_frame(TopInputFrame)
        self.show_frame(ButtonFrame)

    def show_frame(self, cont):
        frame = self.frameslist[cont]
        frame.tkraise()


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


class LeftInputFrame(Frame):

    def __init__(self, parent, size_rectangle, side_length):
        Frame.__init__(self, parent)
        for row in range(size_rectangle):
            CreateInput(self, row).create_entry_widget()


class TopInputFrame(Frame):

    def __init__(self, parent, size_rectangle, side_length):
        Frame.__init__(self, parent)
        for row in range(size_rectangle):
            CreateInput(self, row).create_text_widget()


class ButtonFrame(Frame):

    def __init__(self, parent, size_rectangle, side_length):
        Frame.__init__(self, parent)


MainUIobj = MainUI()
MainUIobj.mainloop()
