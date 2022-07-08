import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.assembleWidgets()

    def assembleWidgets(self):

        self.figure = Figure()
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self, pack_toolbar=False)

        self.btn_start = tk.Button(self, text="Start")
        self.btn_stop = tk.Button(self, text="Stop")

        self.canvas.get_tk_widget().grid(row=0,column=0)
        self.toolbar.grid(row=1,column=0)
        self.btn_start.grid(row=1,column=1)
        self.btn_stop.grid(row=1,column=2)

        self.axes = self.figure.add_subplot(111)
        self.axes.set_ylim(0,1)

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.pack(fill="both", expand=True)
    root.mainloop()
