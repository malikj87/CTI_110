#David Joshua
#11/30/2023
#Use loop to get user input

from statistics import mean

num_grades = int(input("How many grades will you enter? "))

#Create a list to store the grades entered
grades_list = []

#Get grades from user
for i in range(num_grades):
    grade = float(input(f"Enter grade for Module {i + 1}: "))
    while grade < 0 or grade > 100:
        print("You entered an invalid grade: ")
        grade = float(input(f"Enter grade for Module {i + 1}: "))
    grades_list.append(grade)

print(grades_list)    

''' 
#Get input from the user
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

#Create a list to store the grades entered
grades_list = []

#Add values to the list
grades_list.append(grade1)
grades_list.append(grade2)
grades_list.append(grade3)
grades_list.append(grade4)
grades_list.append(grade5)
grades_list.append(grade6)
'''
#Call methods on the list to get results
list_sum = sum(grades_list)
list_avg = mean(grades_list)
lowest_grade = min(grades_list)
highest_grade = max(grades_list)

#Create a value for spacing
x = " "

#Output to user with f-string
print("\n")
print("------------Results------------")
print("Lowest Grade:", '    ', lowest_grade)
print("Highest Grade:", '   ', highest_grade)
print("Sum of Grades:", '   ', f"{list_sum:.2f}")
print("Average:", '         ', f"{list_avg:.2f}")
print("-------------------------------")





