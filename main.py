#!/usr/bin/env python3

import tkinter as tk
import tkinter.ttk as ttk

import matplotlib
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure

import math
from IPython import embed

matplotlib.use('TkAgg')


class Grapher(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.figure = Figure(figsize=(49.7 / 6, 23 / 6), dpi=100)
        self.sub = self.figure.add_subplot(111)
        self.sub.plot(
            [x / 10 for x in range(0, 50)],
            [math.sin(x / 10) for x in range(0, 50)]
        )
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(
            side=tk.BOTTOM, fill=tk.BOTH, expand=True
        )

        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # print(self.canvas.get_tk_widget()['offset'])
        print('\n'.join(f'{str(k)}: {str(v)}' for k, v in
                        self.canvas.get_tk_widget().config().items()))


if __name__ == '__main__':
    root = tk.Tk()
    grapher = Grapher(root)
    grapher.pack()
    # root.mainloop()
    embed()
