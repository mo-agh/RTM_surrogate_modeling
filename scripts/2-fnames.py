import glob
import os
import pickle

site_names = ['BSCN', 'BTCN', 'GONA', 'LCFR', 'RVUS']

for site_name in site_names:
    input_names = [os.path.splitext(os.path.basename(path))[0] 
              for path in glob.glob(f'data/{site_name}/*.input')]
    output_names = [os.path.splitext(os.path.basename(path))[0] 
               for path in glob.glob(f'data/{site_name}/*.output')]
    print(f'{site_name}:')
    print(f'\tinputs: {len(input_names)}')
    print(f'\toutputs: {len(output_names)}')
    
    final_names = []
    for output_name in output_names:
        if output_name in input_names:
            final_names.append(output_name)
    print(f'\tfinal: {len(final_names)}\n')
    
    with open(f'data/{site_name}_fnames.pkl', 'wb') as pkl_file:
        pickle.dump(final_names, pkl_file)