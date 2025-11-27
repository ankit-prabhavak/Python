import numpy as np

# Sample dataset: Each row represents a student, and each column represents scores in different subjects   

scores = np.array([
     [78, 85, 92],
    [65, 70, 68],
    [90, 88, 95],
    [56, 60, 58],
    [80, 75, 82],
    [72, 68, 74],
    [95, 98, 94],
    [60, 62, 65],
    [85, 80, 87],
    [70, 72, 78]
])

# find the average score for each subject
avg_per_subject = np.mean(scores, axis=0)
print("Average score for each subject:", avg_per_subject)

# find the average score per student
avg_per_student = np.mean(scores, axis=1)
print("Average score per student:", avg_per_student)

# find the highest score in each subject
max_per_subject = np.max(scores, axis=0)
print("Highest score in each subject:", max_per_subject)

# find the lowest score in each subject
min_per_subject = np.min(scores, axis=0)
print("Lowest score in each subject:", min_per_subject)


# Advanced operations:

# find which student has the highest total score
total_scores = np.sum(scores, axis=1)
highest_student_idx = np.argmax(total_scores)
print("Student with highest total score: Student", highest_student_idx + 1, "with score", total_scores[highest_student_idx])

# find which subject had the highest average score
highest_avg_subject_idx = np.argmax(avg_per_subject)
print("Subject with highest average score: Subject", highest_avg_subject_idx + 1, "with average", avg_per_subject[highest_avg_subject_idx])

# calculate the standard deviation of scores for each subject
std_per_subject = np.std(scores, axis=0)
print("Standard deviation of scores for each subject:", std_per_subject)

# find all the students who scored above 85 in the first subject
students_above_85_first_subject = np.where(scores[:, 0] > 85)[0] + 1  # +1 for 1-based indexing
print("Students who scored above 85 in the first subject:", students_above_85_first_subject)



# Next Question:
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 30, 22, 35, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Score': [85.5, 90.0, 78.5, 88.0, 92.5]
}

df = pd.DataFrame(data)
print(df)


df.loc[2, 'Score'] = 80.0
print("\nUpdated DataFrame:\n", df)

df.loc[len(df)] = ['Frank', 26, 'San Francisco', 87.0]

print("\nDataFrame after adding a new row:\n", df)

# Append method

new_data = pd.DataFrame({
    'Name': ['Grace', 'Hannah'],
    'Age': [29, 31],
    'City': ['Seattle', 'Boston'],
    'Score': [91.0, 89.5]
})

df = df.append(new_data, ignore_index=True)
print("\nDataFrame after appending new data:\n", df)

# concat method
more_data = pd.DataFrame({
    'Name': ['Ian', 'Jack'],
    'Age': [27, 34],
    'City': ['Miami', 'Denver'],
    'Score': [84.0, 86.5]
})
df = pd.concat([df, more_data], ignore_index=True)
print("\nDataFrame after concatenating more data:\n", df)



# drop method
df = df.drop(index=1)
print("\nDataFrame after dropping row with index 1:\n", df)

# drop method with columns
df = df.drop(columns=['City'])
print("\nDataFrame after dropping 'City' column:\n", df)

# remove duplicates
df = df.append({'Name': 'Alice', 'Age': 24, 'Score': 85.5}, ignore_index=True)
print("\nDataFrame after adding a duplicate row:\n", df)

df = df.drop_duplicates()
print("\nDataFrame after removing duplicates:\n", df)


# rename columns
df = df.rename(columns={'Score': 'Exam Score'})
print("\nDataFrame after renaming 'Score' column to 'Exam Score':\n", df)

# filter rows where Age is greater than 30
filtered_df = df[df['Age'] > 30]
print("\nFiltered DataFrame where Age > 30:\n", filtered_df)


s = df.series([10, 20, 30, 40, 50])
print(s)

# output of pint(s)
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64