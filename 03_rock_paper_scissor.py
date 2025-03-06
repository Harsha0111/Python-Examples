import random

opponent_score = 0
harsha_score = 0

options = ["rock", "paper", "scissor"]


while True:
    user_wish = input("Enter 'y' to play /'q' to quit: ").lower()

    print(options)
    if user_wish == "y":
        user_input = input("Enter your input: ")

        if user_input not in options:
            print("Please correct option: ")
            continue

        opponent_choice = random.randint(0,2)
        opponent_move = options[opponent_choice]
        # option[0] --> rock, option[1] --> paper, option[2] --> scissor

        if user_input == "rock" and opponent_move == "scissor":
            harsha_score += 1
            print("Harsha won!!")
        elif user_input == "paper" and opponent_move == "stone":
            harsha_score += 1
            print("Harsha won!!")
        elif user_input == "scissor" and opponent_move == "paper":
            harsha_score += 1
            print("Harsha won!!")
        elif user_input == opponent_move:
            print("Tie, try again....")
        else:
            opponent_score += 1
            print("Opponent won!!")
    else:
        print("Your score", harsha_score)
        print("Opponent score", opponent_score)
        print("You wish to quit, Bye!!!")
        break