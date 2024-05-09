import pandas as pd

df = pd.read_csv('releases.csv')
df['date'] = pd.to_datetime(df['date'])
df.sort_values(by='date', ascending=False, inplace=True)

df.to_json('releases.json', orient='records')

