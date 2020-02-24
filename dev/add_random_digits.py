#!/usr/bin/python3

import pandas as pd
import sys
import numpy as np

K=1
file1 = './data/filter_db.csv'
f_output1 = './data/filter_db_'+str(K)+'random_digits.csv'
selected_columns = ['ID', 'MNAIS', 'DEPDOM', 'AGEXACTM', 'AGEXACTP']
db_noised = pd.read_csv(file1, usecols=selected_columns, index_col='ID', dtype=str)

db_noised['noise_M'] = (np.random.randint(0, 10**K, db_noised.shape[0]))/(10**K)
db_noised['noise_P'] = (np.random.randint(0, 10**K, db_noised.shape[0]))/(10**K)

print(db_noised)

db_noised['AGEXACTM'] = db_noised['AGEXACTM'].astype(int) + db_noised['noise_M']
db_noised['AGEXACTP'] = db_noised['AGEXACTP'].astype(int) + db_noised['noise_P']

db_noised.drop('noise_M',1,inplace=True)
db_noised.drop('noise_P',1,inplace=True)

print(db_noised)

db_noised.to_csv(f_output1)
