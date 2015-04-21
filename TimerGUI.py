__author__ = 'boh01'
#!/bin/python

import Tkinter as tk
import os
import time


class TimeKeeper():
    def __init(self):
        t = time.time()

        self.master = tk.Tk()

        self.bfont = "Arial 30 bold"
        self.tfont = "Arial 20 bold"
        self.mfont = "Arial 30 bold"

        self.category = []
        self.item = []
        self.misc = []
        self.text = []
        self.rbmode = []
        self.rbtype = []
        self.cat = 1
        self.midb = 1
        self.mode = 1
        self.custom = {}

        self.typeval = tk.IntVar()
        self.typeval.set(0)
        self.modeval = tk.IntVar()
        self.modeval.set(1)

        self.system = os.sys.platform
        self.home = os.getenv("HOME")

        self.hardware = "" # "N900"


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

        self.path_linux = os.path.join(os.getenv("HOME"), ".timekeeper")
        self.path_windows = os.path.join(os.getenv("APPDATA"), "Timekeeper")


    def default(self):
        pass


    def test(self, t=0):
        print "Event called"
        item[2]["background"] = "RED"


    def close(self):
        self.writefile()
        self.master.destroy()


    def makebutton(bmaster, btext, bcommand=self.default, color='blue', font=self.bfont):
        b = tk.Button(bmaster, font=font, background=color, text=btext, border=2, command=bcommand)
        b.pack(side=tk.TOP)
        return b


    def checkdir(self):
        print "Checking for directory"
        if self.system == "linux2":
            if not os.path.exists(self.path_linux):
                print "Could not find directory, creating..."
                os.mkdir(self.path_linux)
            else:
                print "Directory exists"
        elif self.system == "win32":
            if not os.path.exists(self.path_windows):
                print "Could not find directory, creating..."
                os.mkdir(self.path_windows)
            else:
                print "Directory exists"


    def checkfile(self):
        self.checkdir()
        print "Checking to see if config file exists"
        if self.system == "linux2":
            path = os.path.join(self.path_linux, "config.cfg")
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
        if self.system == "win32":
            path = os.path.join(self.path_windows, "config.cfg")
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
        mv = self.modeval.get()
        tv = self.typeval.get()
        if mv == 1:
            t = othertext.get()
            if t != "":
                if tv == 0:
                    if len(text[cat - 1]) < 6:
                        text[cat - 1].append(t)
                        settnames()
                    else:
                        print "Too many buttons in category, item not added"
                elif tv == 1:
                    if len(text) < 6:
                        text.append([t])
                        setcnames()
                    else:
                        print "Too many Categories, item not added"
                elif tv == 2:
                    import time

                    print "Writing", text[cat - 1][0] + "," + t, "on", time.asctime()
                    self.checkdir()
                    if system == "linux2":
                        f = open(os.path.join(self.path_linux, "log.csv"), 'a')
                        f.write(time.asctime() + "," + text[cat - 1][0] + "," + str(t) + "," + str(time.time()) + "\n")
                        f.close()
                    if system == "win32":
                        f = open(os.path.join(self.path_windows, "log.csv"), 'a')
                        f.write(time.asctime() + "," + text[cat - 1][0] + "," + str(t) + "," + str(time.time()) + "\n")
                        f.close()  # TODO change this over to CSV
                    self.close()
                otherstring.set("")
        else:
            if tv == 2:
                self.dellastlogline()


    def writetolog(self, dat=0):
        if dat == 0:
            if system == "linux2":
                f = open(os.path.join(self.path_linux, "log.csv"), 'a')
                f.write(time.asctime() + "," + text[cat - 1][0] + "," + str(time.time()) + "\n")
                f.close()
            if system == "win32":
                f = open(os.path.join(self.path_windows, "log.csv"), 'a')
                f.write(time.asctime() + "," + text[cat - 1][0] + "," + str(time.time()) + "\n")
                f.close()
        else:
            if system == "linux2":
                f = open(os.path.join(self.path_linux, "log.csv"), 'a')
                f.write(time.asctime() + "," + text[cat - 1][0] + "," + str(time.time()) + "\n")
                f.close()
            if system == "win32":
                f = open(os.path.join(self.path_windows, "log.csv"), 'a')
                f.write(time.asctime() + "," + text[cat - 1][0] + "," + str(time.time()) + "\n")
                f.close()


    def graph(self):
        gui = os.popen(runstring)  # TODO fix this

    def oops(self):
        if system == "linux2":
            f = open(os.path.join(self.path_linux, "log.csv"), 'a')
            f.write(time.asctime(time.localtime(time.time() - 900)) + ",Misc,Unknown," + str(time.time() - 900) + "\n")
            f.close()
        if system == "win32":
            f = open(os.path.join(self.path_windows, "log.csv"), 'a')
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
        if system == "linux2":
            f = open(os.path.join(self.path_linux, "log.csv"), 'r')
            log = f.readlines()[1:-1]
            f.close()
            f = open(os.path.join(self.path_linux, "log.csv"), 'w')
            for line in log:
                f.write(line)
            f.close()
        if system == "win32":
            f = open(os.path.join(self.path_windows, "log.csv"), 'r')
            log = f.readlines()[1:-1]
            f.close()
            f = open(self.fp_windows("log.csv"), 'w')
            for line in log:
                f.write(line)
            f.close()

    def fp_linux(self, filename):
        pass

    def fp_windows(self, filename):
        return os.path.join(self.path_windows, "log.csv")


    def ringer(self):
        import os, time
        if self.hardware == "N900":
            os.popen(
                r"dbus-send --print-reply --system --dest=com.nokia.mce /com/nokia/mce/request com.nokia.mce.request.req_vibrator_pattern_activate string:'PatternIncomingCall'")
            time.sleep(.1)
            os.popen(
                r"dbus-send --print-reply --system --dest=com.nokia.mce /com/nokia/mce/request com.nokia.mce.request.req_vibrator_pattern_deactivate string:'PatternIncomingCall'")
            time.sleep(.1)
            os.popen(
                r"dbus-send --print-reply --system --dest=com.nokia.mce /com/nokia/mce/request com.nokia.mce.request.req_vibrator_pattern_activate string:'PatternIncomingCall'")
            time.sleep(.1)
            os.popen(
                r"dbus-send --print-reply --system --dest=com.nokia.mce /com/nokia/mce/request com.nokia.mce.request.req_vibrator_pattern_deactivate string:'PatternIncomingCall'")
            time.sleep(.1)
            os.popen(
                r"dbus-send --print-reply --system --dest=com.nokia.mce /com/nokia/mce/request com.nokia.mce.request.req_vibrator_pattern_activate string:'PatternIncomingCall'")
            time.sleep(.1)
            os.popen(
                r"dbus-send --print-reply --system --dest=com.nokia.mce /com/nokia/mce/request com.nokia.mce.request.req_vibrator_pattern_deactivate string:'PatternIncomingCall'")


    def testwrite(self):
        self.master.destroy()


    def writetask(self, i, j):
        print "Writing", self.text[i - 1][0] + "," + self.text[i - 1][j], "on", time.asctime()
        if i <= len(text[i - 1]):
            if system == "linux2":
                f = open(home + "/.timekeeper/log.csv", 'a')
                f.write(time.asctime() + "," + text[i - 1][0] + "," + text[i - 1][j] + "," + str(time.time()) + "\n")
                f.close()
            if system == "win32":
                f = open(home + "\\.timekeeper\\log.csv", 'a')
                f.write(time.asctime() + "," + text[i - 1][0] + "," + text[i - 1][j] + "," + str(time.time()) + "\n")
                f.close()


    def writetime(self, t):
        print "Writing", t, "to time log on", time.asctime()
        if system == "linux2":
            f = open(home + "/.timekeeper/timelog.csv", 'a')
            f.write(time.asctime() + "," + t + "\n")
            f.close()
        if system == "win32":
            f = open(home + "\\.timekeeper\\timelog.csv", 'a')
            f.write(time.asctime() + "," + t + "\n")
            f.close()


