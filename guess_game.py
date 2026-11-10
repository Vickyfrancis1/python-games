import random

# The computer picks a secret number and the player has a limited number of tries
secret = random.randint(1, 10)
max_tries = 3
print("I am thinking of a number between 1 and 10. You have", max_tries, "tries.")

guess = 0
tries = 0

# Keep asking untill the player guesses right or runs out of tries
while guess != secret and tries < max_tries:
    # Ask for a number; if the player types something else, ask again
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("Please type a whole number.")
        continue
    tries = tries + 1
    
    #Give a hint
    if guess < secret:
        print("Too low, try again.")
    elif guess > secret:
        print("Too high, try again.")
 
 # Show the result
if guess == secret:
    print("You got it in", tries, "tries!")
else:
    print("Game over. The number was", secret)
        