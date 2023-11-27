import random
number_to_find = random.randrange(0,10)
lives = 3


while lives > 0:
    user_number = int(input("Try a Number :"))
    if user_number == number_to_find :
        print("Victory")
        break
    elif user_number > number_to_find :
        print("Lower number")
        lives -=1
        print(f"Lives = {lives}")
    elif user_number < number_to_find :
        print("Bigger number")
        lives -= 1
        print(f"Lives = {lives}")
