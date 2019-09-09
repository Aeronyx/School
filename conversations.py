# File: conversations.py
# Name: George Trammell
# Date: 9/8/19
# Desc: Program has a discussion with the user.
# Sources: None
# OMH
from time import sleep

# Initial Greeting
print('Hello! What is your name?')
name = input('Name: ')

# Capitalize name if uncapitalized
name = name[0].upper() + name[1:]
print('Hello %s! \n' %(name))
sleep(1)

# First Question
print('%s, Do you have any pets?' %(name))
sleep(1)

# Response tree for amount of pets 
pets = input('Type \'y\' for Yes and \'n\' for No: ')

# Nested if statement for appropriate response
if pets == 'y':
    print('Wonderful. How many pets? \n')
    sleep(.5)
    petNumber = int(input('Number of pets (integer): '))
    if petNumber > 2:
        print('That\'s a lotta pets! You make me proud.')
    elif petNumber == 2:
        print('I hope you love your duo very much.')
    elif petNumber == 1:
        print('One loving companion is all you need.')
    elif petNumber < 0:
        print('You can\'t have negative pets!')
    print('Thanks for playing!')

# No pets, ask about eye color instead
elif pets == 'n':
    print('\nUnbelieveable. This program is terminated. \n')
    sleep(1)
    print('Kidding. Sorta. What color are your eyes?')
    eyeColor = input('Eye color: ')
    eyeColor = eyeColor[0].upper() + eyeColor[1:]
    sleep(.5)
    print('Processing...')
    sleep(1.5)
    print('%s\'s a beautiful color! You\'ve been redeemed.' %(eyeColor))
    print('Thanks for playing!')
# Incorrect entry
else:
    print('You didn\'t follow instructions! Try again.')