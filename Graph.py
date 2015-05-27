__author__ = 'boh01'


import csv
import Tkinter
import os

def pluck(iterable, key, value):
    for index, item in enumerate(iterable):
        if item[key] == value:
             return index
    return None

home_dir = os.path.join(os.getenv("APPDATA"), "Timekeeper")
log_filename = os.path.join(home_dir, "log.csv")
log_file = open(log_filename,"rb")
raw_data = csv.reader(log_file)
raw_entries = []
for entry in raw_data:
    raw_entries.append(entry)

events = []
for index, entry in enumerate(raw_entries):
    print entry
    duration = 0
    try:
        duration = float(entry[3]) - float(raw_entries[index-1][3])
    except IndexError:
        pass
    if duration > 0 and duration < 3600*5: # 5 hours
        event = {}
        event["date"] = entry[0]
        event["category"] = entry[1]
        event["task"] = entry[2]
        event["time"] = entry[3]
        event["duration"] = duration
        events.append(event)

categories = {}

for event in events:
    if not pluck(categories,0, event["category"]):
        categories[event["category"]] = event["duration"]
    else:
        categories[event["category"]][1] += event["duration"]

print categories

t = 0
for c in categories:
    t += categories[c]
print t

exit()
for j in entry[0:2]:
    try:
        d.append(float(j))
    except:
        d = []
if d !=[]:
    raw_data.append(d)
exit()
c = Tkinter.Canvas(width=200, height=200)
c.pack()
c.create_line(1,1,40,54.2)
for i in range(len(data)-1):
        c.create_line(1,1,40,64.2)
        c.create_line(data[i][0],data[i][1],data[i+1][0],data[i+1][1],fill = "black")
c.mainloop()