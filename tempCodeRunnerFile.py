import pandas as pd
df=pd.read_csv('data.csv')
x=df["Salary"].mean()
y=df["Department"].mode()
df.fillna({"Salary": x},inplace=True)
df.fillna({"Department":y},inplace=NaN)

print(df)