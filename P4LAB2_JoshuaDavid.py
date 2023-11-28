#David Joshua
#11/28/2023
#Use a for loop with the range function

#Get input from the user
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter an integer higher than the first: "))

#if the first number is smaller
if num1 < num2:
    for i in range (num1, num2 +1, 5):
        print(i)

else:
    #print("First number must be smaller")
    #While the input is invalid
    while num1 > num2 or num1 == num2:
       print("First number must be smaller")
       #Get input from the user
       num1 = int(input("Enter an integer: "))
       num2 = int(input("Enter an integer higher than the first: "))
        
    for i in range (num1, num2 + 1, 5):
        print (i)
