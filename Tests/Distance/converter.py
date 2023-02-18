import re
import csv
import os


# take a coordinate as a string and split it into degrees and minutes
def splitter(coordinate_string):
    match_result = re.search("(\d{2})\..*", coordinate_string)
    return [coordinate_string[0:match_result.span()[0]], match_result.group(0)]

f = open('Tests\\Distance\\first_test.csv', 'w+')
writer = csv.writer(f)
header = ['latitude', 'latitude_direction', 'longitude', 'longitude_direction']
writer.writerow(header)

with open('Tests\\Distance\\data\\230216-initial-edit.csv') as csv_file:
    reader = csv.reader(csv_file)
    line_count = 0
    for row in reader:        
        line_count += 1
        #row0       row1        row2    row3    row4    row5    row6    row7    row8    row9
        #timestamp  datetime    packet  lat     dir     long    dir     alt     fix     volt
        datetime = row[1]
        lat = row[3]
        lat_dir = row[4]
        long = row[5]
        long_dir = row[6]

        if line_count == 1:
           print(f'{datetime}\t{lat}\t{long}')
        elif line_count == 5:
            break
        else:
            


            print(f'{datetime}\t{lat}\t{long}')
    


