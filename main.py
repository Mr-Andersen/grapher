#!/usr/bin/env python3

import tkinter as tk
from tkinter import font

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy
from math import *

matplotlib.use('TkAgg')


def blink(widget):
    bg = widget['bg']
    # widget['foreground'] = 'red'
    widget.config(bg='#e00')
    widget.after(
        750, lambda: widget.config(bg=bg)
    )


class FuncEntry(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Graph')
        self.resizable(False, False)
        self.entry = tk.Entry(
            self, foreground='#151515', background='white',
            font=font.Font(
                family='Courier', size=24, weight='bold'
            )
        )
        self.left_var = tk.StringVar(value='-10')
        self.left = tk.Entry(
            self, foreground='#151515', background='white',
            font=font.Font(
                family='Courier', size=24, weight='bold'
            ), textvariable=self.left_var, width=4
        )
        self.right_var = tk.StringVar(value='10')
        self.right = tk.Entry(
            self, foreground='#151515', background='white',
            font=font.Font(
                family='Courier', size=24, weight='bold'
            ), textvariable=self.right_var, width=4
        )
        self.entry.bind('<Return>', self.spawn_grapher)
        self.left.bind('<Return>', self.spawn_grapher)
        self.right.bind('<Return>', self.spawn_grapher)
        self.entry.grid(row=0, column=0, columnspan=2, ipadx=10, ipady=10,
                        sticky='ew')
        self.left.grid(row=1, column=0, ipadx=10, ipady=10, sticky='ew')
        self.right.grid(row=1, column=1, ipadx=10, ipady=10, sticky='ew')
        self.entry.focus()

    def spawn_grapher(self, event):
        L = self.left_var.get()
        if not L.isdigit() and\
           (len(L) == 0 or not L[0] == '-' or not L[1:].isdigit()):
            blink(self.left)
            return
        R = self.right_var.get()
        if not R.isdigit() and\
           (len(R) == 0 or not R[0] == '-' or not R[1:].isdigit()):
            blink(self.right)
            return
        try:
            Grapher(
                eval(f'lambda x: {self.entry.get()}'),
                x_lim=(int(self.left.get()), int(self.right.get())),
                title=self.entry.get()
            )
        except SyntaxError:
            blink(self.entry)


class Grapher(tk.Toplevel):
    def __init__(self, func, x_lim=(-10, 10), y_lim=None,
                 dpi=100, title=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if title is not None:
            self.title(title)
        self.resizable(False, False)
        figure = Figure(figsize=(6, 4), dpi=dpi)
        sub = figure.add_subplot(1, 1, 1)
        xs = numpy.arange(*x_lim, 1 / dpi)
        ys = [func(x) for x in xs]
        sub.plot(xs, ys)
        figure.axes[0].set_xlim(*x_lim)
        if y_lim is not None:
            self.figure.axes[0].set_ylim(*y_lim)

        canvas = FigureCanvasTkAgg(figure, self)
        canvas.draw()
        canvas.get_tk_widget().pack(
            side=tk.BOTTOM, fill=tk.BOTH, expand=True
        )


if __name__ == '__main__':
    func_entry = FuncEntry()
    # grapher = Grapher(math.sin)
    func_entry.mainloop()
