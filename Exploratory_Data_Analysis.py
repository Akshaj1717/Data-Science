#Do teams that win have significantly more possession that teams that lose?
import pandas as pd
df = pd.read_csv('wc2022_cleaned.csv')

def winner(column):
    if column['number of goals team1'] > column['number of goals team2']:
        return 'winner team1'
    elif column['number of goals team2'] > column['number of goals team1']:
        return 'winner team2'
    else:
        return 'draw'

df['result'] = df.apply(winner, axis=1)

print(df[['team1', 'team2', 'number of goals team1', 'number of goals team2', 'result']].head(10))