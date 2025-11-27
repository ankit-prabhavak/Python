# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------------------
# Load the dataset
# -----------------------------------------
df = pd.read_csv("weather_data.csv")

# -----------------------------------------
# Basic data inspection
# -----------------------------------------

# Check dataset information (columns, types, null values)
# print(df.info())

# Get statistical summary for numeric columns
# print(df.describe())

# Get statistical summary for categorical columns
# print(df.describe(include='object'))

# Shape of the dataset (rows, columns)
# print(df.shape)

# Display first 5 rows
# print(df.head())

# Display last 5 rows
# print(df.tail())

# -----------------------------------------
# Duplicate handling
# -----------------------------------------

# Check which rows are duplicates (True/False)
# print(df.duplicated())

# Show only the duplicated rows
# print(df.loc[df.duplicated()])

# Remove duplicates and reindex
# df.drop_duplicates(ignore_index=True, inplace=True)
# print(df.shape)

# -----------------------------------------
# Unique category values
# -----------------------------------------

# Print unique values in the "Month" column
# print("Unique Months:", df['Month'].unique())

# -----------------------------------------
# Find the variance for each numerical column
# -----------------------------------------

# print("\nVariance for each numerical column:")
# print(df.var(numeric_only=True))

# print(df.skew(numeric_only=True))

'''
Write a code to plot a scattor plot of Ozone vs Temperature
'''


# Scatter plot using Seaborn
# plt.figure(figsize=(8, 5))
# sns.scatterplot(data=df, x="Ozone", y="Temp")

# plt.title("Scatter Plot: Ozone vs Temperature")
# plt.xlabel("Ozone Level")
# plt.ylabel("Temperature")

# plt.grid(True)
# plt.show()


'''
Find the month that has highest ozone average
'''
# Find average Ozone per month
# ozone_avg = df.groupby('Month')['Ozone'].mean()

# print("Average Ozone per Month:")
# print(ozone_avg)

# Find month with highest average
# highest_ozone_month = ozone_avg.idxmax()

# print("\nMonth with Highest Average Ozone:", highest_ozone_month)

'''
Q: Group the data by month and compute the average temperature
'''
# avg_temp = df.groupby('Month')['Temp'].mean()

# print("Average Temperature per Month:")
# print(avg_temp)


'''
Q: What are average values of numerical features for sunny weather
'''

# sunny_avg = df[df['Weather'] == 'Sunny'].mean(numeric_only=True)

# print("Average Numerical Values for Sunny Weather:")
# print(sunny_avg)


'''
Q: What are the average values of numerical features for sunny Weather.
'''

# print("Correlation Matrix:")
# print(df.corr(numeric_only=True))

'''
Q: Find the correlation of the given dataset
'''
print(df.corr(numeric_only=True))
# plt.figure(figsize=(10, 6))
# sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
# plt.title("Correlation Heatmap")
# plt.show()

'''
Q: Find the correlation between ozone and solar for days with wind > 10
'''

# Filter rows where Wind > 10
filtered_df = df[df['Wind'] > 10]

# Compute correlation between Ozone and Solar.R
correlation = filtered_df['Ozone'].corr(filtered_df['Solar.R'])

print("Correlation between Ozone and Solar.R for Wind > 10:", correlation)


'''
Q: What is the average temperature during the month of June when the weather is cloudy ?
'''


