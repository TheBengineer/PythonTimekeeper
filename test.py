__author__ = 'boh01'

from threading import Thread
import Tkinter as tk
import ttk

class asdf(Thread):
    def __init__(self):
        Thread.__init__(self)

        self.window = tk.Tk()  # Init
        self.window.geometry("900x800+300+300")
        self.window.title("Time Tracker - Ben Holleran June 2015")
        self.window.protocol("WM_DELETE_WINDOW", self.window.destroy)

        # Variables

        self.timer = 5 * 60
        self.jobs = []



        # Window
        self.nb =  ttk.Notebook(self.window, width=800, height=800)
        self.nb.enable_traversal()
        self.graph_frame = ttk.Frame(self.nb, name='graph')
        self.graph_frame2 = ttk.Frame(self.nb, name='graph2')
        self.time_frame = ttk.Frame(self.nb, name='time')
        self.nb.add(self.graph_frame, text="asdf")
        self.nb.add(self.graph_frame2, text="asdf2")
        self.nb.pack(fill=tk.BOTH, expand=tk.Y, padx=2, pady=3)

        #self.main_frame = tk.Frame(self.window)
        #self.main_frame.pack(fill=tk.BOTH, expand=1)

        #self.menu_frame = tk.Frame(self.main_frame)  # holds the buttons at the top

        #self.poll_button = tk.Button(self.main_frame, text="Scan VIS")
        #self.menu_frame.pack(side="top", expand=1)

        self.graph_canvas = tk.Canvas(width=800, height=800)
        self.graph_canvas.pack()

        #self.nb =  ttk.Notebook(self.window, name='notebook')
        #self.nb.enable_traversal()
        #self.nb.pack(fill=tk.BOTH, expand=tk.Y, padx=2, pady=3)
        # self.graph_frame = ttk.Frame(self.nb, name='graph')
        # self.time_frame = ttk.Frame(self.nb, name='time')

    def run(self):
        #self.window.mainloop()
        pass


a = asdf()
a.start()
a.window.mainloop()