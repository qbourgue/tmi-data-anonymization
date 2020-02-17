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
    row['count'] = associated_row['count']

print(db)

def db_count_records(file1):
    selected_columns = ['ID', 'MNAIS', 'DEPDOM', 'AGEXACTM', 'AGEXACTP']
    db = pd.read_csv(file1, usecols=selected_columns, index_col='ID')
    print(db_count)
    db_count.to_csv('./data/db_count.csv')
    return db, db_count

def k_selection(db, db_count, K):
    db_selected = db_count.loc[db_count['count'] >= K]
    db_joined = db.merge(db_selected, on=['AGEXACTM','DEPDOM','AGEXACTP'], how='left')
    print(db_joined)
    # save the db into db_joined.csv
    db_joined.to_csv('./data/db_joined.csv')
    db_final = db_joined[pd.isnull(db_joined['count'])][db.columns]
    # save the db into db_final.csv
    db_final.to_csv('./data/db_final.csv')
    print(db_final)
    return(db_final)
