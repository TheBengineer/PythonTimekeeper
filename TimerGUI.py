__author__ = 'boh01'
#!/bin/python

import Tkinter, os, time
t=time.time()

master = Tkinter.Tk()

bfont = "Arial 30 bold"
tfont = "Arial 20 bold"
mfont = "Arial 30 bold"

category =[]
item =[]
misc =[]
text =[]
rbmode = []
rbtype = []
cat = 1
midb = 1
mode = 1

typeval = Tkinter.IntVar()
typeval.set(0)
modeval = Tkinter.IntVar()
modeval.set(1)

system = os.sys.platform
home = os.getenv("HOME")


# Set up window framework --\/ \/ \/--
master.title("Simple Python Time Tracker")

container = Tkinter.Frame(master)
container.pack(expand = Tkinter.YES,fill = Tkinter.BOTH)
containerright = Tkinter.Frame(container, background="cyan",borderwidth=5,relief=Tkinter.RIDGE,width=200)
containerright.pack(side=Tkinter.RIGHT, expand=Tkinter.YES, fill=Tkinter.BOTH)
textframe = Tkinter.Frame(container, background="cyan",borderwidth=5,relief=Tkinter.RIDGE,width=200)
textframe.pack(fill=Tkinter.X,side=Tkinter.BOTTOM)
containerleft = Tkinter.Frame(container, background="cyan", borderwidth=5,relief=Tkinter.RIDGE,width=200)
containerleft.pack(side=Tkinter.LEFT, expand=Tkinter.YES, fill=Tkinter.BOTH)
containermid = Tkinter.Frame(container, background="cyan",borderwidth=5,relief=Tkinter.RIDGE,width=200)
containermid.pack(side=Tkinter.LEFT, expand=Tkinter.YES, fill=Tkinter.BOTH)

taskframe = Tkinter.Frame(containerright, background="cyan", borderwidth=5,relief=Tkinter.RIDGE,width=200)
taskframe.pack(side=Tkinter.BOTTOM, expand=Tkinter.YES, fill=Tkinter.BOTH)
modeframe = Tkinter.Frame(containerright, background="cyan", borderwidth=5,relief=Tkinter.RIDGE,width=200)
modeframe.pack(side=Tkinter.BOTTOM, expand=Tkinter.YES, fill=Tkinter.BOTH)
task2frame = Tkinter.Frame(taskframe, background="cyan",width=200)
task2frame.pack(side=Tkinter.TOP, expand=Tkinter.YES, fill=Tkinter.BOTH)



Tkinter.Label(containerleft, text="Category",font = tfont, justify = Tkinter.CENTER,background="orange").pack(side=Tkinter.TOP, anchor=Tkinter.W)
Tkinter.Label(containermid, text="Task",font = tfont, justify=Tkinter.LEFT,background="purple").pack(side=Tkinter.TOP, anchor=Tkinter.W)
Tkinter.Label(containerright, text="Menu",font = tfont, justify=Tkinter.LEFT,background="gray").pack(side=Tkinter.TOP, anchor=Tkinter.W)
Tkinter.Label(modeframe, text="Mode",font = tfont, justify=Tkinter.RIGHT,background="gray").pack(side=Tkinter.RIGHT, anchor=Tkinter.NE)
tasklabel = Tkinter.Label(task2frame, text="Add:",font = tfont,background="gray")
tasklabel.pack(side=Tkinter.RIGHT, anchor=Tkinter.NE)
# Set up window framework --/\ /\ /\--



def default():
    pass

def test(t=0):
    print "Event called"
    item[2]["background"] = "RED"

def close():
    writefile()
    master.destroy()

def makebutton(bmaster,btext,bcommand=default,color='blue',font=bfont):
    b = Tkinter.Button(bmaster,font =  font,background=color ,text = btext,border=2,command=bcommand)
    b.pack(side= Tkinter.TOP)
    return b

