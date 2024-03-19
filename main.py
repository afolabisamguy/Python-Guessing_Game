import random


def difficulty():
    print('PLease enter the difficulty level')
    print('press 1 for 1 - 100')
    print('press 2 for 1 - 200')
    print('press 3 for 1 - 300')
    print('press 4 for 1 - 400')
    print('press 5 for 1 - 500')
    print('press 6 for 1 - 600')
    print('press 7 for 1 - 700')
    print('press 8 for 1 - 800')
    print('press 9 for 1 - 900')
    print('press 10 for 1 - 1000')
    try:
        diff = int(input())
    except ValueError:
        print('Please enter a valid integer')
    return diff


difficulty = difficulty()


def guessing():
    differ = difficulty * 100
    replay = True
    print('Welcome to Sam\'s Guessing Game')
    print(f'The number is random between 1 to {differ}, guess the number')
    print('You will be informed if the number is greater than or lesser than the number')
    number = random.randrange(1, differ + 1)
    attempt = 0
    while replay:

        try:
            guess_number = int(input())
        except ValueError:
            print('You must enter a number')
        else:
            while guess_number is not number:
                if guess_number > number:
                    print('Your guess is greater than the number')
                    break
                elif guess_number < number:
                    print('Your guess is lesser than the number')
                    break
            attempt += 1
            if guess_number == number:
                print('You\'re correct.. You a somewhat of a genius')
                print(f'It took You {attempt} attempts')
                print('Press Y to play again or N to Quit')
                rep = input()

                if rep == 'y':
                    replay = True
                    number = random.randrange(1, 101)
                    print('Welcome to Sam\'s Guessing Game')
                    print(f'The number is random between 1 to {differ}, guess the number')
                    print('You will be informed if the number is greater than or lesser than the number')
                    attempt = 0

                else:
                    replay = False
                    print('Thanks For playing')


guessing()
