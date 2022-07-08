import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import nidaqmx_machine
import time

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("nidaqmx gui test")
        self.fig = Figure()
        # Figure pre configuration
        self.sampling_time = .25
        self.n = 100
        self.x_len = self.n
        self.v_min = 0
        self.v_max = .1
        self.y_range = [self.v_min, self.v_max]
        # Configure figure
        self.ax = self.fig.add_subplot(111)
        self.xs = list(range(0, self.n))
        self.ys = [0]*self.x_len
        self.ax.set_ylim(self.y_range)
        self.line, = self.ax.plot(self.xs, self.ys)
        # Grid figure
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.get_tk_widget().grid(row=0, column=0)
        # Grid buttons
        self.btn_start = tk.Button(self, text="Start")
        self.btn_stop = tk.Button(self, text="Stop")
        self.btn_quit = tk.Button(self, text="Quit", command=self.quit)
        self.btn_start.grid(row=1, column=1)
        self.btn_stop.grid(row=1, column=2)
        self.btn_quit.grid(row=2, column=1)
        self.ani = animation.FuncAnimation(self.fig, nidaqmx_machine.logging, fargs=(
        self.ys, self.sampling_time, self.line, self.x_len,))

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.pack(fill="both", expand=True)
    root.mainloop()
