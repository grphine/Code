import re
import csv

# take a coordinate as a string and split it into degrees and minutes
def splitter(coordinate_string):
    match_result = re.search("(\d{2})\..*", coordinate_string)  #match minutes
    return [coordinate_string[0:match_result.span()[0]], match_result.group(0)]     #return [degrees, minutes]

#reformat coordinate into standardised system
def coord_rewrite(split_coord, direction):
    d = ''
    if direction == 'W' or direction == 'S':   
        d = '-'
    return d + split_coord[0] + "'" + split_coord[1]

with open('Tests\\Distance\\data\\230216-initial-edit.csv') as csv_file:
    with open('Tests\\Distance\\first_test.csv', 'w+', newline='') as write_file:
        reader = csv.reader(csv_file)
        writer = csv.writer(write_file)
        writer.writerow(['datetime', 'latitude', 'longitude'])  #headers
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

            if line_count == 1:     #headers
                # print(f'{datetime}\t{lat}\t{long}')
                continue
            # elif line_count == 5:
            #     break
            else:
                # print(f'{datetime}\t{coord_rewrite(splitter(lat), lat_dir)}\t{coord_rewrite(splitter(long), long_dir)}')
                writer.writerow([datetime, coord_rewrite(splitter(lat), lat_dir), coord_rewrite(splitter(long), long_dir)])

    


