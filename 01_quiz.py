print("Welcom All!!")


user_input = input("Do you want to play: ").lower()


if user_input != "yes":
    print("invalid input")
    quit()
else:
    print("Get ready to play:) ")

score = 0

cpu_input = input("What is CPU..? ").lower()
if cpu_input == "central processing unit":
    print("correct")
    score += 1
else:
    print("Incorrect!!")
    exit

pu_input = input("What is PU..? ").lower()
if pu_input == "processing unit":
    print("correct")
    score += 1
else:
    print("Incorrect!!")
    exit

print("Score " + str(score))