def checkdir():
    print "Checking for directory"
    if system == "linux2":
        if not os.path.exists(home+"/.timekeeper/"):
            print "Could not find directory, creating..."
            os.popen("mkdir /home/user/.timekeeper/")
        else:
            print "Directory exists"
    elif system == "win32":
        if not os.path.exists(home+"\\.timekeeper\\"):
            print "Could not find directory, creating..."
            os.popen("mkdir "+home+"\\.timekeeper")
        else:
            print "Directory exists"
def checkfile():
    import os
    checkdir()
    print "Checking to see if config file exists"
    if system == "linux2":
        if os.path.isfile(home+"/.timekeeper/config"):
            print "File exists, checking for data"
            if len(open(home+ "/.timekeeper/config",'r').readlines())>1:
                print "Data found"
                return 1
            else:
                return 0
                print "No data found"
        else:
            return 0
            print "No file found"
    if system == "win32":
        if os.path.isfile(home+"\\.timekeeper\\config"):
            print "File exists, checking for data"
            if len(open(home+"\\.timekeeper\\config",'r').readlines())>1:
                print "Data found"
                return 1
            else:
                return 0
                print "No data found"
        else:
            return 0
            print "No file found"

def custom():
    global cat
    global text
    global modeval
    global typeval
    mv = modeval.get()
    tv = typeval.get()
    if mv == 1:
        t=othertext.get()
        if t != "":
            if tv == 0:
                if len(text[cat-1]) < 6:
                    text[cat-1].append(t)
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
                print "Writing",text[cat-1][0]+","+t,"on",time.asctime()
                checkdir()
                if system == "linux2":
                    f = open(home+"/.timekeeper/log.csv",'a')
                    f.write(time.asctime()+","+text[cat-1][0]+","+str(t)+","+str(time.time())+"\n")
                    f.close()
                if system == "win32":
                    f = open(home+"\\.timekeeper\\log.csv",'a')
                    f.write(time.asctime()+","+text[cat-1][0]+","+str(t)+","+str(time.time())+"\n")
                    f.close()
                close()
            otherstring.set("")
    else:
        if tv == 2:
            dellastlogline()

def writetolog(dat=0):
    if dat ==0:
        if system == "linux2":
            f = open(home+"/.timekeeper/log.csv",'a')
            f.write(time.asctime()+","+text[cat-1][0]+","+str(time.time())+"\n")
            f.close()
        if system == "win32":
            f = open(home+"\\.timekeeper\\log.csv",'a')
            f.write(time.asctime()+","+text[cat-1][0]+","+str(time.time())+"\n")
            f.close()
    else:
        if system == "linux2":
            f = open(home+"/.timekeeper/log.csv",'a')
            f.write(time.asctime()+","+text[cat-1][0]+","+str(time.time())+"\n")
            f.close()
        if system == "win32":
            f = open(home+"\\.timekeeper\\log.csv",'a')
            f.write(time.asctime()+","+text[cat-1][0]+","+str(time.time())+"\n")
            f.close()

def graph():
    gui=os.popen(runstring)

def oops():
    if system == "linux2":
        f = open(home+"/.timekeeper/log.csv",'a')
        f.write(time.asctime(time.localtime(time.time()-900))+",Misc,Unknown,"+str(time.time()-900)+"\n")
        f.close()
    if system == "win32":
        f = open(home+"\\.timekeeper\\log.csv",'a')
        f.write(time.asctime(time.localtime(time.time()-900))+",Misc,Unknown,"+str(time.time()-900)+"\n")
        f.close()

def setcustom():
    global cat
    global text
    global typeval
    global modeval
    global mode
    global tasklabel
    mode = modeval.get()
    tv = typeval.get()
    settnames()
    if mode == 1:
        tasklabel["text"] = "Add:"
        if tv == 0:
            custom["background"]="purple"
            custom["text"]="Add Task:"
        elif tv == 1:
            custom["background"]="orange"
            custom["text"]="Add Category:"
        elif tv == 2:
            custom["background"]="purple"
            custom["text"]="Add Temp Task:"
    else:
        tasklabel["text"] = "Del:"
        if tv == 0:
            custom["background"]="red"
            custom["text"]="Select Task to Delete          /\\"
            settnames()
        elif tv == 1:
            custom["background"]="red"
            custom["text"]="Select Category to Delete   /\\"
            setcnames()
        elif tv == 2:
            custom["background"]="red"
            custom["text"]="Delete last Log Entry"

