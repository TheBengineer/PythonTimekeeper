__author__ = 'boh01'

from threading import Thread
import os
import Tkinter as tk
import time

import TimerGUI


class Window(Thread):
    def __init__(self):
        Thread.__init__(self)

        self.window = tk.Tk()  # Init
        self.window.geometry("900x500+300+300")
        self.window.title("Time Tracker - Ben Holleran June 2015")
        self.window.protocol("WM_DELETE_WINDOW", self.onQuit)

        # Variables

        self.timer = 5 * 60
        self.jobs = []


        # Menu bar
        self.toolbar = tk.Menu(self.window)

        self.filemenu = tk.Menu(self.toolbar, tearoff=0)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Poll", command=self.runPoll)
        self.filemenu.add_command(label="Exit", command=self.toolbar.quit)
        self.toolbar.add_cascade(label="File", menu=self.filemenu)
        self.toolbar.add_command(label="Poll", command=self.runPoll)
        self.toolbar.add_command(label="Set Timer", command=self.setTimer)
        self.toolbar.add_command(label="Quit", command=self.window.quit)
        self.window.config(menu=self.toolbar)

        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

        self.menu_frame = tk.Frame(self.main_frame)  # holds the buttons at the top

        self.poll_button = tk.Button(self.main_frame, text="Scan VIS")
        self.menu_frame.pack(side="top", expand=1)

        # self.nb =  ttk.Notebook(self.main_frame, name='notebook')
        # self.nb.enable_traversal()
        # self.nb.pack(fill=tk.BOTH, expand=tk.Y, padx=2, pady=3)
        # self.graph_frame = ttk.Frame(self.nb, name='graph')
        # self.time_frame = ttk.Frame(self.nb, name='time')
        print "Done"

    def onQuit(self):
        print "User aborted, quitting."
        # self.RMAThread.interrupt_main()
        # self.VisThread.interrupt_main()
        self.window.destroy()
        os._exit(1)

    def runPoll(self):
        t = TimerGUI.TimeKeeper()
        while len(self.jobs):
            job = self.jobs.pop()
            self.window.after_cancel(job)
        self.jobs.append(self.window.after(self.timer*1000, self.runPoll))
        t.run()
        print "Here"


    def setTimer(self):
        tmp_pop = popupWindow(self.window, self)
        self.window.wait_window(tmp_pop.top)

    def run(self):
        self.jobs.append(self.window.after(0, self.runPoll))
        self.window.mainloop()


class popupWindow(object):
    def __init__(self, master, window):
        self.parent = window
        top = self.top = tk.Toplevel(master)
        self.l = tk.Label(top, text="Time in minutes between polls:")
        self.l.pack()
        self.l2 = tk.Label(top, text="")
        self.l2.pack()
        self.e = tk.Entry(top)
        self.e.pack()
        self.b = tk.Button(top, text='Apply', command=self.cleanup)
        self.b.pack()
        self.e.bind('<Return>', self.cleanup)

    def cleanup(self, event=None):
        self.value = self.e.get()
        try:
            self.value = float(self.value)
        except ValueError:
            self.value = 5 * 60
            self.l2.config(text="Value cannot be converted to a number. Try again")
            return
        self.parent.timer = self.value * 60.0
        self.top.destroy()


a = Window()
a.start()