def buttonhandle():
    global cat
    global midb
    global mode
    global text
    global typeval
    tv = typeval.get()
    if mode == 1:
        writetask(cat, midb)
        close()
    if mode == 2:
        if tv == 0:
            text[cat - 1][midb] = ""
            text[cat - 1].remove("")
            settnames()
        elif tv == 1:
            text.remove(text[midb - 1])
            setcnames()
            settnames()


def b1():
    global midb
    midb = 1
    buttonhandle()


def b2():
    global midb
    midb = 2
    buttonhandle()


def b3():
    global midb
    midb = 3
    buttonhandle()


def b4():
    global midb
    midb = 4
    buttonhandle()


def b5():
    global midb
    midb = 5
    buttonhandle()


def b6():
    global midb
    midb = 6
    buttonhandle()


def c1():
    global cat
    cat = 1
    settnames()


def c2():
    global cat
    cat = 2
    settnames()


def c3():
    global cat
    cat = 3
    settnames()


def c4():
    global cat
    cat = 4
    settnames()


def c5():
    global cat
    cat = 5
    settnames()


def c6():
    global cat
    cat = 6
    settnames()


def settnames():
    global text
    global cat
    global item
    global mode
    for i in range(len(item)):
        item[i].pack_forget()
    if typeval.get() == 1:
        print "Resetting task buttons to category names"
        for i in range(len(text)):
            item[i]["text"] = text[i][0]
            if mode == 1:
                item[i]["background"] = "purple"
            else:
                item[i]["background"] = "red"
            item[i].pack()
    else:
        print "Resetting task buttons to", text[cat - 1][0]
        for i in range(len(text[cat - 1]) - 1):
            item[i]["text"] = text[cat - 1][i + 1]
            if mode == 1:
                item[i]["background"] = "purple"
            else:
                item[i]["background"] = "red"
            item[i].pack()


