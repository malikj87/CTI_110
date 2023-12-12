#David Joshua
#Functions, random numbers, and while loops
#12-07-2023
#CTI-110 P5HW - Math Quiz


#Import random library
import random

#This function displays the main menu
def show_menu():
    print("Welcome to Math Quiz")
    print("MAIN MENU")
    print("-----------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")

#This function adds two random numbers
def add():
    ran1 = random.randint(0, 10)
    ran2 = random.randint(0, 10)
    print(f"{ran1} + {ran2}")
    return (ran1 + ran2)

#This function adds two random numbers
def subtract():
    ran1 = random.randint(0, 10)
    ran2 = random.randint(0, 10)
    print(f"{ran1} - {ran2}")
    return (ran1 - ran2)

#This function simulates the user guessing.
#While the guess is wrong, allow the user to guess again
def guessing(guess, correct_answer):
    num_guesses = 0
    
    while guess != correct_answer:
        num_guesses += 1
        if guess > correct_answer:   #If the user guesses too high
            print("Your guess is too high")
            guess = int(input("Guess again: "))  #represent guess
        else:                        #If the user guesses too low
            print("Your guess is too low")
            guess = int(input("Guess again: "))  #represent guess
    #User answer is correct, the while loop breaks
    print("Your answer is correct!!!!")
    print(f"It took you {num_guesses} incorrect guesses to get it right")
    

#Main Function
def main():
    show_menu()
    user_option = int(input("Please choose 1, 2 or 3 from menu option: "))
    while user_option != 3:
        
        if user_option == 1:
            ran_sum = add()    #represents the correct answer
            my_guess = int(input("What is your guess? "))  #represent guess
            guessing(my_guess, ran_sum)
            print()
            show_menu()
            user_option = int(input("Please choose 1, 2 or 3 from menu option: "))
            
        if user_option == 2:
            ran_sum = subtract()    #represents the correct answer
            my_guess = int(input("What is your guess? "))  #represent guess
            guessing(my_guess, ran_sum)
            print()
            show_menu()
            user_option = int(input("Please choose 1, 2 or 3 from menu option: "))

    #if user_choice == 3, the while loop breaks
    print("Thank you for playing, goodbye!")

#Call the main function
if __name__ == "__main__":
    main()
