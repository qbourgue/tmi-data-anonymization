#!/usr/bin/python3

import pandas as pd
import sys

def db_count_records(file1):
    selected_columns = ['ID', 'MNAIS', 'DEPDOM', 'AGEXACTM', 'AGEXACTP']
    db = pd.read_csv(file1, usecols=selected_columns, index_col='ID')
    db_count = db.groupby(['DEPDOM','AGEXACTM','AGEXACTP']).size().reset_index(name='count')
    return db, db_count

def k_selection(db, db_count, K):
    db_selected = db_count.loc[db_count['count'] >= K]
    db_joined = pd.merge(db, db_selected, on=['DEPDOM','AGEXACTM','AGEXACTP'], how='left')
    print(db_joined)
    db_final = db_joined[pd.isnull(db_joined['count'])][db.columns]
    print(db_final)
    return(db_final)

if __name__ == "__main__":
    K = 5
    if len(sys.argv) == 1:
        file1 = './data/filter_db.csv'
        db, db_count = db_count_records(file1)
        db_x = k_selection(db, db_count, K)
    elif len(sys.argv) == 2:
        file1 = sys.argv[1]
        db, db_count = db_count_records(file1)
        db_x = k_selection(db, db_count, K)
    else:
        print('0 or 1 argument is accepted, not more')
