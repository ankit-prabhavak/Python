import pandas as pd
import numpy as np
import csv


data = {
    "Serial":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Name":["Ankit", "Ashutosh", "Nikesh", "Anku", "Gaurav", "Dhananjaya", "Satyam", "Vaibhav", "Rohit", "Dev", "Saurabh"],
    "Occupation":["CEH", "ME", "CEO", "Defence", "Tech", "Engg.", "UPSC", "Softy", "SUP", "DS", "Navy"],
    "Contact":["1234567890", "0987654321", "1122334455", "2233445566", "3344556677", "4455667788", "5566778899", "6677889900", "7788990011", "8899001122", "9900112233"]
    }
    

df = pd.DataFrame(data)
# print(df)

df["Age"] =  [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

print(df)

# df = df.set_index("Name")
# first  = df.loc["Ankit"]
# print(first)


# print(df)

# df.info()
# print(df.head())

# df.drop(df.columns[-1], axis = 1, inplace= True)
# print(df)

# df["Occupation"] = ["CEH", "ME", "CEO", "Defence", "Tech", "Engg.", "UPSC", "Softy", "SUP", "DS", "Navy"]
# print(df)




# series = np.array(data["Name"])
# pf = pd.Series(series, name = "Name")

# print(pf)
# print(df)

# gf = pd.DataFrame(petha)
# print(gf)
# petha = [[1,2,3],
#          [4,5,6],
#          [4,9,1]]

# petha = np.array(petha)
# index = petha[[1,2,0], [0,1,1]]

# print(index)

# x = [1 ,2 ,3 ,5]
# y = [1 ,5 ,3, 6,8]


# s = pd.Series(x, name = "X")
# s2 = pd.Series(y, name = "Y")

# print(s)


# t = pd.Series(12)
# print(t)

# Create a Pandas DataFrame from a dictionary

