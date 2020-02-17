#!/usr/bin/python3

import pandas as pd
import sys

def db_count_records(file1):
    selected_columns = ['ID', 'MNAIS', 'DEPDOM', 'AGEXACTM', 'AGEXACTP']
    db = pd.read_csv(file1, usecols=selected_columns, index_col='ID', dtype=str)
    db_count = db.groupby(['AGEXACTM','DEPDOM','AGEXACTP']).size().reset_index(name='count')
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
