import random

print("Welcome to the Guessing Game!")
print("Select a range from one numer to other to make a guess.")
min = int(input("Enter the minimum number: "))
max = int(input("Enter the maximum number: "))
number_to_guess = random.randint(min, max)
lives = 5
guesses = 0
while lives > guesses:
    guess +=1
    guess = int(input(f"Guess a number between {min} and {max}: "))
    
    if guess < number_to_guess:
        print("Too low! Try again.")            
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} in {guesses} tries.")
        