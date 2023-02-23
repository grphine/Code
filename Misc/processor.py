import csv
from datetime import datetime as dt
import pandas as pd

# pd.set_option('display.max_colwidth', None)
# pd.set_option('display.float_format', '{:20,.2f}'.format)

def distancedata():
    with open('Tests\\Distance\\second_test.csv', 'r') as csv_file:
        file = list(csv.reader(csv_file, delimiter=','))
        
        print('\\hline')
        print(f'{" & ".join(file[0])} \\\\')
        print('\\hline')
        for k in range(1,5):
            print(f'{file[k][0]} & {file[k][1]} & {file[k][2]} \\\\')
        print(f'\\multicolumn{{3}}{{|c|}}{{$\\cdots$}} \\\\')
        for k in range(len(file)-4,len(file)):
            print(f'{file[k][0]} & {file[k][1]} & {file[k][2]} \\\\')
        print('\hline')

def batterydata():
    with open('Tests\\Battery\\data\\230214-old.csv', 'r') as csv_file:
        file = list(csv.reader(csv_file, delimiter=','))    
        print('\\hline')
        print(f'{" & ".join(file[0])} \\\\')
        print('\\hline')
        for k in range(1,5):
            print(f'{file[k][0]} & {file[k][1]} & {file[k][2]} & \\censor{{{file[k][3]}}} & \\censor{{{file[k][4]}}} & {file[k][5]} & {file[k][6]} & {file[k][7]} \\\\')
        print(f'\\multicolumn{{8}}{{|c|}}{{$\\cdots$}} \\\\')
        for k in range(len(file)-4,len(file)):
            print(f'{file[k][0]} & {file[k][1]} & {file[k][2]} & \\censor{{{file[k][3]}}} & \\censor{{{file[k][4]}}} & {file[k][5]} & {file[k][6]} & {file[k][7]} \\\\')
        print('\hline')

# batterydata()

# distancedata()