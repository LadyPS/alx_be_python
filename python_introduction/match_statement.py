import random

while True:
    secret_number = random.randint(1,   10)
    guess_count = 0

    print("I'm thinking of a number between 1 and 10. Can you guess it?")

    while True:
        guess = int(input("Your guess: "))
        guess_count += 1

        match guess:
            Case secret_number:
            Print("Congratulation, you guessed it!")
        break
    case _ if guess > secret_number:
    print("Oops, your guess is bit high. Try again!")
    case _ if guess < secret_number:
    print("Nope, your guess is a bit low. Give it another shot!")
    
    play_again = input("play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break