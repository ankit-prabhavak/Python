import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("weather_data.csv")

# print(df.info)
# print(df.describe)

# print(df.describe(include='object'))

# print(df.shape)
# print(df.head())
# print(df.tail())

print(df.duplicated())
# print(df.drop_duplicates())

print(df.loc[df.duplicated()])

df.drop_duplicates(ignore_index=True, inplace=True)
print(df.shape)
















