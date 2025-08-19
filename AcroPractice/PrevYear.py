'''
Previous year university question

'''

'''
2-marks questions:
'''
# 1. Predict the output.
# def count(s):
#     for str in s.split():
#         s = "&".join(str)
#         print(s)
#     return s
# print(count("python is fun to learn."))


'''
7-marks questions:
'''

'''
1. Construct a function perfect_square(number) that returns a number if it is a perfect square otherwise it returns -1.
'''
# solution:

# def perfect_square(n):
#     sqr_root = int(n**0.5)

#     if n == sqr_root**2:
#         return n
#     else:
#         return -1
    
# num = 2
# res = perfect_square(num)
# if res != -1:
#      print(f"Yes, {num} is a perfect square.")
# else:
#      print(f"No, {num} is not a perfect square.")
    


'''
2. Construct a program to change the contents of the file by reversing each charater separated by comma.

'''
# solution:

# try:
#     with open("text.txt", "r") as file1:
#         contents = file1.read()
#         contents = contents[::-1]
#         contents = ",".join(contents)
#     with open("text.txt", "w") as file2:
#         file2.write(contents)

# except FileNotFoundError:
#     print("File not found.")

# finally:
#     print("Program executed successfully.")

'''
3. Construct a plot for the following dataset using matplotlib.
'''

# solution:
# import matplotlib.pyplot as plt

# food = ["Meat", "Banana", "Avocado", "Apple", "Orange"]
# calories = [200, 100, 150, 50, 60]
# potassium = [100, 200, 150, 50, 60]
# fat = [10, 5, 7, 2, 3]

# plt.plot(food, calories, label="Calories", marker="o")
# plt.plot(food, potassium, label="Potassium", marker="o")        
# plt.plot(food, fat, label="Fat", marker="o")

# plt.xlabel("Food")
# plt.ylabel("Nutrients")
# plt.title("Nutrients in food")
# plt.legend()
# plt.xticks(rotation=None)
# plt.grid()
# plt.tight_layout()

# plt.show()

'''
4. Define a function removenth(s, n).
'''
# solution:

# def removenth(s, n):
#     if n < 0 or n > len(s):
#         return s
#     else:
#         return s[:n] + s[n+1:]

# s = "Python"
# n = 3
# print(removenth(s, n))

'''
5. Construct a program that accepts a comma separated sequence of words as input and prints the words in a commm-separated sequence after sorting them alphabetically.
'''
# solution:

# def sort_words(s):
#     words = s.split(",")
#     words = [word.strip() for word in words]
#     words.sort()
 
#     return ", ".join(words)

# s = "python, java, c++, c"
# print(sort_words(s))


'''
6. A password verifier program that takes a password as input and checks if it contains at least one uppercase letter, one lowercase letter, one digit, and one special character.
'''

# solution:

# def password_checker(password):
#     abc = False
#     ABC = False
#     num = False
#     special = False

#     if len(password) < 6 or len(password) > 12:
#         return -1
#     else:
#         for char in password:
#             if char.isalpha():
#                 if char.islower():
#                     abc = True
#                 else:
#                     ABC = True
#             elif char.isdigit():
#                 num = True
#             else:
#                 special = True

#         if abc and ABC and num and special:
#             return 1
#         else:
#             return -1
    



# def main():
#     passwords = input("Enter passwords separated by comma: ")
#     passwords = passwords.split(",")
#     passwords = [password.strip() for password in passwords]

#     filter_passwords = ", ".join([password for password in passwords if password_checker(password) != -1])
#     print(filter_passwords)

# main()

'''
7. Construct a function ret_smaller(s) that returns the smallest list from the nested list. if two lists have the same lenght then return the first list that is encountered.
'''
# solution:
# def ret_smaller(lister):
#     smallest = lister[0]

#     for i in lister:
#         if len(i) < len(smallest):
#             smallest = i

#     return smallest

# print(ret_smaller([[1,5,48,4,8], [6,4,6,4], [1,2,3,4,5,6], [1,2,3,4]]))


'''
8. Construct the following filters:
   1. filter all the numbers
   2. filter all the strings starting with vowel
   3. filter all the strings that contain any of the following noun: Agra, Ramesh, Tomato, Patna.
   create a program to implement these filters to clean the text.

'''

# def number(text):
#     return  text.isdigit()

# def start_vowel(text):
#     return text[0].lower() in 'aeiou'

# def nouns(text):
#     nouns = ['agra', 'ramesh', 'tomato', 'patna']
#     return  text.lower() in nouns

