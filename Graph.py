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


##
events = []
for index, entry in enumerate(raw_entries):
    duration = 0
    try:
        duration = float(entry[3]) - float(raw_entries[index - 1][3])
    except IndexError:
        pass
    if duration > 0 and duration < 3600 * 5:  # 5 hours
        event = {}
        event["date"] = str(entry[0])
        event["category"] = str(entry[1])
        event["task"] = str(entry[2])
        event["time"] = str(entry[3])
        event["duration"] = duration
        events.append(event)

categories = {}
for event in events:
    if event["category"] not in categories:
        categories[event["category"]] = event["duration"]
    else:
        categories[event["category"]] += event["duration"]

tasks = {}
for event in events:
    if event["category"] not in tasks:
        tasks[event["category"]] = {}
    if event["task"] not in tasks[event["category"]]:
        tasks[event["category"]][event["task"]] = event["duration"]
    else:
        tasks[event["category"]][event["task"]] += event["duration"]

print tasks
print categories

sorted_categories = sorted(categories.items(), key=lambda x: x[1])
sorted_tasks = []
for c in reversed(sorted_categories):
    sorted_tasks.append((c,  sorted(tasks[c[0]].items(), key=lambda x: x[1], reverse=True)))
print sorted_tasks
print  sorted(tasks.items(), key=lambda x: x[1])

total_time = 0
for c in sorted_categories:
    total_time += c[1]

time_per_degree = total_time / 360.0

c = Tkinter.Canvas(width=800, height=800)
c.pack()
c.create_line(1, 1, 40, 54.2)
last_slice = 90
colors = ["red", "orange", "yellow", "green", "blue", "violet"]

for task in tasks:
    bit = tasks[task] / time_per_degree
    c.create_arc(250, 250, 550, 550, style=Tkinter.PIESLICE, fill=random.choice(colors), start=last_slice, extent=bit)
    c.create_text(400 + (math.cos(-math.radians((last_slice + (bit / 2.0)))) * 210),
                  400 + (math.sin(-math.radians((last_slice + (bit / 2.0)))) * 210),
                  text=task)
    last_slice += bit

last_slice = 90

for category in sorted_categories:
    bit = category[1] / time_per_degree
    c.create_arc(300, 300, 500, 500, style=Tkinter.PIESLICE, fill=random.choice(colors), start=last_slice, extent=bit)
    if bit > 20:
        c.create_text(400 + (math.cos(-math.radians((last_slice + (bit / 2.0)))) * 70),
                      400 + (math.sin(-math.radians((last_slice + (bit / 2.0)))) * 70),
                      text=category[0])
    else:
        c.create_text(400 + (math.cos(-math.radians((last_slice + (bit / 2.0)))) * 110),
                      400 + (math.sin(-math.radians((last_slice + (bit / 2.0)))) * 110),
                      text=category[0])
    last_slice += bit
c.mainloop()
