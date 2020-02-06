import pandas as pd

db_full = pd.read_csv('./data/filter_db.csv', index_col='ID')
db_randomized = db_full.sample(n = 500)
db_randomized.to_csv('./data/db_short.csv')