def dellastlogline():
    print "Deleting last Log entry"
    if system == "linux2":
        f = open(home+"/.timekeeper/log.csv",'r')
        log = f.readlines()[1:-1]
        f.close()
        f = open(home+"/.timekeeper/log.csv",'w')
        for line in log:
            f.write(line)
        f.close()
    if system == "win32":
        f = open(home+"\\.timekeeper\\log.csv",'r')
        log = f.readlines()[1:-1]
        f.close()
        f = open(home+"\\.timekeeper\\log.csv",'w')
        for line in log:
            f.write(line)
        f.close()

def ringer():
    import os,time
    os.popen(r"dbus-send --print-reply --system --dest=com.nokia.mce /com/nokia/mce/request com.nokia.mce.request.req_vibrator_pattern_activate string:'PatternIncomingCall'")
    time.sleep(.1)
    os.popen(r"dbus-send --print-reply --system --dest=com.nokia.mce /com/nokia/mce/request com.nokia.mce.request.req_vibrator_pattern_deactivate string:'PatternIncomingCall'")
    time.sleep(.1)
    os.popen(r"dbus-send --print-reply --system --dest=com.nokia.mce /com/nokia/mce/request com.nokia.mce.request.req_vibrator_pattern_activate string:'PatternIncomingCall'")
    time.sleep(.1)
    os.popen(r"dbus-send --print-reply --system --dest=com.nokia.mce /com/nokia/mce/request com.nokia.mce.request.req_vibrator_pattern_deactivate string:'PatternIncomingCall'")
    time.sleep(.1)
    os.popen(r"dbus-send --print-reply --system --dest=com.nokia.mce /com/nokia/mce/request com.nokia.mce.request.req_vibrator_pattern_activate string:'PatternIncomingCall'")
    time.sleep(.1)
    os.popen(r"dbus-send --print-reply --system --dest=com.nokia.mce /com/nokia/mce/request com.nokia.mce.request.req_vibrator_pattern_deactivate string:'PatternIncomingCall'")

def testwrite():
    master.destroy()

def writetask(i,j):
    global text
    import time
    print "Writing",text[i-1][0]+","+text[i-1][j], "on",time.asctime()
    if i <= len(text[i-1]):
        if system == "linux2":
            f = open(home+"/.timekeeper/log.csv",'a')
            f.write(time.asctime()+","+text[i-1][0]+","+text[i-1][j]+","+str(time.time())+"\n")
            f.close()
        if system == "win32":
            f = open(home+"\\.timekeeper\\log.csv",'a')
            f.write(time.asctime()+","+text[i-1][0]+","+text[i-1][j]+","+str(time.time())+"\n")
            f.close()


def writetime(t):
    print "Writing",t, "to time log on",time.asctime()
    if system == "linux2":
        f = open(home+"/.timekeeper/timelog.csv",'a')
        f.write(time.asctime()+","+t+"\n")
        f.close()
    if system == "win32":
        f = open(home+"\\.timekeeper\\timelog.csv",'a')
        f.write(time.asctime()+","+t+"\n")
        f.close()


def buttonhandle():
    global cat
    global midb
    global mode
    global text
    global typeval
    tv = typeval.get()
    if mode == 1:
        writetask(cat,midb)
        close()
    if mode == 2:
        if tv == 0:
            text[cat-1][midb]=""
            text[cat-1].remove("")
            settnames()
        elif tv == 1:
            text.remove(text[midb-1])
            setcnames()
            settnames()
def b1():
    global midb
    midb=1
    buttonhandle()
def b2():
    global midb
    midb=2
    buttonhandle()
def b3():
    global midb
    midb=3
    buttonhandle()
def b4():
    global midb
    midb=4
    buttonhandle()
def b5():
    global midb
    midb=5
    buttonhandle()
