__author__ = 'boh01'
#!/bin/python
import time, os, datetime
home = os.getenv("HOME")
runstring = "python "+home +"/.timekeeper/TimerGUI.py"
while 1:
    gui=os.popen(runstring)
    print "Running time tracker"
    for line in gui:
        print line,
    print "\n Running again in 15 minutes"
    time.sleep(60*15)
