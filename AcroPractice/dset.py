import numpy as np
import pandas as pd


# Placement Records DataFrame
# Placement_Records = pd.DataFrame({
#     'Year':[2025,2024,2022,2021,2020],
#     'Branch':["CSE","ECE","ME","CE","EE"],
#     'Placed_Students':[300,250,200,150,100],
#     'Company':["Google","Microsoft","Amazon","Meta","Apple"],
#     'Package':[50,45,40,35,30]
#     })


# print("Placement Records DataFrame:\n", Placement_Records)


# filtered_records = Placement_Records.groupby('Year')

# for year, group in filtered_records:
#     print(f"\nYear: {year}\n", group)


# Calculate the sum of placed students for each year
# sum_placed_students = filtered_records['Placed_Students'].sum()

# print("\nSum of placed students for each year:\n", sum_placed_students)

# print(filtered_records.get_group('Meta'))


from matplotlib import pyplot as plt


# plt.plot(Placement_Records['Company'], Placement_Records['Package'])

products_sales = pd.DataFrame({
    "Month": [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ],
    "Facecream": [250, 270, 300, 280, 320, 310, 330, 340, 360, 370, 390, 400],
    "Facewash": [150, 160, 170, 165, 180, 175, 190, 200, 210, 220, 230, 240],
    "Toothpaste": [400, 420, 430, 410, 440, 450, 460, 470, 480, 490, 500, 510],
    "Shampoo": [300, 310, 320, 315, 330, 325, 340, 350, 360, 370, 380, 390],
    "Total-Units": [1100, 1160, 1220, 1170, 1270, 1260, 1320, 1360, 1410, 1450, 1500, 1540],
    "Total-Profits": [22000, 23200, 24400, 23400, 25400, 25200, 26400, 27200, 28200, 29000, 30000, 30800]
})

# products_sales.to_csv("products.csv")


# plt.plot(products_sales["Month"], products_sales["Total-Profits"])
# plt.title("Shop Data")
# plt.xlabel("Months")
# plt.ylabel("Total-Profits")
plt.show()

# Problem: Display the number of units sold per month for each product using multi-line plot

# plt.plot(products_sales["Month"], products_sales["Facecream"], marker = "o")

# plt.plot(products_sales["Month"], products_sales["Toothpaste"], marker = "o")

# plt.plot(products_sales["Month"], products_sales["Shampoo"], marker = "o")

# plt.title("Shop Data")
# plt.xlabel("Monts")
# plt.ylabel("Total Units Sold")
# plt.legend(["Facecream", "Toothpaste", "Shampoo"])
# plt.show()


# Display the total units sold per month and total profit for all months using subplot

# fig, axs = plt.subplots(1, 2)

# axs[0].plot(products_sales["Month"], products_sales["Total-Units"])
# axs[0].set_xlabel("Month")
# axs[0].set_ylabel("Total-Units")
# axs[0].set_title('Units Sales per Month')

# axs[1].plot(products_sales["Month"], products_sales["Total-Profits"], color="g")
# axs[1].set_xlabel("Month")
# axs[1].set_ylabel("Total-Profits")
# axs[1].set_title('Profits Per Month')

# Plot a bar chart of total sales per month. Also find which month has the highest overall sales.

colors = [
    "indigo",
    "blue",
    "green",
    "orange",
    "purple",
    "brown",
    "pink",
    "gray",
    "olive",
    "cyan",
    "magenta",
    "red"
]


# plt.bar(products_sales["Month"], products_sales["Total-Units"], edgecolor= "black", color=colors)
# plt.xlabel("Months")
# plt.ylabel("Total Units Sold")
# plt.title("Sales Per Month")
# plt.grid()

# print("Maximum sales was in the month ",products_sales.loc[products_sales["Total-Units"].idxmax(), "Month"])

# plt.show()


# Compare the sales quarterly

# Plot sales for the first quarter (Jan–Apr)
# fig, axs = plt.subplots(2,2)

# axs[0, 0].plot(products_sales["Month"][:4], products_sales["Total-Units"][:4], color="blue", marker='o')
# axs[0, 0].set_title("Sales Per Quarter (Jan–Apr)")
# axs[0, 0].set_xlabel("Months")
# axs[0, 0].set_ylabel("Total Units Sold")


# axs[0, 1].plot(products_sales["Month"][4:8], products_sales["Total-Units"][4:8], color="blue", marker='o')
# axs[0, 1].set_title("Sales Per Quarter (May–Aug)")
# axs[0, 1].set_xlabel("Months")
# axs[0, 1].set_ylabel("Total Units Sold")

# axs[1, 0].plot(products_sales["Month"][8:12], products_sales["Total-Units"][8:12], color="blue", marker='o')
# axs[1, 0].set_title("Sales Per Quarter (Sepr–Dec)")
# axs[1, 0].set_xlabel("Months")
# axs[1, 0].set_ylabel("Total Units Sold")


# plt.tight_layout()
# plt.show()


# Problem: Show the total profit of each month using histogram...

