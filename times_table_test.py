import random
import time
from operator import itemgetter

highscores = []

# Choose your constraints
MAX_ATTEMPTS = 3
N_QUESTIONS = 5

# Intro and starter
print(f'\nWelcome to the times table test!\nThere are {N_QUESTIONS} questions and {MAX_ATTEMPTS} attempts per questions. Get points for each one correct first try.')
breaker = input('Press ENTER to start the timer. ')

#Set our values and start the clock
while True:
    i = 0
    points = 0
    test = []
    start_time = time.time()

    # Populate our test
    while i < N_QUESTIONS:

        a, b = random.randint(2,12), random.randint(2,12)

        # Duplicate checker
        duplicate = False
        for pair in test:
            if pair[0] == a and pair[1]== b:
                duplicate = True
                break
            elif pair[1] == a and pair[0] == b:
                duplicate = True
                break
        if not duplicate:
            test.append((a, b))
            i += 1
    
    # Loop through questions
    for q in test:
        attempts = 1

        # Ask
        while True:
            response = (input(f'What is {q[0]} x {q[1]}? '))

            # Incase of non-int input
            while type(response) != int:
                try: response = int(response)
                except: response = input(f'Please enter an integer.\n{q[0]} x {q[1]}? ')
            
            # Correct/incorrect & points tallying
            if response == q[0]*q[1] and attempts == 1:
                print('First try!')
                points += 1
                break
            elif response == q[0]*q[1]:
                print('Correct!')
                break
            else:
                if attempts == MAX_ATTEMPTS:
                    print(f'The answer was {q[0]*q[1]}.')
                    break
                else:
                    print(f'Try again.')
                    attempts += 1
                    continue
    
    # End timer
    end_time = time.time()

    # Results
    print(f'{points}/{N_QUESTIONS} points in {round(end_time - start_time, 1)} seconds.')

    # Storing score
    name = input('Please enter your name or initials. ')
    score = [f'{points}/{N_QUESTIONS}', f'{round(end_time - start_time, 1)}sec', name]
    highscores.append(score)

    # Quitter
    quitter = input('Press Q to quit, enter to try again. ')

    if quitter == 'q' or quitter == 'Q':
        break
    else:
        continue

# Sort appropriately
h = sorted(highscores, key=itemgetter(1))
print(f'Highscores: {sorted(h, key=itemgetter(0), reverse=True)}')
print('Goodbye!')

