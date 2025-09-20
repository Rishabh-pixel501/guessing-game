import random
import time
import sys

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

slow_print("Welcome to the Guessing Game", 0.05)
time.sleep(1)
slow_print("Choose a number from 1 to 10 ", 0.05)
time.sleep(1)
slow_print("You have 3 attempts. If you don't get it right... something bad will happen :)", 0.05)

def guessing_game():
    max_attempts = 3
    attempts_made = 0
    computer = random.randint(1, 10)

    messages = [
        "Oh no, wrong number!",
        "Again wrong! I told you to adjust your guess!",
        "That's it..."
    ]

    while attempts_made < max_attempts:
        slow_print("Enter Your Number: ", 0.05)
        try:
            player = int(input())
        except ValueError:
            slow_print("Please enter a valid number!", 0.05)
            continue

        if player > computer:
            print(f"Lower number please. You have {max_attempts - (attempts_made + 1)} attempts left.")
        elif player < computer:
            print(f"Higher number please. You have {max_attempts - (attempts_made + 1)} attempts left.")
        else:
            slow_print(f"You guessed it in {attempts_made + 1} attempts!", 0.05)
            return

        slow_print(messages[attempts_made], 0.1)
        attempts_made += 1

    end_messages = [
        "I warned you many times...",
        "You made me do this.",
        "Say bye-bye to your computer."
    ]
    for msg in end_messages:
        slow_print(msg, 0.1)
        time.sleep(0.8)

    for i in range(5, 0, -1):
        slow_print(f"Deleting System 32 in {i} seconds...", 0.05)
        time.sleep(1)

    slow_print("Just kidding!", 0.05)


guessing_game()
