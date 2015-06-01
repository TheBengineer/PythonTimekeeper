__author__ = 'boh01'

import csv
import Tkinter
import os
import math
import ttk


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
sorted_categories = sorted(categories.items(), key=lambda x: x[1])

tasks = {}
for event in events:
    if event["category"] not in tasks:
        tasks[event["category"]] = {}
    if event["task"] not in tasks[event["category"]]:
        tasks[event["category"]][event["task"]] = event["duration"]
    else:
        tasks[event["category"]][event["task"]] += event["duration"]

sorted_tasks = []
for c in reversed(sorted_categories):
    sorted_tasks.append((c, sorted(tasks[c[0]].items(), key=lambda x: x[1], reverse=True)))

total_time = 0
for c in sorted_categories:
    total_time += c[1]

time_per_degree = total_time / 360.0


c = Tkinter.Canvas(width=800, height=800)
c.pack()


def color(a, b=None):
    import random

    random.seed(a)
    x = [random.random(), random.random(), random.random()]
    if b:
        random.seed(b)
        y = [random.random(), random.random(), random.random()]
    else:
        y = [0, 0, 0]
    c = "#"
    for i, n in enumerate(x):
        number = int((x[i] * 3600) + (y[i] * 400))
        c += hex(number)[2:].rjust(3, "0")
    return c


last_slice = 90
for category in sorted_tasks:
    print category[1]
    for task in category[1]:
        bit =- task[1] / time_per_degree
        c.create_arc(100, 100, 700, 700, style=Tkinter.PIESLICE, fill=color(category[0][0], task[0]), start=last_slice,
                     extent=bit)
        if bit > 10:
            c.create_text(400 + (math.cos(-math.radians((last_slice + (bit / 2.0)))) * 170),
                          400 + (math.sin(-math.radians((last_slice + (bit / 2.0)))) * 170),
                          text=task[0])
        else:
            c.create_text(400 + (math.cos(-math.radians((last_slice + (bit / 2.0)))) * 320),
                          400 + (math.sin(-math.radians((last_slice + (bit / 2.0)))) * 320),
                          text=task[0])
        last_slice += bit

last_slice = 90

for category in sorted_categories:
    bit = category[1] / time_per_degree
    c.create_arc(300, 300, 500, 500, style=Tkinter.PIESLICE, fill=color(category[0]), start=last_slice, extent=bit)
    if bit > 20:
        c.create_text(400 + (math.cos(-math.radians((last_slice + (bit / 2.0)))) * 60),
                      400 + (math.sin(-math.radians((last_slice + (bit / 2.0)))) * 60),
                      text=category[0])
    else:
        c.create_text(400 + (math.cos(-math.radians((last_slice + (bit / 2.0)))) * 120),
                      400 + (math.sin(-math.radians((last_slice + (bit / 2.0)))) * 120),
                      text=category[0])
    last_slice += bit

c.mainloop()
