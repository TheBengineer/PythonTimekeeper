__author__ = 'boh01'
#!/bin/python
import time, os, datetime
import TimerGUI

while 1:
    print "Running time tracker"
    t = TimerGUI.TimeKeeper()
    t.run()
    print "\n Running again in 15 minutes"
    time.sleep(60*5)
