#!/usr/bin/python3

import pandas as pd
import sys

def couple_rank(file1):
    selected_columns = ['ID', 'MNAIS', 'DEPDOM', 'AGEXACTM', 'AGEXACTP']
    db = pd.read_csv(file1, usecols=selected_columns, index_col='ID')
    col1 = db['AGEXACTM']+db['AGEXACTP']
    db['rank'] = col1.rank(method='dense', ascending=True).astype(int)
    db.to_csv('./data/rank_swapping_db.csv')
    return db

def permutation_d(db_rank, distance):
    print("ok") 
    return db_rank 

if __name__ == "__main__":
    distance = 5
    if len(sys.argv) == 1:
        file1 = './data/filter_db.csv'
        db_rank = couple_rank(file1)
        db_permutation_d = permutation_d(db_rank, distance)
    elif len(sys.argv) == 2:
        file1 = sys.argv[1]
        db_rank = couple_rank(file1)
        db_permutation_d = permutation_d(db_rank, distance)
    else:
        print("0 or 1 argument is accepted, not more")

###BROUILLON

## rank the column AGEXACTM groupby DEPDOM
    #db["rank"] = db.groupby('DEPDOM')['AGEXACTM'].rank("dense", ascending=True).astype(int)

## rank the column AGEXACTM, then AGEXACTP
   # col1 = db['AGEXACTM'].astype(str)
   # col2 = db['AGEXACTP'].astype(str)
   # db['rank'] = db.groupby('DEPDOM').(col1+col2).astype(int).rank(method='dense', ascending=True).astype(int)
