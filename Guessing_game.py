import random

def guessing_game():
    '''This function generates random number between 0 and 100 and takes 
    user input as a guess. Guess is compared with random generated number
    and user is provided an answer weather guess was too high or too low,
    until user enters correct number'''

    print('Please guess the number between 0 and 100')
    generated_random_number = random.randint(0, 100)
    number_guessed = False

    #making sure that input should be of type int
    while(number_guessed == False):
        try:
            user_guess = int(input("Enter your guess: "))
            print("\n")
        except ValueError:
            print("\n", "Please enter digits only", sep = "")
            continue

    #checking wheater input fits in between 0 and 100        
        if (user_guess < 0 or user_guess > 100):
            print("Please enter digits only between 0 and 100")
            continue

    #comparing input with generated number and giving user feedback weather input
    # is too low or too high and if guess is correct exiting while loop        
        if (user_guess < generated_random_number):
            print("Your guess " + str(user_guess) + " is too low")
        elif (user_guess > generated_random_number):
            print("Your guess " + str(user_guess) + " is too high")
        elif (user_guess == generated_random_number):
            print("Your guess " + str(user_guess) + " is just right")
            number_guessed = True


guessing_game()
