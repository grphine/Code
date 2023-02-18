import csv
import matplotlib.pyplot as plt
from datetime import datetime as dt
import seaborn as sns
sns.set_style("whitegrid")

blue, = sns.color_palette("muted", 1)

timestamps_1 = []
level_1 = []
fix_1 = []

with open('Tests\\Battery\\data\\230213.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        timestamps_1.append(dt.strptime(row[1], '%d-%m-%y %H:%M:%S'))
        level_1.append(float(row[7]))
        fix_1.append(int(row[6]))
with open('Tests\\Battery\\data\\230214-old.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        timestamps_1.append(dt.strptime(row[1], '%d-%m-%y %H:%M:%S'))    #13-02-23 22:19:32
        level_1.append(float(row[7]))
        fix_1.append(int(row[6]))

plt.subplot(2, 1, 1)
plt.plot_date(timestamps_1, level_1, fmt='g.', tz='UTC', xdate=True, ydate=False, label = "Battery level")

plt.xticks(rotation = 25)
plt.xlabel('Timestamps')
plt.ylabel('Voltage (V)')
plt.title('Battery discharge')
plt.grid()
plt.legend()

plt.plot(timestamps_1, fix_1, label = "GPS fix quality")


plt.grid()


timestamps_2  = []
level_2 = []
fix_2 = []

with open('Tests\\Battery\\data\\230214.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        timestamps_2.append(dt.strptime(row[1], '%d-%m-%y %H:%M:%S'))
        level_2.append(float(row[7]))
        fix_2.append(int(row[6]))

plt.subplot(2, 1, 2)
plt.scatter(timestamps_2, level_2, color = 'g', marker = '.',label = "Battery level")

plt.xticks(rotation = 25)
plt.xlabel('Timestamps')
plt.ylabel('Voltage (V)')
plt.title('Battery charge')
plt.grid()
plt.legend()

plt.plot(timestamps_2, fix_2, label = "GPS fix quality")

plt.grid()

plt.suptitle("Battery charge curves")
plt.show()

