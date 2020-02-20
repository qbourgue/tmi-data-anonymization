#!/usr/bin/python3

import pandas as pd
import sys
from tqdm import tqdm

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
    delta_db['d_Dep'] = (db_anon['DEPDOM'] != x.iloc[0]['DEPDOM'])*0.5
    
    # Max betwen the abs dif of agemere and agepere
    delta_db['Max'] = delta_db.max(axis=1)
    print( 'Delta db ', delta_db.head(10))
    
    # Min of the max distances
    distance = delta_db['Max'].min()
    print("Permutation distance for ",x," is ",distance)

    # Count 0 distance neighbour
    neighbour = delta_db[delta_db['Max'] == distance]
    print("Neighbour :")
    print(neighbour)
    counter = neighbour.shape[0]
    print('There is ',counter, 'elements at distance ',distance)

def compute_dist_mute(x,db_anon):
    delta_db = pd.DataFrame(columns=['d_AgeM','d_AgeP','d_Dep','Max'])
    
    # Absolute difference of attributes Agemere agepere.
    delta_db['d_AgeM'] = abs(db_anon['AGEXACTM'] - x['AGEXACTM'])
    delta_db['d_AgeP'] = abs(db_anon['AGEXACTP'] - x['AGEXACTP'])
    delta_db['d_Dep'] = (db_anon['DEPDOM'] != x['DEPDOM'])*0.5
    
    # Max betwen the abs dif of agemere and agepere
    delta_db['Max'] = delta_db.max(axis=1)
    
    # Min of the max distances
    distance = delta_db['Max'].min()
    # Count 0 distance neighbour
    neighbour = delta_db[delta_db['Max'] == distance]
    occurence = neighbour.shape[0]
    return distance, occurence

def compute_all_dist(db, db_anon):
    #dist_all_db = pd.DataFrame(columns=['ID', 'MNAIS','AGEXACTM','DEPDOM','AGEXACTP','count','distance','occurence'])
    dist_all_db = db
    dist_all_db['distance'] = 0.0
    dist_all_db['distance'] = dist_all_db['distance'].astype(float)
    dist_all_db['occurence'] = 0
    dist_all_db['occurence'] = dist_all_db['occurence'].astype(int)

    #for index in tqdm(range(db.shape[0])):
    for index, row in tqdm(db.iterrows()):
        x = row
        distance, occurence = compute_dist_mute(x,db_anon)
        dist_all_db.loc[index]['distance'] = distance
        dist_all_db.loc[index]['occurence'] = occurence 
        x['distance'] = distance
        x['occurence'] = occurence 
        print('new x',x)
        print('Id',index,' Distance',distance,'occurence',occurence) 
    db.to_csv("db_distance_occurence.csv")
    

if __name__ == "__main__":
    if len(sys.argv) == 4:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        db, db_anon = read_database(file1, file2)
        index = int(sys.argv[3])
        x = db.loc[[index]]
        compute_distance(x, db_anon)
    elif len(sys.argv) ==3:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        db, db_anon = read_database(file1, file2)
        compute_all_dist(db, db_anon)

    else:
        print('Give me two dataset and an index') 
