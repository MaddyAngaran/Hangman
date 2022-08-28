# This program takes the user through a game of Hangman
# It prompts user for letter guesses and displays that letter on a board if the guess is correct.
# If the guess is incorrect, the stick figure will lose a body part.
# The user has as many tries/incorrect guesses as the man has body parts (6).

import random

# Places correct letter guess in correct location of userAnswer array
def check():
    x = 0
    for letter in guess:
        if letter in h.lower():
            for i in answer:
                if letter == i.lower():
                    if letter == i:
                        userAnswer[x] = f' {letter} '
                    else:
                        userAnswer[x] = f' {letter.upper()} '
                x = x + 1

# Prints out the blank and filled spaces
def board():
    check()
    for i in userAnswer:
        print(i, end=' ')
    print('')
    for i in h:
        if i != ' ':  # print __
            print('‾‾‾', end=' ')
        if i == ' ':
            print('    ', end='')  # spaces with no __
    print('')

# Prints out a circle for the head of the hangman body
def head():
    print('    *  *   ')
    print(' *        * ')
    print('*          *')
    print('*          *')
    print(' *        * ')
    print('    *  *    ')

# prints the full hangman body
def body0():
    x = 0
    head()
    print('     |')
    for i in range(7):
        if i < 3:
            print((' ' * (4 - i)) + '/' + (' ' * i) + '|' + (' ' * i) + '\\' + (' ' * (5 - i)))
        elif i == 3:
            print('     |')
        else:
            print((' ' + ' ' * (7 - i)) + '/' + ' ' * (x) + ' ' + ' ' * (x) + '\\' + (' ' * (7 - i)))
            x = x + 1

# Prints the hangman body after one incorrect guess
def body1():
    x = 0
    head()
    print('     |')
    for i in range(7):
        if i < 3:
            print((' ' * (4 - i)) + '/' + (' ' * i) + '|' + (' ' * i) + '\\' + (' ' * (5 - i)))
        elif i == 3:
            print('     |')
        else:
            print((' ' + ' ' * (7 - i)) + ' ' + ' ' * (x) + ' ' + ' ' * (x) + '\\' + (' ' * (7 - i)))
            x = x + 1

# Prints the hangman body after two incorrect guesses
def body2():
    x = 0
    head()
    print('     |')
    for i in range(4):
        if i < 3:
            print((' ' * (4 - i)) + '/' + (' ' * i) + '|' + (' ' * i) + '\\' + (' ' * (5 - i)))
        else:
            print('     |')

# Prints the hangman body after three incorrect guesses
def body3():
    x = 0
    head()
    print('     |')
    for i in range(4):
        if i < 3:
            print((' ' * (4 - i)) + ' ' + (' ' * i) + '|' + (' ' * i) + '\\' + (' ' * (5 - i)))
        else:
            print('     |')

# Prints the hangman body after four incorrect guesses
def body4():
    x = 0
    head()
    print('     |')
    for i in range(4):
        if i < 3:
            print((' ' * (4 - i)) + ' ' + (' ' * i) + '|' + (' ' * i) + ' ' + (' ' * (5 - i)))
        else:
            print('     |')

# Prints out correct amount of limbs for the amount of incorrect attempts by the user
def body(turn):
    if turn == 0:
        body0()
    elif turn == 1:
        body1()
    elif turn == 2:
        body2()
    elif turn == 3:
        body3()
    elif turn == 4:
        body4()
    elif turn == 5:
        x = 0
        head()
    else:
        pass
    print('')

if __name__ == "__main__":
    # Stores stats outside of loop to keep count of wins and losses until program reruns
    wins = 0
    losses = 0
    choice = 0
    h = ''

    # Arrays of possible game answers
    movies = ['The Notebook', 'The Avengers', 'Fight Club']
    foods = ['Lasagna', 'Sushi', 'French Fries']
    animals = ['Sea Horse', 'Python', 'Great White Shark']

    print('Welcome to hangman!')

    # Runs loop until the user chooses to exit
    while choice != 3:
        while choice != 3:
            print('Would you like to:')
            print('1 - Choose a category')
            print('2 - See stats')
            print('3 - Quit game')
            choice = int(input('Enter choice: '))
            print('')

            if choice == 1:
                print('Would you like:')
                print('1 - Animals')
                print('2 - Movies')
                print('3 - Foods')
                r = int(input('Enter choice: '))
                print('')

                # Saves random item from the array chosen by the user to a variable
                if r == 1:
                    h = animals[random.randint(0, 2)]
                if r == 2:
                    h = movies[random.randint(0, 2)]
                if r == 3:
                    h = foods[random.randint(0, 2)]
                break

            if choice == 2:
                print(f'Wins = {wins}')
                print(f'Losses = {losses}')
                use = input('Press enter to go back to menu: ')
                print('')

        if choice == 3:
            break

        guess = ''
        print('')
        # Array for formatting and displaying correct guesses
        userAnswer = []
        # Array to store correct answer
        answer = []
        # Array to store correct guesses for comparing with answer
        userGuesses = []
        turn = 0

        for i in h:
            # Sets each individual letter of the answer to the answer array
            answer.append(i)
            userAnswer.append('   ')
            userGuesses.append(' ')

        while True:
            board()
            print('')
            guess = input("Enter a letter guess: ")
            print('')
            if guess in h.lower():
                body(turn)
            else:
                turn += 1
                body(turn)
                print(f'There are no {guess}s')
                print('')
            x = 0

            for letter in guess:
                if letter in h.lower():
                    for i in answer:
                        if letter == i.lower():
                            if letter == i:
                                userGuesses[x] = (letter)
                            else:
                                userGuesses[x] = (letter.upper())
                        x = x + 1

            # Runs when user has lost
            if turn >= 6:
                board()
                losses = losses + 1
                print('You lost')
                print(f'The correct answer was ' + h)
                print('')
                print('Would you like to play again?')
                print('1 - Yes')
                print('2 - No')
                choice = int(input('Enter choice: '))
                # changes choice to 3 to exit while loop
                if choice == 2:
                    choice = 3
                print('')
                break

            # Runs when user has won
            if userGuesses == answer:
                wins = wins + 1
                board()
                print('You Won!!')
                print('')
                print('Would you like to play again?')
                print('1 - Yes')
                print('2 - No')
                choice = int(input('Enter choice: '))
                # changes choice to 3 to exit while loop
                if choice == 2:
                    choice = 3
                print('')
                break
