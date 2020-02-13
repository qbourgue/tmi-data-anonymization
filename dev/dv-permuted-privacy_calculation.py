#!/usr/bin/python3

import pandas as pd
import sys

def read_database(file_, file_anon):
    db = pd.read_csv(file_, usecols=['ID','DEPDOM', 'AGEXACTM', 'AGEXACTP'], index_col='ID')
    db_anon = pd.read_csv(file_anon, usecols=['ID','DEPDOM', 'AGEXACTM', 'AGEXACTP'], index_col='ID')
    return db, db_anon

def compute_distance(x,db_anon):
    delta_db = pd.DataFrame()
    print(" X : ", x)
    print(" X age m : ", x.iloc[0]['AGEXACTM'])
    print( 'anon',db_anon.head(10))
    # Absolute difference of attributes Agemere agepere.
    delta_db['d_AgeM'] = abs(db_anon['AGEXACTM'] - x.iloc[0]['AGEXACTM'])
    delta_db['d_AgeP'] = abs(db_anon['AGEXACTP'] - x.iloc[0]['AGEXACTP'])
    # Max betwen the abs dif of agemere and agepere
    delta_db['Max'] = delta_db.max(axis=1)
    print( 'Delta db ', delta_db.head(10))
    # Min of the max distances
    distance = delta_db['Max'].min()
    print("Permutation distance for ",x," is ",distance)





if __name__ == "__main__":
    if len(sys.argv) == 4:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        db, db_anon = read_database(file1, file2)
        index = int(sys.argv[3])
        x = db.loc[[index]]
        compute_distance(x, db_anon)
    else:
        print('Give me two dataset and an index') 
