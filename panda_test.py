import pandas as pd
import json

df = pd.read_csv('oura_2024-10-28_2024-12-28_trends.csv')
json_str = df.to_json(orient='records')
json_data = json.loads(json_str)

df['date'] = pd.to_datetime(df['date']).dt.date

lowest_score = df['Resting Heart Rate Score'].min()

lowest_score_date = df.loc[df['Resting Heart Rate Score'] == lowest_score, 'date'].values[0]


# print(f'Date: {lowest_score_date}, lowest score: {lowest_score}')
print(json_str)