def setcnames():
    print "Resetting category button names"
    global text
    global category
    for i in range(len(category)):
        category[i].pack_forget()
    for i in range(len(text)):
        category[i]["text"] = text[i][0]
        category[i].pack()


def writenewfile():
    appdata - os.getenv["APPDATA"]
    print "Writing new file"

    def lwrite(text):
        f.write(text + "\n")

    if system == "linux2":
        f = open(home + "/.timekeeper/config", 'w')
    elif system == "win32":
        f = open(home + "\\.timekeeper\\config", 'w')
    else:
        print "NO MACS EVER! DIE!"
        print "Becasue you have a mac, this program will now crash."
        exit()
    lwrite("[Schoolwork")
    lwrite("ClassA\nClassB\nClassC\nClassD\nClassE")
    lwrite("[People")
    lwrite("Brittany")
    lwrite("[Projects")
    lwrite("Cornell")
    lwrite("Python")
    lwrite("[Misc")
    lwrite("[Other")
    f.close()


def writefile():
    checkdir()
    global text
    print "writing changes to new config file"
    if system == "linux2":
        f = open(home + "/.timekeeper/config", 'w')
    elif system == "win32":
        f = open(home + "\\.timekeeper\\config", 'w')
    else:
        print "NO MACS EVER!, DIE!"
        print "Becasue you have a mac, this program will now crash."
        exit()
    for i in range(len(text)):
        for j in range(len(text[i])):
            if j == 0:
                f.write("[" + text[i][j])
            else:
                f.write(text[i][j])
            f.write("\n")
    f.close()


def readfile():
    print "Reading config file"
    global text, system, home
    text = []
    if checkfile():
        if system == "linux2":
            f = open(home + "/.timekeeper/config", 'r')
        elif system == "win32":
            f = open(home + "\\.timekeeper\\config", 'r')
        else:
            print "NO MACS EVER!, DIE!"
            print "Becasue you have a mac, this program will now crash."
            exit()
        for line in f.readlines():
            if line[0] == "[":
                text.append([line[1:-1]])
            else:
                text[len(text) - 1].append(line[0:-1])
        f.close()
    else:
        writenewfile()
        readfile()


category.append(makebutton(containerleft, "Schoolwork", c1, "orange"))
category.append(makebutton(containerleft, "People", c2, "orange"))
category.append(makebutton(containerleft, "Projects", c3, "orange"))
category.append(makebutton(containerleft, "Class", c4, "orange"))
category.append(makebutton(containerleft, "Misc", c5, "orange"))
category.append(makebutton(containerleft, "Other", c6, "orange"))
custom = tk.Button(textframe, text="Add Task:", font="Arial 27 bold", command=custom, background="purple")
custom.pack(side=tk.LEFT)

item.append(makebutton(containermid, "test1", b1, "purple"))
item.append(makebutton(containermid, "test2", b2, "purple"))
item.append(makebutton(containermid, "test3", b3, "purple"))
item.append(makebutton(containermid, "test4", b4, "purple"))
item.append(makebutton(containermid, "Other", b5, "purple"))
otherstring = tk.StringVar()
othertext = tk.Entry(textframe, font=bfont, textvariable=otherstring)
othertext.pack(side=tk.RIGHT)

misc.append(makebutton(containerright, "OOPS", oops, 'red', bfont))

rbmode.append(
    tk.Radiobutton(modeframe, text="Add", variable=modeval, value=1, font=mfont, indicatoron=0, background="green",
                   command=setcustom))
rbmode.append(
    tk.Radiobutton(modeframe, text="Del", variable=modeval, value=2, font=mfont, indicatoron=0, background="red",
                   command=setcustom))
rbmode[0].pack(anchor=tk.W)
rbmode[1].pack(anchor=tk.W)

rbtype.append(tk.Radiobutton(task2frame, text="Task", variable=typeval, value=0, font=mfont, indicatoron=0,
                             background="purple", command=setcustom))
rbtype.append(tk.Radiobutton(taskframe, text="Category", variable=typeval, value=1, font=mfont, indicatoron=0,
                             background="orange", command=setcustom))
rbtype.append(tk.Radiobutton(taskframe, text="Temp Task", variable=typeval, value=2, font=mfont, indicatoron=0,
                             background="purple", command=setcustom))
rbtype[0].pack(anchor=tk.W)
rbtype[1].pack(anchor=tk.W)
rbtype[2].pack(anchor=tk.W)

readfile()
setcnames()
settnames()
ringer()
master.mainloop()
writetime(str(time.time() - t))
exit()