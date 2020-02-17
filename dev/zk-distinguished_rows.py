#!/usr/bin/python3

import pandas as pd
import sys
from tqdm import tqdm

K = 5
file1 = './data/filter_db.csv'

selected_columns = ['ID', 'MNAIS', 'DEPDOM', 'AGEXACTM', 'AGEXACTP']
db = pd.read_csv(file1, usecols=selected_columns, index_col='ID')

db_count = db.groupby(['AGEXACTM','DEPDOM','AGEXACTP']).size().reset_index(name='count')

db['count'] = 0

for index, row in tqdm(db.iterrows()):
    associated_row = db_count.loc[(db_count['DEPDOM'] == row['DEPDOM']) &(db_count['AGEXACTM'] == row['AGEXACTM']) & (db_count['AGEXACTP'] == row['AGEXACTP'])]
    db['count'].loc[[index]] = associated_row['count'].iloc[0]

print(db)
