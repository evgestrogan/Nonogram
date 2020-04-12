from tkinter import *


class CreateCanvasSquare:
    def __init__(self, master, start_x, start_y, size_square, color):
        self.master = master
        self.square = self.master.create_rectangle(start_x, start_y, start_x + size_square, start_y + size_square,
                                                   fill=color)
        self.master.tag_bind(self.square, '<Button-1>', self.move)

    def move(self, event):
        self.master.itemconfig(self.square, fill='red')


class CreateInput:
    def __init__(self, master, numb):
        self.numb = numb
        self.master = master

    def create_entry_widget(self):
        ent = Entry(self.master, font="Courier 10", justify=RIGHT)
        ent.bind("<Return>", (lambda event: self.take_values(ent.get(), self.numb)))
        ent.grid(row=self.numb, column=0)

    def create_text_widget(self):
        ent = Text(self.master, width=2, font="Courier 10", height=8)
        ent.bind("<Return>", (lambda event: self.take_values(ent.get("1.0", END), self.numb)))
        ent.grid(row=0, column=self.numb)

    def take_values(self, text, numb):
        print(str(numb) + ':' + text)
