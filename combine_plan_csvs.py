import os, glob
import pandas as pd
from datetime import date

path = '/Users/brentbuehler/Plans 6.7.20'
os.chdir(path)

all_files = glob.glob(path + "/*.xlsx")
plans = []

for filename in all_files:
    try:
        df = pd.read_excel(filename, index_col=None, header=0)
        plans.append(df)
    except:
        print("Error, could not read", filename)
        continue

concatenated_plans = pd.concat(plans, axis=0, ignore_index=True)
# deduplicated_plans = df.drop_duplicates()
today = str(date.today())
concatenated_plans.to_csv('all_plans_' + today + '.csv', encoding='utf-8')
