import random


def guess_random_number(tries, start, stop):
    number = random.randint(start, stop)

    while tries != 0:
        print(tries, 'tries remaining.')
        guess = int(input('Guess a number:'))
        if guess == number:
            print('You guessed correctly!')
            return
        elif guess <= number:
            print('Guess higher!')
        elif guess >= number:
            print('Guess lower!')
        tries -= 1
    print('Out of tries. You failed. The number was:', number)


#guess_random_number(5, 0, 10)

def guess_random_num_linear(tries, start, stop):
    number = random.randint(start, stop)
    print('The number is: ', number)
    for n in range(start, stop+1):
        print('Number of tries left:', tries)
        print('Guess:', n)
        if n == number:
            print('The program guessed correctly!')
            return
        else:
            tries -= 1
            if tries == 0:
                print('The program has failed to fuess the correct number.')
                return


#guess_random_num_linear(5, 0, 10)

def guess_random_num_binary(tries, start, stop):
    number = random.randint(start, stop)
    print('The number to guess is:', number)
    guess = (start + stop) // 2
    low = start
    high = stop
    while tries != 0:
        print('Number of tries left:', tries)
        print('Programs guess is:', guess)
        if guess == number:
            print('The program has guess successfully!')
            return
        elif guess <= number:
            low = guess + 1
            print('Guessing higher!')
            guess = (guess + 1 + high) // 2
        elif guess >= number:
            high = guess - 1
            print('Guessing lower!')
            guess = (guess + low) // 2
        tries -= 1
    print('The program failed to guess the number:', number)


guess_random_num_binary(5, 0, 100)
