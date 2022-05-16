import random


def dice_game():

    high_score = 0
    userInput = 0

    while True:
        print('Current High Score:' + str(high_score))
        print('1) Roll Dice')
        print('2) Leave Game')
        userInput = input('Enter your choice: ')

        if userInput == '1':
            print()
            rollOne = random.randint(1, 6)
            rollTwo = random.randint(1, 6)
            rollTotal = rollOne + rollTwo
            print('You roll a...' + str(rollOne))
            print('You roll a...' + str(rollTwo))
            print()
            print('You have rolled a total of:' + str(rollTotal))
            print()
            if rollTotal > high_score:
                print('New high score!\n')
                high_score = rollTotal
        elif userInput == '2':
            print('Goodbye!')
            break
        else:
            continue


dice_game()
