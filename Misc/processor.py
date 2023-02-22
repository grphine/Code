import csv
from datetime import datetime as dt
import pandas as pd

# pd.set_option('display.max_colwidth', None)
# pd.set_option('display.float_format', '{:20,.2f}'.format)

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

# with open('Tests\\Battery\\data\\230214.csv', 'r') as csv_file:
#     file = list(csv.reader(csv_file, delimiter=','))
    
#     print('\\hline')
#     print(f'{" & ".join(file[0])} \\\\')
#     print('\\hline')
#     for k in range(1,5):
#         print(f'{file[k][0]} & {file[k][1]} & {file[k][2]} & \\censor{{{file[k][3]}}} & \\censor{{{file[k][4]}}} & {file[k][5]} & {file[k][6]} & {file[k][7]} \\\\')
#     print(f'\\multicolumn{{8}}{{|c|}}{{$\\cdots$}} \\\\')
#     for k in range(len(file)-4,len(file)):
#         print(f'{file[k][0]} & {file[k][1]} & {file[k][2]} & \\censor{{{file[k][3]}}} & \\censor{{{file[k][4]}}} & {file[k][5]} & {file[k][6]} & {file[k][7]} \\\\')
#     print('\hline')

    # tcount = 0
    # line_count = 0
    # for row in file:
    #     tcount += 1
    # for row in file:
    #     if line_count == 0:
    #         print(f'{"& ".join(row)} \\\\')
    #         line_count += 1
    #         print()
    #     elif line_count < 6:
    #         print(f'{row[0]} & {row[1]} & {row[2]} & \\censor{{{row[3]}}} & \\censor{{{row[4]}}} & {row[5]} & {row[6]} & {row[7]} \\\\')
    #         line_count += 1
        

# df = pd.read_csv('Tests\\Battery\\data\\230213.csv')
# string = df.loc[0:1,:]
# print(string)

