import os
import glob

site_names = ['BSCN', 'BTCN', 'GONA', 'LCFR', 'RVUS']

for site_name in site_names:
    file_paths = glob.glob(f'data/{site_name}/*.*')
    
    for file_path in file_paths:
        name, ext = os.path.splitext(file_path)
        os.rename(file_path, name[:-7]+ext)