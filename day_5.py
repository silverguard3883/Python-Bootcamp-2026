#Loops

#"For" loops iterate through a data structure one index at a time

meats = ["chicken", "beef", "pork", "fish"]


for meat in meats: #In this case, "meat" is the index variable that changes as the for loop iterates through the list "meats"
    print(meat) #Every time the list is iterated, the index variable changes
    print(meat + " tacos") #Can add output text to change output


student_scores = [100, 90, 95, 98, 64, 78, 58, 86, 89]

total_exam_score = sum(student_scores)
print(total_exam_score)
                            
#The for loop below does the same thing as the "sum" function above
sum = 0
for score in student_scores:
    sum += score
print(sum)

#Max challenge (find the maximum score without using the "max" function)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)


#Range function
for number in range(1,10): #prints a range of numbers
    print(number)
print("\n")
    
for number in range(1,11,3): #prints every 3rd number
    print(number)

#Gauss Challenge - Total all the numbers from 1-100

total = 0
for number in range(1,101):
    total += number
print(total)








