#data cleaning
import pandas as pd
df= pd.read_csv("worldcup2022.csv")

#finding missing values and handling
print(df.isnull().sum())

#context of data
"""
print(df.shape)
print(df.info())
print(df.describe())
print(df['possession team1'].head())
"""

#cleaning
print(df.info()) #index 50 and 54 have spacing issue, 25-27 have spacing issue
df.columns.str.strip("'").str.strip()
df.columns = df.columns.str.replace(r'\s+', ' ', regex=True)
df.rename(columns={'completed line breaksteam1': 'completed line breaks team1',
                   'completed defensive line breaksteam1': 'completed defensive line breaks team1'},
          inplace=True)
print(df.columns.tolist())



