import csv
import matplotlib.pyplot as plt
import matplotlib.dates as md
import datetime as dt
import time

x = []
y = []

with open('Tests\\Battery\\data\\230213.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[7]))

with open('Tests\\Battery\\data\\230214-old.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[7]))

plt.scatter(x, y, color = 'g', marker = '.',label = "Battery level")

plt.xticks(rotation = 25)
plt.xlabel('Timestamps')
plt.ylabel('Voltage (V)')
plt.title('Battery discharge', fontsize = 20)
plt.grid()
plt.legend()
plt.show()