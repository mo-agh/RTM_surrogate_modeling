import numpy as np
import pickle
from tqdm import tqdm

with open(f'data/LCFR_fnames.pkl', 'rb') as pkl_file:
    fnames = pickle.load(pkl_file)
    
input_data = []
params_data = []
output_data = []
    
for fname in tqdm(fnames):
    in_file = np.load(f'matrices/LCFR/{fname}_input_data.npy')[list(range(12, 153))+list(range(169, 213))]
    out_file = np.load(f'matrices/LCFR/{fname}_output_data.npy')[list(range(3, 156))+list(range(172, 216))]
    
    for i in range(13):
        if any(in_file[:, i]>9000) or any(out_file[:, i]>9000):
            continue
        input_data.append(in_file[:, i])
        params_data.append(out_file[:12, i])
        output_data.append(out_file[12:, i])
    
input_data = np.asarray(input_data).astype('float32')
params_data = np.asarray(params_data).astype('float32')
output_data = np.asarray(output_data).astype('float32')

np.save('matrices/LCFR_input_data.npy', input_data)
np.save('matrices/LCFR_params_data.npy', params_data)
np.save('matrices/LCFR_output_data.npy', output_data)
