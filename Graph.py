__author__ = 'boh01'

import csv
import Tkinter
import os
import random
import math


def pluck(iterable, key, value):
    for index, item in enumerate(iterable):
        if item[key] == value:
            return index
    return None


home_dir = os.path.join(os.getenv("APPDATA"), "Timekeeper")
log_filename = os.path.join(home_dir, "log.csv")
log_file = open(log_filename, "rb")
raw_data = csv.reader(log_file)
raw_entries = []
for entry in raw_data:
    raw_entries.append(entry)

events = []
for index, entry in enumerate(raw_entries):
    duration = 0
    try:
        duration = float(entry[3]) - float(raw_entries[index - 1][3])
    except IndexError:
        pass
    if duration > 0 and duration < 3600 * 5:  # 5 hours
        event = {}
        event["date"] = entry[0]
        event["category"] = entry[1]
        event["task"] = entry[2]
        event["time"] = entry[3]
        event["duration"] = duration
        events.append(event)

categories = {}

for event in events:
    if event["category"] not in categories:
        categories[event["category"]] = event["duration"]
    else:
        categories[event["category"]] += event["duration"]

total_time = 0
for c in categories:
    total_time += categories[c]

time_per_degree = total_time / 360.0

c = Tkinter.Canvas(width=800, height=800)
c.pack()
c.create_line(1, 1, 40, 54.2)
last_slice = 0
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
for category in categories:
    bit = categories[category]/time_per_degree
    c.create_arc(300, 300, 500, 500, style=Tkinter.PIESLICE, fill = random.choice(colors) ,start=last_slice, extent=bit)
    c.create_text(400+(math.cos(math.degrees(last_slice+(bit/2.0)))*50),
                  400+(math.sin(math.degrees(last_slice+(bit/2.0)))*50),
                  text = category)
    last_slice += bit
c.mainloop()
