import random

random_number_limit = int(input("Enter top range limit: "))

random_number = random.randint(1, random_number_limit)

guess_count = 0
while True:
    guess_count += 1

    user_guess =  int(input("Guess a number: "))

    if random_number == user_guess:
        print("You'r guess is correct!!")
        break
    elif random_number > user_guess:
        print("You'r guess is less than random number ")
    else:
        print("You'r guess is greater than random number ")
        
    continue
