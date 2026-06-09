import pandas as pd
df=pd.read_csv(r"C:\Users\acer\Documents\fazio\tested.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum())
df["Age"]=df["Age"].fillna(df["Age"].mean())
df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])
print(df["Survived"].value_counts())
print(df.groupby("Sex")["Survived"].mean())
print(df.groupby("Pclass")["Survived"].mean())
import matplotlib.pyplot as plt
df["Survived"].value_counts().plot(kind="bar")
plt.title("Survived count")
plt.show()
df["Age"].hist()
plt.title("Age distribution")
plt.show()
import seaborn as sns
sns.countplot(x="sex",hue="Survived",data=df)
plt.show()


