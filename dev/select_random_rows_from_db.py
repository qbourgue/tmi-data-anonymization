import pandas as pd

db_full = pd.read_csv('./data/sdcMicro_rankswapping_k001_1random_digits.csv', index_col='ID', dtype=str)
db_randomized = db_full.sample(n = 100)
db_randomized.to_csv('./data/short-sdcMicro_rankswapping_k001_1random_digits.csv')
