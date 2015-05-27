__author__ = 'boh01'
#!/bin/python
import time, os, datetime
import TimerGUI

polltime = 5 # minutes


while 1:
    print "Running time tracker"
    t = TimerGUI.TimeKeeper()
    t.run()
    print "\n Running again in {0} minutes".format(polltime)
    time.sleep(polltime*60)

