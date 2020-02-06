import json
import pandas as pd

json_file = "./short_anon_naisdb.csv"
csv_file = "./data/anon_filter_db_csv.csv"
f = open(json_file)

#for line in f:
#   data = json.loads(line)
#   print(data["ID"], data["MNAIS"], data["AGEXACTM"], data["DEPDOM"], data["AGEXACTP"])
 
pd_data = pd.concat([pd.DataFrame(json.loads(line)) for line in f], ignore_index=True)
pd_data = pd_data.drop(columns="_id")

print(pd_data)
#w = open(csv_file, "w+")
pd_data.to_csv(csv_file, index=False, encoding='utf8')

f.close()
