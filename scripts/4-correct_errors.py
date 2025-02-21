import numpy as np
import pickle

def float_time(string_time):
    return int(string_time.split(':')[0]) + int(string_time.split(':')[1])/60

def split_row(row_string):
    row_output = str(row_string).split('\\t')[1:14]
    row_output[-1] = row_output[-1].split('\\n')[0]
    row_output[-1] = row_output[-1].split("'")[0]
    return row_output

ctgs = {'D' : 1.0,
        'M' : 2.0,
        'R' : 3.0}

site_names = [
    'BSCN', 
    'BTCN', 
    'GONA', 
    'LCFR', 
    'RVUS'
    ]

site_name = site_names[0]

fnames = ['BSCN00_2021_208']
fname = fnames[0]
    

input_data = np.zeros((223, 13), dtype='float64')
input_uncert = np.zeros((217, 13), dtype='float64')
output_data = np.zeros((226, 13), dtype='float64')
output_uncert = np.zeros(( 217, 13), dtype='float64')

with open(f'data/{site_name}/{fname}.input', 'rb') as file:
    input_string = file.readlines()
    
for j, row in enumerate(range(5, 228)):
    row_split = split_row(input_string[row])
    if row==7 or row==9:
        row_float = [float_time(x) for x in row_split]
    elif row==16:
        row_float = [ctgs[x] for x in row_split]
    else:
        row_float = [float(x) for x in row_split]
    input_data[j] = row_float
    
for k, row in enumerate(range(229, 446)):
    row_split = split_row(input_string[row])
    row_float = [float(x) for x in row_split]
    input_uncert[k] = row_float
    
        
with open(f'data/{site_name}/{fname}.output', 'rb') as file:
    output_string = file.readlines()
    
m = 0
for row in range(5, 234):
    if 23>row>19:
        continue
    row_split = split_row(output_string[row])
    if row==7 or row==9:
        row_float = [float_time(x) for x in row_split]
    elif row==16:
        row_float = [ctgs[x] for x in row_split]
    else:
        row_float = [float(x) for x in row_split]
    output_data[m] = row_float
    m += 1
    
for n, row in enumerate(range(235, 452)):
    row_split = split_row(output_string[row])
    row_float = [float(x) for x in row_split]
    output_uncert[n] = row_float
    
# np.save(f'matrices/{site_name}/{fname}_input_data.npy', input_data)
# np.save(f'matrices/{site_name}/{fname}_input_uncert.npy', input_uncert)
# np.save(f'matrices/{site_name}/{fname}_output_data.npy', output_data)
# np.save(f'matrices/{site_name}/{fname}_output_uncert.npy', output_uncert)

        
        

