import random

winning_number = random.randint(1, 10)
attempts = 0

def get_user_answer():
    answer = input("What is your guess?")
    return int(answer)


while attempts <= 3:
    print(winning_number)
    if attempts == 3:
        print("Sorry, better luck next time")
        break
    else:
        print(f"Attempt #{attempts + 1}")
        user_guess = get_user_answer()
        if user_guess == winning_number:
            print("Congrats! You have won.")
            break
        else:
            if user_guess < winning_number:
                print("Sorry, your answer is too low")
            elif user_guess > winning_number:
                print("Sorry, your answer is too high")
            attempts += 1