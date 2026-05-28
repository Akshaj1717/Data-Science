#data cleaning
import pandas as pd
df= pd.read_csv("worldcup2022.csv")

#finding missing values and handling
print(df.isnull().sum())

#context of data
print(df.shape)
print(df.info())
print(df.describe())

