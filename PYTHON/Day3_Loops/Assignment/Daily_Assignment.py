#Number guessing game 
secret = 7

guess = int(input("Guess the number: "))

while True:

    if guess == secret:
        print("Correct! You guessed the number.")
        break

    elif guess < secret:
        print("Too Low")

    else:
        print("Too High")

    guess = int(input("Guess again: "))