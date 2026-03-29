"""List Comprehension"""

"""Basic way to append numbers"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
for i in numbers:
    add_1 = i + 1
    new_list.append(add_1)

"""List Comprehension way"""
#new_list = [new_item for item in list]     #Example of how LC is structured

new_list = [n + 1 for n in numbers]         #A lot less code!!!

name = "Zach"
letters_list = [letter for letter in name]

doubled_list = [n * 2 for n in range(1,5)]

"""Conditional List Comprehension"""

#new_list = [new_item for item in list if test]
names = ['Alex', 'Bob', 'Catherine', 'David', 'Elle', 'Frank']
short_names = [name for name in names if len(name) <= 4]

upper_case_names = [name.upper() for name in names if len(name) >= 5]


"""Dictionary Comprehension"""

#new_dict = {new_key:new_value for item in list}
#new_dict = {new_key:new_value for (key, value) in dict.items()}
#new_dict = {new_key:new_value for (key, value) in dict.items() if test}
import random
student_scores = {student:random.randint(1,100) for student in names}
passed_student = {student:score for (student, score) in student_scores.items() if score > 60}

"""Iterate through Pandas DataFrame"""
import pandas
student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

"""Loop through rows of dataframe"""

#for (index, row) in student_dataframe.iterrows():
    # #print(row)
    # #print(row.student)
    # #pritn(row.score)
    # if row.student == "Alex":
    #     print(row.score)



