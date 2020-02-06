import pandas as pd

columns_selector = ['ID', 'MNAIS', 'AGEXACTM', 'DEPDOM', 'AGEXACTP']

#db_filtered_csv = pd.read_csv('./data/db_short.csv', usecols=columns_selector, index_col='ID')
db_filtered_csv = pd.read_csv('../base_de_donnees/nais2016_id.csv', usecols=columns_selector, index_col='ID')
db_filtered_csv.to_csv('./data/filter_db.csv')

#file = open('./short-nais2016_id.csv')
#reader = csv.reader(file)
#
#db_attributes = next(reader)
#db_selected_columns = { columns_selector[i] : None for i in range(0, len(columns_selector))} 
#
#for attributes in db_selected_columns:
#    if attributes in db_attributes:
#        db_selected_columns[attributes] = db_attributes.index(attributes)
#    else:
#        print('wrong arguments in columns_selector')
#
#print(db_selected_columns)
#
#for column_value in db_selected_columns.items():
#    column_value[1]