# # test the functions
# def filter_text(text):
#      filtered_text = []
#      for word in text:
#          if not number(word) and not start_vowel(word) and not nouns(word):
#              filtered_text.append(word)

#      return filtered_text


# # test the function
# raw = "hello every body i am ramesh and i live in Agra and i am 7 years old."
# print(" ".join(filter_text(raw.split())))

'''
9. Change all the numbers in the file to text. Construct the program for the same.
'''
# solution
# def into_text(num):
#     digit = {
#         '0': 'zero',
#         '1': 'one',
#         '2': 'two',
#         '3': 'three',
#         '4': 'four',
#         '5': 'five',
#         '6': 'six',
#         '7': 'seven',
#         '8': 'eight',
#         '9': 'nine'
#     }

#     if len(num) == 1:
#         return digit[num]
#     else:
#         text = [digit[i] for i in num]
#         return ' '.join(text)
    
# try:
#     with open('text.txt', 'r') as file:
#         data = file.read()
#         data = data.split()

#         for word in data:
            
#             if word.isdigit():
#                 data[data.index(word)] = into_text(word)
#             elif word[:-1].isdigit():
#                 data[data.index(word)] = into_text(word[:-1])+ word[-1]
    

#     with open('text.txt', 'w') as file:
#         file.write(' '.join(data))

# except FileNotFoundError:
#     print("File not found")
# except Exception as e:
#     print(e)
# finally:
#     print("File has been modified")


'''
10. Write a program which accepts a sequence of words separated by whitespace as file input. Print the words composed of digit only.
'''
# solution

# try:
#     with open('text.txt', 'r') as file:
#         data = file.read()
#         data = data.split()

#         for word in data:
#             if word.isdigit():
#                 print(word)

# except FileNotFoundError:
#     print("File not found")
# except Exception as e:
#     print(f"{e}")
# finally:
#     print("Program has been executed")


