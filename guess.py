#!/usr/bin/env python3
#
# Number Guessing Game!

def prompt(num):
    # Use this function to ask the user about a guess.
    # This function returns 'H', 'L', or 'C'.
    print(f"My guess: {num}")
    inp = ""
    while inp.upper() not in ['H', 'L', 'C']:
        inp = input(f"Is {num} too (H)igh, too (L)ow, or (C)orrect? ")
    return inp.upper()

def play(max):
    print(f"Think of a number from 1 to {max}.")
    input("When you're ready, press Enter.")

    high = max
    low = 1
    done = False
    count = 0
    
    while high != low and not done:
        count += 1
        guess = int((high + low) / 2)
        inp = prompt(guess)
        if inp == 'H':
            high = guess
        elif inp == 'L':
            low = guess
        else:
            done = True
            print(f"You guessed it in {count} guesses.") 

    if high == low and not done:
        print("You ruled out all the numbers.")


if __name__ == '__main__':
    play(1000)
