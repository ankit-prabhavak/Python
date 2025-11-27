# Find the maximum among three numbers
'''def findMax(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    

x = findMax(1, 2, 3)
print(x)  
'''

# Write a program to check whether the given string is palindrome or not.
'''
def checkPalindrome(s):
    return s == "".join(reversed(s))

string = "racecar"
print(checkPalindrome(string)) 
'''

# Write a program to find all prime numbers in the given range.
'''
def findPrime(start, end):  
    
    for i in range(start, end + 1 ):
        if i == 1:
            continue
        elif i == 2:
            print(i)
        else:
            count = 0
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    count += 1
                    
            if count == 0:
                print(i)

findPrime(1, 100)
'''

# Write a program to program to create nested dictionary to store student data and retrieve specific student details.
'''
# Creating a nested dictionary to store student data
students = {
    101: {"name": "John Doe", "age": 15, "grade": "10", "subjects": ["Math", "Science", "English"]},
    102: {"name": "Jane Smith", "age": 14, "grade": "9", "subjects": ["Math", "History", "Art"]},
    103: {"name": "Samuel Brown", "age": 16, "grade": "11", "subjects": ["Chemistry", "Physics", "Biology"]},
    104: {"name": "Emily Davis", "age": 17, "grade": "12", "subjects": ["Literature", "Math", "History"]}
}

# Function to retrieve student details by student ID
def get_student_details(student_id):
    if student_id in students:
        student = students[student_id]
        print(f"Student ID: {student_id}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Grade: {student['grade']}")
        print(f"Subjects: {', '.join(student['subjects'])}")
    else:
        print(f"Student with ID {student_id} not found.")

# Example usage
student_id_to_lookup = 102  # You can change this ID to look up other students
get_student_details(student_id_to_lookup)

'''

# Write a program to print fibonaci series upto a user defined limit.
'''
# There are other ways to do this. We can also use the recursive approach!
def fibonacii(n):
    a = 0
    b = 1

    for i in range(1, n+1):
        if i == 1:
            print(a, end=" ")
        elif i == 2:
            print(b, end=" ")
        else:
            c = a + b
            print(c, end=" ")
            a = b
            b = c

fibonacii(10)
'''
