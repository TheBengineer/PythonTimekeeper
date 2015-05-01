__author__ = 'boh01'


import csv
import Tkinter

n = "C:\F.csv"
f = open(n,"rb")
rdata =csv.reader(f)
data = []
for i in rdata:
    d = []
    for j in i[0:2]:
        try:
            d.append(float(j))
        except:
            d = []
    if d !=[]:
        data.append(d)
print data
c = Tkinter.Canvas(width=200, height=200)
c.pack()
c.create_line(1,1,40,54.2)
for i in range(len(data)-1):
        c.create_line(1,1,40,64.2)
        c.create_line(data[i][0],data[i][1],data[i+1][0],data[i+1][1],fill = "black")
c.mainloop()