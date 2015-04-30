__author__ = 'boh01'
#!/bin/python

import Tkinter as tk
import os
import time

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
        self.home = os.getenv("HOME")

        if self.system == "linux2":
            self.directory = os.getenv("HOME")
        elif self.system == "win32":
            self.directory = os.path.join(os.getenv("APPDATA"), "Timekeeper")
        else:
            print "NO MACS EVER! DIE!"
            print "Because you have a mac, this program will now crash."
            exit()

        self.hardware = ""  # "N900"

        self.category = []
        self.item = []
        self.misc = []
        se = []
        self.rbmode = []
        self.rbtype = []
        self.cat = 1
        self.midb = 1
        self.mode = ADD
        self.custom = {}
        self.buttons_text = []

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

        self.readfile()
        self.build_categories()

        #self.category.append(self.makebutton(self.containerleft, "", self.c1, "orange"))
        #self.category.append(self.makebutton(self.containerleft, "", self.c2, "orange"))
        #self.category.append(self.makebutton(self.containerleft, "", self.c3, "orange"))
        #self.category.append(self.makebutton(self.containerleft, "", self.c4, "orange"))
        #self.category.append(self.makebutton(self.containerleft, "", self.c5, "orange"))
        #self.category.append(self.makebutton(self.containerleft, "", self.c6, "orange"))

        custom = tk.Button(self.textframe, text="Add Task:", font="Arial 27 bold", command=self.custom,
                           background="purple")
        custom.pack(side=tk.LEFT)

        self.item.append(self.makebutton(self.containermid, "test1", self.b1, "purple"))
        self.item.append(self.makebutton(self.containermid, "test2", self.b2, "purple"))
        self.item.append(self.makebutton(self.containermid, "test3", self.b3, "purple"))
        self.item.append(self.makebutton(self.containermid, "test4", self.b4, "purple"))
        self.item.append(self.makebutton(self.containermid, "Other", self.b5, "purple"))
        self.otherstring = tk.StringVar()
        self.othertext = tk.Entry(self.textframe, font=self.bfont, textvariable=self.otherstring)
        self.othertext.pack(side=tk.RIGHT)

        self.misc.append(self.makebutton(self.containerright, "OOPS", self.oops, 'red', self.bfont))

        self.rbmode.append(
            tk.Radiobutton(self.modeframe, text="Add", variable=self.modeval, value=ADD, font=self.mfont, indicatoron=0,
                           background="green",
                           command=self.setcustom))
        self.rbmode.append(
            tk.Radiobutton(self.modeframe, text="Del", variable=self.modeval, value=DELETE, font=self.mfont, indicatoron=0,
                           background="red",
                           command=self.setcustom))
        self.rbmode[0].pack(anchor=tk.W)
        self.rbmode[1].pack(anchor=tk.W)

        self.rbtype.append(
            tk.Radiobutton(self.task2frame, text="Task", variable=self.typeval, value=0, font=self.mfont, indicatoron=0,
                           background="purple", command=self.setcustom))
        self.rbtype.append(
            tk.Radiobutton(self.taskframe, text="Category", variable=self.typeval, value=1, font=self.mfont,
                           indicatoron=0,
                           background="orange", command=self.setcustom))
        self.rbtype.append(
            tk.Radiobutton(self.taskframe, text="Temp Task", variable=self.typeval, value=2, font=self.mfont,
                           indicatoron=0,
                           background="purple", command=self.setcustom))
        self.rbtype[0].pack(anchor=tk.W)
        self.rbtype[1].pack(anchor=tk.W)
        self.rbtype[2].pack(anchor=tk.W)

    def build_categories(self):
        print "Building Category buttons"
        for i in self.category:
            i.pack_forget()
        self.category = []
        for index, category in enumerate(self.buttons_text):
            category_name = category[0]
            self.category.append(self.makebutton(self.containerleft, category_name, lambda: self.category_button(index), "orange"))

    def build_tasks(self):
        print "Building Category buttons"
        for i in self.category:
            i.pack_forget()
        self.category = []
        for index, category in enumerate(self.buttons_text):
            category_name = category[0]
            self.category.append(self.makebutton(self.containerleft, category_name, lambda: self.category_button(index), "orange"))

    def default(self):
        pass

    def test(self, t=0):
        print "Event called"
        self.item[2]["background"] = "RED"

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

    def custom(self):
        add_mode = self.modeval.get()
        task_mode = self.typeval.get()
        if add_mode == ADD:
            t = self.othertext.get()
            if t != "":
                if task_mode == 0:
                    if len(self.buttons_text[self.cat - 1]) < 6:
                        self.buttons_text[self.cat - 1].append(t)
                        self.settnames()
                    else:
                        print "Too many buttons in category, item not added"
                elif task_mode == 1:
                    if len(self.buttons_text) < 6:
                        self.buttons_text.append([t])
                        self.setcnames()
                    else:
                        print "Too many Categories, item not added"
                elif task_mode == 2:
                    import time

                    print "Writing", self.buttons_text[self.cat - 1][0] + "," + t, "on", time.asctime()
                    self.checkdir()
                    f = self.open_file("log.csv", 'a')
                    f.write(time.asctime() + "," + self.buttons_text[self.cat - 1][0] + "," + str(t) + "," + str(
                        time.time()) + "\n")
                    f.close()
                    self.close()
                self.otherstring.set("")
        else:
            if task_mode == 2:
                self.dellastlogline()

    def writetolog(self, dat=0):
        if dat == 0:  # TODO What does this do?
            f = self.open_file("log.csv", 'a')
            f.write(time.asctime() + "," + self.buttons_text[self.cat - 1][0] + "," + str(time.time()) + "\n")
            f.close()
        else:
            f = self.open_file("log.csv", 'a')
            f.write(time.asctime() + "," + self.buttons_text[self.cat - 1][0] + "," + str(time.time()) + "\n")
            f.close()

    def graph(self):
        #gui = os.popen(runstring)  # TODO fix this
        pass

    def oops(self):
        f = self.open_file("log.csv", 'a')
        f.write(time.asctime(time.localtime(time.time() - 900)) + ",Misc,Unknown," + str(time.time() - 900) + "\n")
        f.close()

    def setcustom(self):
        mode = self.modeval.get()
        tv = self.typeval.get()
        self.settnames()
        if mode == 1:
            self.tasklabel["text"] = "Add:"
            if tv == 0:
                self.custom["background"] = "purple"
                self.custom["text"] = "Add Task:"
            elif tv == 1:
                self.custom["background"] = "orange"
                self.custom["text"] = "Add Category:"
            elif tv == 2:
                self.custom["background"] = "purple"
                self.custom["text"] = "Add Temp Task:"
        else:
            self.tasklabel["text"] = "Del:"
            if tv == 0:
                self.custom["background"] = "red"
                self.custom["text"] = "Select Task to Delete          /\\"
                self.settnames()
            elif tv == 1:
                self.custom["background"] = "red"
                self.custom["text"] = "Select Category to Delete   /\\"
                self.setcnames()
            elif tv == 2:
                self.custom["background"] = "red"
                self.custom["text"] = "Delete last Log Entry"

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

    def writetask(self, i, j):
        print "Writing", self.buttons_text[i - 1][0] + "," + self.buttons_text[i - 1][j], "on", time.asctime()
        if i <= len(self.buttons_text[i - 1]):
            f = self.open_file("log.csv", 'a')
            f.write(
                time.asctime() + "," + self.buttons_text[i - 1][0] + "," + self.buttons_text[i - 1][j] + "," + str(time.time()) + "\n")
            f.close()

    def writetime(self, t):
        print "Writing", t, "to time log on", time.asctime()
        f = self.open_file("timelog.csv", 'a')
        f.write(time.asctime() + "," + t + "\n")
        f.close()

    def buttonhandle(self):
        tv = self.typeval.get()
        if self.mode == ADD:
            self.writetask(self.cat, self.midb)
            self.close()
        if self.mode == DELETE:
            if tv == 0:
                self.buttons_text[self.cat - 1][self.midb] = ""
                self.buttons_text[self.cat - 1].remove("")
                self.settnames()
            elif tv == 1:
                self.buttons_text.remove(self.buttons_text[self.midb - 1])
                self.setcnames()
                self.settnames()

    def b1(self):
        self.midb = 1
        self.buttonhandle()

    def b2(self):
        self.midb = 2
        self.buttonhandle()

    def b3(self):
        self.midb = 3
        self.buttonhandle()

    def b4(self):
        self.midb = 4
        self.buttonhandle()

    def b5(self):
        self.midb = 5
        self.buttonhandle()

    def b6(self):
        self.midb = 6
        self.buttonhandle()

    def category_button(self, cat_num):
        self.cat = cat_num
        self.settnames()

    def settnames(self):
        for i in range(len(self.item)):
            self.item[i].pack_forget()
        if self.typeval.get() == 1:
            print "Resetting task buttons to category names"
            for i in range(len(self.buttons_text)):
                self.item[i]["text"] = self.buttons_text[i][0]
                if self.mode == ADD:
                    self.item[i]["background"] = "purple"
                else:
                    self.item[i]["background"] = "red"
                self.item[i].pack()
        else:
            print "Resetting task buttons to", self.buttons_text[self.cat - 1][0]
            for i in range(len(self.buttons_text[self.cat - 1]) - 1):
                self.item[i]["text"] = self.buttons_text[self.cat - 1][i + 1]
                if self.mode == ADD:
                    self.item[i]["background"] = "purple"
                else:
                    self.item[i]["background"] = "red"
                self.item[i].pack()

    def setcnames(self):
        print "Resetting category button names"
        for button in self.category:
            button.pack_forget()
        for index, text in enumerate(self.buttons_text):
            self.category[index]["text"] = text[index][0]
            self.category[index].pack()

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
        for i in range(len(self.buttons_text)):
            for j in range(len(self.buttons_text[i])):
                if j == 0:
                    f.write("[" + self.buttons_text[i][j])
                else:
                    f.write(self.buttons_text[i][j])
                f.write("\n")
        f.close()

    def readfile(self):
        print "Reading config file"
        self.buttons_text = []
        if self.checkfile():
            f = self.open_file("config.cfg", "r")
            for line in f.readlines():
                if line[0] == "[":
                    self.buttons_text.append([line[1:-1]])
                else:
                    self.buttons_text[len(self.buttons_text) - 1].append(line[0:-1])
            f.close()
        else:
            self.writenewfile()
            self.readfile()

    def run(self):
        self.setcnames()
        self.settnames()
        self.master.mainloop()
        self.writetime(str(time.time() - self.t))
        exit()


if __name__ == "__main__":
    a = TimeKeeper()
    a.run()