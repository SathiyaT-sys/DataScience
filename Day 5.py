import pandas as pd
df=pd.read_csv('data.csv')
x=df["Salary"].mean()
y=df["Gender"].mode()
df.fillna({"Salary": x},inplace=True)
df.fillna({"Gender": y},inplace=True)

print(df)


#print(df.fillna(1))
#print(df.sum("Salary",axis=0))
#print(df.columns)
#print(df['Salary'])
#print(df.iloc[2])
#print(df.loc[0,'Age'])

# print (df.isnull().sum())

#sort=df.sort_values(by='Age',ascending=True)
#print(sort)

#fil=df[df['Age']>20]
#print(fil)

#print(df.head())
#print(df.tail())
#print(df.describe())
#print(df.info())