def b6():
    global midb
    midb=6
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
            if mode==1:
                item[i]["background"] = "purple"
            else:
                item[i]["background"] = "red"
            item[i].pack()
    else:
        print "Resetting task buttons to",text[cat-1][0]
        for i in range(len(text[cat-1])-1):
            item[i]["text"] = text[cat-1][i+1]
            if mode==1:
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
    global system, home
    print "Writing new file"
    def lwrite(text):
        f.write(text+"\n")
    if system == "linux2":
        f= open(home+"/.timekeeper/config",'w')
    elif system == "win32":
        f= open(home+"\\.timekeeper\\config",'w')
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
        f= open(home+"/.timekeeper/config",'w')
    elif system == "win32":
        f= open(home+"\\.timekeeper\\config",'w')
    else:
        print "NO MACS EVER!, DIE!"
        print "Becasue you have a mac, this program will now crash."
        exit()
    for i in range(len(text)):
        for j in range(len(text[i])):
            if j==0:
                f.write("["+text[i][j])
            else:
                f.write(text[i][j])
            f.write("\n")
    f.close()

def readfile():
    import os
    print "Reading config file"
    global text, system,home
    text =[]
    if checkfile():
        if system == "linux2":
            f= open(home+"/.timekeeper/config",'r')
        elif system == "win32":
            f= open(home+"\\.timekeeper\\config",'r')
        else:
            print "NO MACS EVER!, DIE!"
            print "Becasue you have a mac, this program will now crash."
            exit()
        for line in f.readlines():
            if line[0] == "[":
                text.append([line[1:-1]])
            else:
                text[len(text)-1].append(line[0:-1])
        f.close()
    else:
        writenewfile()
        readfile()


category.append(makebutton(containerleft,"Schoolwork",c1,"orange"))
category.append(makebutton(containerleft,"People",c2,"orange"))
category.append(makebutton(containerleft,"Projects",c3,"orange"))
category.append(makebutton(containerleft,"Class",c4,"orange"))
category.append(makebutton(containerleft,"Misc",c5,"orange"))
category.append(makebutton(containerleft,"Other",c6,"orange"))
custom= Tkinter.Button(textframe,text="Add Task:",font="Arial 27 bold",command=custom,background="purple")
custom.pack(side=Tkinter.LEFT)

item.append(makebutton(containermid,"test1",b1,"purple"))
item.append(makebutton(containermid,"test2",b2,"purple"))
item.append(makebutton(containermid,"test3",b3,"purple"))
item.append(makebutton(containermid,"test4",b4,"purple"))
item.append(makebutton(containermid,"Other",b5,"purple"))
otherstring=Tkinter.StringVar()
othertext = Tkinter.Entry(textframe,font=bfont,textvariable=otherstring)
othertext.pack(side=Tkinter.RIGHT)

misc.append(makebutton(containerright,"OOPS",oops,'red',bfont))

rbmode.append(Tkinter.Radiobutton(modeframe, text="Add", variable=modeval, value=1,font=mfont,indicatoron=0,background="green",command=setcustom))
rbmode.append(Tkinter.Radiobutton(modeframe, text="Del", variable=modeval, value=2,font=mfont,indicatoron=0,background="red",command=setcustom))
rbmode[0].pack(anchor=Tkinter.W)
rbmode[1].pack(anchor=Tkinter.W)


rbtype.append(Tkinter.Radiobutton(task2frame, text="Task", variable=typeval, value=0,font=mfont,indicatoron=0,background="purple",command=setcustom))
rbtype.append(Tkinter.Radiobutton(taskframe, text="Category", variable=typeval, value=1,font=mfont,indicatoron=0,background="orange",command=setcustom))
rbtype.append(Tkinter.Radiobutton(taskframe, text="Temp Task", variable=typeval, value=2,font=mfont,indicatoron=0,background="purple",command=setcustom))
rbtype[0].pack(anchor=Tkinter.W)
rbtype[1].pack(anchor=Tkinter.W)
rbtype[2].pack(anchor=Tkinter.W)

readfile()
setcnames()
settnames()
ringer()
master.mainloop()
writetime(str(time.time()-t))
exit()