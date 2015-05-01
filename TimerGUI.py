__author__ = 'boh01'
#!/bin/python

import Tkinter as tk
import os
import time
from functools import partial


ADD = 1
DELETE = 2


class TimeKeeper():
    def __init__(self):
        self.t = time.time()

        self.master = tk.Tk()

        self.bfont = "Arial 30 bold"
        self.tfont = "Arial 20 bold"
        self.mfont = "Arial 30 bold"

        self.system = os.sys.platform

        if self.system == "linux2":
            self.directory = os.getenv("HOME")
        elif self.system == "win32":
            self.directory = os.path.join(os.getenv("APPDATA"), "Timekeeper")
        else:
            print "NO MACS EVER! DIE!"
            print "Because you have a mac, this program will now crash."
            exit()

        self.categories = []
        self.tasks = []
        self.buttons_text = {}
        self.readfile()

        self.misc = []
        self.rbmode = []
        self.rbtype = []
        self.cat = self.buttons_text.keys()[0]
        self.mode = ADD
        self.custom = {}

        self.typeval = tk.IntVar()
        self.typeval.set(0)
        self.modeval = tk.IntVar()
        self.modeval.set(1)


        # Set up window framework --\/ \/ \/--
        self.master.title("Simple Python Time Tracker")

        self.container = tk.Frame(self.master)
        self.container.pack(expand=tk.YES, fill=tk.BOTH)
        self.containerright = tk.Frame(self.container, background="cyan", borderwidth=5, relief=tk.RIDGE, width=200)
        self.containerright.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)
        self.textframe = tk.Frame(self.container, background="cyan", borderwidth=5, relief=tk.RIDGE, width=200)
        self.textframe.pack(fill=tk.X, side=tk.BOTTOM)
        self.containerleft = tk.Frame(self.container, background="cyan", borderwidth=5, relief=tk.RIDGE, width=200)
        self.containerleft.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)
        self.containermid = tk.Frame(self.container, background="cyan", borderwidth=5, relief=tk.RIDGE, width=200)
        self.containermid.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)

        self.taskframe = tk.Frame(self.containerright, background="cyan", borderwidth=5, relief=tk.RIDGE, width=200)
        self.taskframe.pack(side=tk.BOTTOM, expand=tk.YES, fill=tk.BOTH)
        self.modeframe = tk.Frame(self.containerright, background="cyan", borderwidth=5, relief=tk.RIDGE, width=200)
        self.modeframe.pack(side=tk.BOTTOM, expand=tk.YES, fill=tk.BOTH)
        self.task2frame = tk.Frame(self.taskframe, background="cyan", width=200)
        self.task2frame.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)

        tk.Label(self.containerleft, text="Category", font=self.tfont, justify=tk.CENTER,
                 background="orange").pack(side=tk.TOP, anchor=tk.W)
        tk.Label(self.containermid, text="Task", font=self.tfont, justify=tk.LEFT, background="purple").pack(
            side=tk.TOP, anchor=tk.W)
        tk.Label(self.containerright, text="Menu", font=self.tfont, justify=tk.LEFT, background="gray").pack(
            side=tk.TOP, anchor=tk.W)
        tk.Label(self.modeframe, text="Mode", font=self.tfont, justify=tk.RIGHT, background="gray").pack(
            side=tk.RIGHT, anchor=tk.NE)
        self.tasklabel = tk.Label(self.task2frame, text="Add:", font=self.tfont, background="gray")
        self.tasklabel.pack(side=tk.RIGHT, anchor=tk.NE)
        # Set up window framework --/\ /\ /\--

        self.build_categories()

        self.add_del_button = tk.Button(self.textframe, text="Add Task:", font="Arial 27 bold",
                                        command=self.add_del_tasks, background="purple")
        self.add_del_button.pack(side=tk.LEFT)

        self.build_tasks()

        self.otherstring = tk.StringVar()
        self.othertext = tk.Entry(self.textframe, font=self.bfont, textvariable=self.otherstring)
        self.othertext.bind("<Return>", self.add_del_tasks)
        self.othertext.pack(side=tk.RIGHT)

        self.misc.append(self.makebutton(self.containerright, "OOPS", self.oops, 'red', self.bfont))

        self.rbmode.append(
            tk.Radiobutton(self.modeframe, text="Add", variable=self.modeval, value=ADD, font=self.mfont, indicatoron=0,
                           background="green", command=self.setcustom))
        self.rbmode.append(
            tk.Radiobutton(self.modeframe, text="Del", variable=self.modeval, value=DELETE, font=self.mfont,
                           indicatoron=0, background="red", command=self.setcustom))
        self.rbmode[0].pack(anchor=tk.W)
        self.rbmode[1].pack(anchor=tk.W)

        self.rbtype.append(
            tk.Radiobutton(self.task2frame, text="Task", variable=self.typeval, value=0, font=self.mfont, indicatoron=0,
                           background="purple", command=self.setcustom))
        self.rbtype.append(
            tk.Radiobutton(self.taskframe, text="Category", variable=self.typeval, value=1, font=self.mfont,
                           indicatoron=0, background="orange", command=self.setcustom))
        self.rbtype.append(
            tk.Radiobutton(self.taskframe, text="Temp Task", variable=self.typeval, value=2, font=self.mfont,
                           indicatoron=0, background="purple", command=self.setcustom))
        self.rbtype[0].pack(anchor=tk.W)
        self.rbtype[1].pack(anchor=tk.W)
        self.rbtype[2].pack(anchor=tk.W)
        self.textframe.config(width = 662, height = 85)
        self.textframe.pack_propagate(False)

    def build_categories(self):
        print "Building Category buttons"
        for category_button in self.categories:
            category_button.pack_forget()
            category_button.destroy()
        self.categories = []
        for index, category_name in enumerate(self.buttons_text):
            print  category_name
            button_call = partial(self.category_button_handle, index)
            self.categories.append(self.makebutton(self.containerleft, category_name, button_call, "orange"))

    def build_tasks(self):
        print "Assigning Category buttons"
        for task_button in self.tasks:
            task_button.pack_forget()
            task_button.destroy()
        self.tasks = []
        for index in range(5):
            button_call = partial(self.task_button_handle, index)
            self.tasks.append(self.makebutton(self.containermid, "", button_call, "purple"))
        self.set_task_names()

    def default(self):
        pass

    def test(self, t=0):
        print "Event called"
        self.tasks[2]["background"] = "RED"

    def close(self):
        self.writefile()
        self.master.destroy()

    def makebutton(self, bmaster, btext, bcommand=None, color='blue', font=None):
        if not bcommand:
            bcommand = self.default
        if not font:
            font = self.bfont
        b = tk.Button(bmaster, font=font, background=color, text=btext, border=2, command=bcommand)
        b.pack(side=tk.TOP)
        return b

    def checkdir(self):
        print "Checking for directory"
        if not os.path.exists(self.directory):
            print "Could not find directory, creating..."
            os.mkdir(self.directory)
        else:
            print "Directory exists"

    def checkfile(self):
        self.checkdir()
        print "Checking to see if config file exists"
        path = os.path.join(self.directory, "config.cfg")
        if os.path.isfile(path):
            print "File exists, checking for data"
            if len(open(path, 'r').readlines()) > 1:
                print "Data found"
                return 1
            else:
                print "No data found"
                return 0
        else:
            print "No file found"
            return 0

    def add_del_tasks(self, event=None):
        add_mode = self.modeval.get()
        task_mode = self.typeval.get()
        new_text = self.othertext.get()
        if add_mode == ADD:
            if new_text != "":
                if task_mode == 0:
                    if self.cat in self.buttons_text:
                        if len(self.buttons_text[self.cat]) < 6:
                            self.buttons_text[self.cat].append(new_text)
                            self.set_task_names()
                        else:
                            print "Too many buttons in category, task not added"
                    else:
                        print "Category", self.cat, "does not exist in", self.buttons_text
                elif task_mode == 1:
                    if len(self.buttons_text) < 6:
                        if new_text not in self.buttons_text:
                            self.buttons_text[new_text] = []
                            self.set_category_names()
                        print "Category", new_text, "already exists in", self.buttons_text
                    else:
                        print "Too many Categories, Category not added"
                elif task_mode == 2:
                    self.writetask(self.cat, new_text)
                self.otherstring.set("")
        else:  # DELETE mode
            if task_mode == 0:
                pass # This is handled by clicking on a task button
                self.buttons_text[self.cat].remove(new_text)  # deletes the task from the dict
                self.set_task_names()
            elif task_mode == 1:
                pass # This is handled by clicking on a task button
                del self.buttons_text[new_text]  # Deletes the full category
                self.set_category_names()
            elif task_mode == 2:
                self.dellastlogline()
        self.writefile()
        self.set_category_names()
        self.set_task_names()

    def graph(self):
        # gui = os.popen(runstring)  # TODO fix this
        pass

    def oops(self):
        f = self.open_file("log.csv", 'a')
        f.write(time.asctime(time.localtime(time.time() - 900)) + ",Misc,Unknown," + str(time.time() - 900) + "\n")
        f.close()

    def setcustom(self):
        self.mode = self.modeval.get()
        tv = self.typeval.get()
        self.set_task_names()
        if self.mode == 1:
            self.tasklabel["text"] = "Add:"
            if tv == 0:
                self.add_del_button["background"] = "purple"
                self.add_del_button["text"] = "Add Task:"
            elif tv == 1:
                self.add_del_button["background"] = "orange"
                self.add_del_button["text"] = "Add Category:"
            elif tv == 2:
                self.add_del_button["background"] = "purple"
                self.add_del_button["text"] = "Add Temp Task:"
        else:
            self.tasklabel["text"] = "Del:"
            if tv == 0:
                self.add_del_button["background"] = "red"
                self.add_del_button["text"] = "Select Task to Delete          /\\"
                self.set_task_names()
            elif tv == 1:
                self.add_del_button["background"] = "red"
                self.add_del_button["text"] = "Select Category to Delete   /\\"
                self.set_category_names()
            elif tv == 2:
                self.add_del_button["background"] = "red"
                self.add_del_button["text"] = "Delete last Log Entry"

    def dellastlogline(self):
        print "Deleting last Log entry"
        f = self.open_file("log.csv", 'r')
        log = f.readlines()[1:-1]
        f.close()
        f = self.open_file("log.csv", 'w')
        for line in log:
            f.write(line)
        f.close()

    def open_file(self, filename, mode):
        if self.system == "linux2":
            return open(os.path.join(self.directory, filename), mode)
        elif self.system == "win32":
            return open(os.path.join(self.directory, filename), mode)
        else:
            print "NO MACS EVER! DIE!"
            print "Because you have a mac, this program will now crash."
            exit()

    def testwrite(self):
        self.master.destroy()

    def writetask(self, category_name, task_name):
        print "Writing", category_name + "," + task_name, "at", time.asctime()
        f = self.open_file("log.csv", 'a')
        f.write(time.asctime() + "," + category_name + "," + task_name + "," + str(time.time()) + "\n")
        f.close()

    def writetime(self, t):
        print "Writing", t, "to time log on", time.asctime()
        f = self.open_file("timelog.csv", 'a')
        f.write(time.asctime() + "," + t + "\n")
        f.close()

    def task_button_handle(self, task_num):
        tv = self.typeval.get()
        print self.mode
        if self.mode == ADD:
            self.writetask(self.cat, self.buttons_text[self.cat][task_num])
            self.close()
        if self.mode == DELETE:
            if tv == 0:
                del self.buttons_text[self.cat][task_num]
            elif tv == 1:
                del self.buttons_text[self.tasks[task_num]["text"]]
                self.set_category_names()
            self.set_task_names()

    def category_button_handle(self, cat_num):
        self.cat = self.categories[cat_num]["text"]
        self.set_task_names()
        self.set_category_names()
        self.categories[cat_num]["background"] = "orange4"

    def set_task_names(self):
        for task in self.tasks:
            task.pack_forget()
        if self.typeval.get() == 1:
            print "Resetting task buttons to category names"
            for index, category in enumerate(self.buttons_text):
                task = self.tasks[index]
                task["text"] = category
                if self.mode == ADD:
                    task["background"] = "purple"
                else:
                    task["background"] = "red"
                task.pack()
        else:
            print "Resetting task buttons to", self.cat
            for task_num, task_text in enumerate(self.buttons_text[self.cat]):  # Gets all the tasks from the text tuple
                task = self.tasks[task_num]
                task["text"] = task_text
                if self.mode == ADD:
                    task["background"] = "purple"
                else:
                    task["background"] = "red"
                task.pack()

    def set_category_names(self):
        print "Resetting category button names"
        for button in self.categories:
            button.pack_forget()
        for index, text in enumerate(self.buttons_text):
            self.categories[index]["text"] = text
            self.categories[index]["background"] = "orange"
            self.categories[index].pack()

    def writenewfile(self):

        def lwrite(f, text):
            f.write(text + "\n")

        print "Writing new file"
        f = self.open_file("config.cfg", "w")
        lwrite(f, "[Tom")
        lwrite(f, "Emails\nTickets")
        lwrite(f, "[Dave")
        lwrite(f, "Japan")
        lwrite(f, "Markem")
        lwrite(f, "[Ben")
        lwrite(f, "Python")
        lwrite(f, "Useful Web")
        lwrite(f, "Useless Web")
        lwrite(f, "[Misc")
        lwrite(f, "[Other")
        f.close()

    def writefile(self):
        self.checkdir()
        print "writing changes to new config file"
        f = self.open_file("config.cfg", "w")
        for category_name in self.buttons_text:
            f.write("[" + category_name+"\n")
            for task_name in self.buttons_text[category_name]:
                f.write(task_name)
                f.write("\n")
        f.close()

    def readfile(self):
        print "Reading config file"
        if self.checkfile():
            f = self.open_file("config.cfg", "r")
            lastline = None
            for line in f.readlines():
                if line[0] == "[":
                    self.buttons_text[line[1:-1]] = []
                    lastline = line[1:-1]
                else:
                    if lastline:
                        self.buttons_text[lastline].append(line[0:-1])
            f.close()
        else:
            self.writenewfile()
            self.readfile()

    def run(self):
        self.set_category_names()
        self.set_task_names()
        self.master.mainloop()
        self.writetime(str(time.time() - self.t))
        exit()


if __name__ == "__main__":
    a = TimeKeeper()
    a.run()