# plt.hist(products_sales["Total-Profits"], bins=5, edgecolor="black", color="blue")
# plt.xlabel("Total Profits")   
# plt.show()


# Problem: Plot a pie-chart showing the percentage contribution of each category of the shops yearly sales.

yearly_sales = {
    "Facecream": sum(products_sales["Facecream"]),
    "Facewash": sum(products_sales["Facewash"]),
    "Toothpaste": sum(products_sales["Toothpaste"]),
    "Shampoo": sum(products_sales["Shampoo"])
}
# labels = yearly_sales.keys()
# sizes = yearly_sales.values()
# explode = (0, 0, 0.1, 0)  # explode the 1st slice (i.e. 'Facecream')

# colors = ["gold", "yellowgreen", "lightcoral", "lightskyblue"]

# plt.pie(sizes, explode=explode, labels=labels, colors=colors,
#         autopct='%1.1f%%', shadow=True, startangle=140)

# plt.axis('equal')
# plt.title("Yearly Sales")
# plt.show()


import seaborn as sns

# print(sns.get_dataset_names())

# tips = sns.load_dataset('tips')

# print(tips.head())

# print(tips.describe())

# print(tips.info())

# print(tips.tail())

# Problem: Plot a line graph showing the total passengers month wise in the dataset 'flights'

# flights = sns.load_dataset('flights')

# sns.lineplot(data=flights, x="month", y="passengers", hue="year", marker="o")


# plt.title("Total Passengers Month Wise")
# plt.xlabel("Months")
# plt.ylabel("Total Passengers")
# plt.show()


# Problem: From the titanic dataset, find the distribution of passengers by class (pclass)

titanic = sns.load_dataset('titanic')
# sns.countplot(data=titanic, x="pclass", hue="who",  edgecolor="black")
# plt.title("Distribution of Passengers by Class")
# plt.xlabel("Passenger Class")
# plt.ylabel("Number of Passengers")
# plt.show()


# Problem: Show the count of passengers survived

# sns.countplot(data=titanic, x="survived", hue="who",  edgecolor="black")
# plt.title("Count of Passengers Survived")
# plt.xlabel("Survived (0 = No, 1 = Yes)")
# plt.ylabel("Number of Passengers")
# plt.show()


# Box Plot
# sns.boxplot(data=titanic, x="pclass", y="age", hue="who")
# plt.title("Box Plot of Age by Passenger Class")
# plt.xlabel("Passenger Class")
# plt.ylabel("Age")
# plt.show()


# Problem: Compare the fare distribution by class (pclass) using box plot

# sns.boxplot(data=titanic, x="pclass", y="fare", hue="who", showfliers= False)
# plt.title("Box Plot of Fare by Passenger Class")
# plt.xlabel("Passenger Class")
# plt.ylabel("Fare")
# plt.show()

# Violin plot


# Measures of central tendancy
# 1. mean 2. median 3. mode

# Measures of Dispersion
# 1. variance 2. standard deviation 3. range 4. IQR(Inter Quatile Range)


shop = pd.DataFrame({
    "Product": ["Soap", "Shampoo", "Biscuit", "Shoes", "Dress", "Pen", "Notebook"],
    "QA": [10, 5, 20, 10, 15, 20, 18],
    "PA": [25, 120, 10, 1500, 1000, 20, 50],
    "TA": [250, 600, 150, 1000, 1500, 3000, 2500],
    "QB": [8, 6, 15, 12, 13, 25, 20],
    "PB": [30, 100, 15, 1200, 1300, 15, 55],
    "TB": [240, 600, 180, 700, 1300, 3500, 2200],
    "Category": ["Grocery", "Grocery", "Grocery", "Fashion", "Fashion", "Stationary", "Stationary"]
})

# Questions:
'''
1. Compare the mean price of shop A and shop B
'''

# print("Mean of Shop A Price: ", shop["PA"].mean())
# print("Mean of Shop B Price: ", shop["PB"].mean())


''''
2. Which measure would be more suitable for comparing total sales between shop if one product has very high sale.

'''
# print("Shop A Sales:\n", "Mean: ", round(shop["TA"].mean()), "Median: ", shop["TA"].median())
# print("Shop B Sales:\n", "Mean: ", round(shop["TB"].mean()), "Median: ", shop["TB"].median())


'''
3. Identify the product with maximum deviations from mean price
'''


'''
4. Which category has the most consistent pricing.

'''
# We'll use standard deviation as a measure of consistency (lower std = more consistent)

# category_std = shop.groupby("Category")[["PA", "PB"]].std()
# print(category_std)

'''
5. Find the inter quantile range for total sale_A
'''


# Q1 = shop['TA'].quantile(0.25)
# Q3 = shop['TA'].quantile(0.75)

# IQR = Q3-Q1
# print("Interquantile Range For A", IQR)


'''
6. Find the range of product price for shop A 
'''

print(max(shop["PA"])-min(shop["PA"]))


'''
7. Calculate the coefficient of variations for price of shop A

'''

print