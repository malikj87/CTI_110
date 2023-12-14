#David Joshua
#11/21/2023
#use else statements

#Get value from user
total_change = int(input("Enter your amount of change: "))

if total_change == 0:
    print("no change")

#Calculate coins needed
num_quarters = total_change // 25
total_change = total_change - (25 * num_quarters)

num_dimes = total_change // 10
total_change = total_change - (10 * num_dimes)

num_nickels = total_change // 5
total_change = total_change - (5 * num_nickels)

num_pennies = total_change // 1
total_change = total_change - (1 * num_pennies)

#Display results
if num_quarters > 0:
    if num_quarters == 1:
        print("Quarter: ", num_quarters)
    else:
        print("Quarters: ", num_quarters)

if num_dimes > 0:
    if num_dimes == 1:
        print("Dime: ", num_dimes)
    else:
        print ("Dimes: ", num_dimes)
    

if num_nickels > 0:
    if num_nickels == 1:
        print("Nickel: ", num_nickels)
    else:
        print("Nickels: ", num_nickels)

if num_pennies > 0:
    if num_pennies == 1:
        print("Penny: ", num_pennies)
    else:
        print("Pennies: ", num_pennies)
