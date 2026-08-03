#                    Guess the Number Game ⭐⭐⭐

# Computer secretly chooses a number.
# (For now, hardcode it to something like 27 instead of using random.)
# Keep asking until user guesses correctly.

# After completion print:
# Correct!
# Attempts: X

# Bonus:
# Tell user
#   Too High
#   Too Low

number = 27

def guess_number():
    attempts = 0
    while True:
        no_guessed = input("Guess the number: ").strip()
        attempts += 1
        if no_guessed.isdigit():
            no_guessed = int(no_guessed)
            if no_guessed == number:
                print("Correct!")
                print(f"Attempts: {attempts}")
                break
            elif no_guessed > 50:
                print("Too Hight")

            elif no_guessed < 10:
                print("Too Low")

            else:
                print("Try Again!")
        else:
            print("Enter a number only.")


guess_number()