'''
11. Construct a program to read cities.csv dataset, remove last column and save it in any array. Save the last column to another array. Plot first two columns.
'''
# solution
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data as a dictionary
data = {
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Population': [8419600, 3980400, 2716000],
    'Area': [783.8, 503, 589]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Writing DataFrame to 'cities.csv'
df.to_csv('cities.csv', index=False)

print("Data has been written to cities.csv using pandas")

# Initialize arrays to store the data
city_data = []
last_column_data = []

# Read the CSV file and process data
with open('cities.csv', 'r') as file:
    reader = csv.reader(file)
    
    # Skip the header row
    header = next(reader)
    
    for row in reader:
        # Check if the row has enough columns to avoid IndexError
        if len(row) < 2:  # Ensure the row has at least two columns
            print(f"Skipping row due to insufficient columns: {row}")
            continue  # Skip this row
            
        # Add all columns except the last one to city_data
        city_data.append(row[:-1])
        
        # Add the last column (Area, for example) to last_column_data
        last_column_data.append(row[-1])

# Convert city_data to a numpy array for better handling (optional)
city_data = np.array(city_data)

# print(city_data)
# Extract the first two columns for plotting (e.g., City and Population)
first_column = city_data[:, 0]  # First column (City names)
second_column = city_data[:, 1]  # Second column (Population)

# Plot the first two columns
plt.figure(figsize=(10, 6))
plt.scatter(first_column, second_column, color='blue', label='City vs Population')
plt.xlabel('City')
plt.ylabel('Population')
plt.title('City vs Population Plot')
plt.xticks(rotation=90)  # Rotate city names for better readability
plt.tight_layout()
plt.legend()
# plt.show()

# Now delete the last column in the CSV file
# Step 1: Reload the CSV file using pandas
df = pd.read_csv('cities.csv')

# Step 2: Drop the last column
df.drop(df.columns[-1], axis=1, inplace=True)

# Step 3: Save the updated DataFrame back to the CSV file
df.to_csv('cities.csv', index=False)

print("Last column has been deleted from the CSV file.")

# If you want to see the extracted last column data (e.g., Area)
print("Last column data (Area):", last_column_data)

''' 
12. Calculator using Tkinter
'''

# import tkinter as tk

# def click(button_text):
#     expression = entry.get()
#     entry.delete(0, tk.END)
#     entry.insert(0, button_text + expression)

# def clear():
#     entry.delete(0, tk.END)

# def calculate():
#     try:
#         result = eval(entry.get())
#         entry.delete(0, tk.END)
#         entry.insert(0, str(result))
#     except Exception as e:
#         entry.delete(0, tk.END)
#         entry.insert(0, "Error")


# window = tk.Tk()
# window.title("Calculator")
# window.geometry("300x250")

# entry = tk.Entry(window, width=20, borderwidth=5, font=("Aerial, 14"), relief = "solid")
# entry.grid(row=0, column=0, columnspan=4)

# buttons = [
#           ("1",1,0), ("2",1,1), ("3",1,2), 
#           ("4",2,0), ("5",2,1), ("6",2,2),
#           ("7",3,0), ("8",3,1), ("9",3,2), 
#                      ("0",4,1),
#           ("+",5,0), ("-",5,1), ("*",5,2), 
#           ("/",6,0), ("=",6,1), ("C",6,2),
        
#           ]
    

# for (text, row, column) in buttons:
#     if text == "C":
#         button = tk.Button(window, text=text, width=10, height=3, fg="white", bg="blue", activebackground="red", command=clear)
#     elif text == "=":
#         button = tk.Button(window, text=text, width=10, height=3,fg="white", bg="blue", activebackground="red", command=calculate)
#     else:
#         button = tk.Button(window, text=text, width=10, height=3,fg="white", bg="blue", activebackground="red", command=lambda t=text: click(t))
    
#     button.grid(row=row, column=column)

# window.mainloop()


'''
PU:
1. Write a program to print all primes between a given range.
'''
# solution:

# def is_prime(num):
#     if num == 1:
#         return False
#     elif num == 2:
#         return True
#     else:
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True
    
# def print_primes(start, end):
#     for num in range(start, end + 1):
#         if is_prime(num):
#             print(num, end = " ")
        
# print_primes(1,20)


'''
PU:
2. Write a program to create a nested dictionary to store student data and retrieve specific students details.
'''
# solution:
# Creating a nested dictionary to store student data
# students = {
#     '101': {
#         'name': 'Alice',
#         'age': 20,
#         'courses': ['Math', 'Science', 'English'],
#         'address': '123 Elm Street'
#     },
#     '102': {
#         'name': 'Bob',
#         'age': 22,
#         'courses': ['History', 'Math', 'Art'],
#         'address': '456 Oak Avenue'
#     },
#     '103': {
#         'name': 'Charlie',
#         'age': 21,
#         'courses': ['Physics', 'Chemistry', 'Biology'],
#         'address': '789 Pine Road'
#     }
# }

# # Function to retrieve specific student details
# def get_student_details(student_id):
#     # Check if student exists
#     if student_id in students:
#         student = students[student_id]
#         print(f"Student ID: {student_id}")
#         print(f"Name: {student['name']}")
#         print(f"Age: {student['age']}")
#         print(f"Courses: {', '.join(student['courses'])}")
#         print(f"Address: {student['address']}")
#     else:
#         print("Student not found!")

# # Example of retrieving student details by ID
# student_id = input("Enter the student ID to retrieve details: ")
# get_student_details(student_id)


'''
PU:
3. Write a program to generate fibonaci series up to user defined limits.
'''
# solution:

# def fibonacci(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         if i == 0:
#             print(a, end=" ")
#         elif i == 1:
#             print(b, end=" ")
#         else:
#             c = a + b
#             print(c, end=" ")
#             a = b
#             b = c

# n = int(input("Enter the number of terms: "))
# fibonacci(n)

'''
4. Construct a python program to accept user details(name, age, and email) and display them on the screen using tkinter.
'''
# solution:
# import tkinter as tk

# # Create the main window
# window = tk.Tk()
# window.title("User Details")

# # Create labels for Name, Age, and Email
# tk.Label(window, text="Name:").grid(row=0, column=0, padx=10, pady=5)
# tk.Label(window, text="Age:").grid(row=1, column=0, padx=10, pady=5)
# tk.Label(window, text="Email:").grid(row=2, column=0, padx=10, pady=5)

# # Create variables to store user input
# name = tk.StringVar()
# age = tk.StringVar()
# email = tk.StringVar()

# # Create entry widgets for Name, Age, and Email
# tk.Entry(window, textvariable=name).grid(row=0, column=1, padx=10, pady=5)
# tk.Entry(window, textvariable=age).grid(row=1, column=1, padx=10, pady=5)
# tk.Entry(window, textvariable=email).grid(row=2, column=1, padx=10, pady=5)

# # Label to display feedback
# feedback = tk.Label(window, text="", fg="green")
# feedback.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

# # Function to handle the submit button click
# def submit():
#     # Retrieve the input data
#     user_name = name.get()
#     user_age = age.get()
#     user_email = email.get()

#     # Check if all fields are filled
#     if user_name and user_age and user_email:
#         feedback.config(text=f"Details Submitted: {user_name}, {user_age}, {user_email}")
#     else:
#         feedback.config(text="Please fill out all fields.", fg="red")

# # Create the Submit button
# tk.Button(window, text="Submit", command=submit).grid(row=4, column=1, pady=10)

# # Run the main loop
# window.mainloop()

'''
PU:
5. Write a program to plot a bar chart and a pie chart using matplotlib.
'''
# solution:
# import matplotlib.pyplot as plt

# # Data
# overs = [1, 2, 3, 4, 5, 6]
# runs = [10, 20, 30, 40, 50, 60]


# bar_colors = ['lightblue', 'lightgreen', 'lightcoral', 'gold', 'lightpink', 'lightskyblue']


# # Create subplots
# fig, axs = plt.subplots(1, 2)  # 1 row, 2 columns

# # Bar plot on the first subplot
# axs[0].bar(overs, runs, color=bar_colors)
# axs[0].set_title('Power Play Stats')  # Corrected from .title() to .set_title()
# axs[0].set_xlabel('Overs')  # Corrected from .xlabel() to .set_xlabel()
# axs[0].set_ylabel('Runs')  # Corrected from .ylabel() to .set_ylabel()

# # Pie chart on the second subplot
# axs[1].pie(runs, labels=overs, autopct='%1.1f%%')
# axs[1].set_title("Different Phases")  # Corrected title

# # Show the legend for the pie chart
# axs[1].legend(title="Overs")

# # Display the plot
# plt.tight_layout()  # Adjusts the layout so that everything fits without overlap
# plt.show()

'''
PU:
6. Write a program to visualize random data points using both histogram and a scatter plot.
'''
# solution:
# import matplotlib.pyplot as plt

# # Data: Countries and their corresponding centuries
# country_century = {"AUS": 10, "NZ": 8, "ENG": 12, "SA": 9, "PAK": 11}

# # Create subplots
# fig, axs = plt.subplots(1, 2)

# # Plotting the histogram with the century values
# axs[0].hist(country_century.values(), bins=[8,9,10,11,12], edgecolor='black')  # Define bins for centuries
# axs[0].set_title("Sachin's Centuries")
# axs[0].set_xlabel("Centuries")
# axs[0].set_ylabel("Number of Countries")


# # Creating lists for the country names and century counts
# countries = list(country_century.keys())
# centuries = list(country_century.values())

# # Create a scatter plot

# axs[1].scatter(countries, centuries, color='blue', s=100, edgecolor='black')

# # Adding titles and labels
# axs[1].set_title("Sachin's Centuries by Country")
# axs[1].set_xlabel("Country")
# axs[1].set_ylabel("Number of Centuries")
# # Display the plot
# plt.tight_layout()  # Adjust layout to prevent overlap
# plt.show()

'''
PU:
7. Write a program to create a pandas Dataframe from a csv file and demonstrate the operations like adding a column, deleting a column, and filtering rows.
'''
# solution:
# import pandas as pd
# import csv

# # Reading the CSV file and creating the DataFrame
# with open("cities.csv", "r") as file:
#     reader = csv.reader(file)
#     header = next(reader)  # Reading the header
#     data = [row for row in reader]  # Reading the data rows
#     df = pd.DataFrame(data, columns=header)  # Creating DataFrame
#     print("DataFrame created:")
#     print(df)

# # Example CSV content ("cities.csv"):
# # City,Population,Area
# # New York,8419600,783.8
# # Los Angeles,3980400,503
# # Chicago,2716000,589

# # Add a new column
# df['Income'] = [15000, 20000, 18500,]  # Adding a new column 'Income'
# print("\nDataFrame after adding a new 'Income' column:")
# print(df)

# # Delete a column (for example, 'Area')
# df = df.drop(columns=['Area'])
# print("\nDataFrame after deleting the 'Area' column:")
# print(df)

# # Filter rows where the population is greater than 4000000
# filtered_df = df[df['Population'].astype(int) > 4000000]
# print("\nFiltered DataFrame (Population > 4 million):")
# print(filtered_df)


'''
PU:
8. Write a program to handle exceptions where a user enters a non-integer value, and the program promts them to enter valid integer.
'''

# solution:


# cond = False
# while cond != True:
#     try:
#         num = int(input("Enter an integer: "))
#         cond = True
#         print(f"Entered number was: {num}")
#     except ValueError:
#         print("Please enter a valid integer")
#     finally:
#         print("Program executed successfully")
    
'''
9. Write a program to read a file and display its content. If the file does not exist, display an error message.
'''

# solution:
# try:
#     file = open("file.txt", "r")
#     print(file.read())
#     file.close()

# except FileNotFoundError:
#     print("File not found. Please check the file path and name.")

# finally:
#     print("Program executed successfully")




