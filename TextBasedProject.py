# File: TextBasedProject.py
# Name: George Trammell
# Start Date: 9/12/19
# End Date: 
# Desc: 
# Sources: None
# On my honor, I have neither given nor received unauthorized aid.

from time import sleep
import sys

print('\n' * 5)
print(' Hangman! '.center(80, '*'))
print('\n\n\n\nWelcome to a text-based Hangman game! Please either type a word you\'d like a friend to guess,\nor just press \'Enter\' to have the computer generate a word for you.')
userWord = input('\n')
turnCount = 10
answerWord = ''

if userWord == '':
    # Generate Random English Word
    print('We\'ll generate a word for you. Get ready!')
    answerWord = 'constructive'
elif userWord > '':
    # Check if userWord is in English dictionary
    # If it is, return userWord  
    # If it's not, ask them to type another word
    if userWord.isalpha() == True:
        answerWord = userWord.strip().lower()
        print('We\'ll use that word! Let\'s begin.\n\n\n\n')
    else:
        print('That\'s not a valid word! Play by the rules next time.')
        sys.exit(1)
    

sleep(1)
print('Here\'s the board for your word. It has %s letters!' % (len(answerWord)))
board = ['_'] * len(answerWord)

def turn():
    global turnCount
    global answerWord
    global board

    print(*board, sep=' ')
    while turnCount > 0:
        turnCount -= 1
        if turnCount <= 5:
            sleep(1)
            print('\n**Try to guess the word!**')
            print('**Type your guess here, or press \'Enter\' to keep playing.')
            guess = input('\n')
            sleep(1)
            if guess == answerWord:
                print('You won! The word was %s. Thank you for playing!' % (answerWord))
                print('\n\n')
                print('*' * 80)
                sys.exit(1)
            elif guess == '':
                pass
            elif guess != answerWord:
                turnCount -= 1
                print('Nope! A turn has been revoked; you have %s turns remaining. Keep trying!' % (turnCount))

        while True:
            char = input('Pick a character: ')
            if char.isalpha() == True:
                print('\n')
                sleep(1)
                break
            else:
                print('That isn\'t a valid character. Please try again.')

        char = char[0].lower()
        success = 0
        for i in range(len(answerWord)):
            if char == answerWord[i]:
                board[i] = char
                success = 1
                if (i+1) == len(answerWord):
                    print('Good Guess! %s\'s have been revealed.' % (char.upper()))
                    print(*board, sep=' ')
            elif (success == 1) and ((i+1) == len(answerWord)):
                print('Good Guess! %s\'s have been revealed. You have %s more turn(s) left.' % (char.upper(), turnCount))
                print(*board, sep=' ')
            elif (i+1) == len(answerWord):
                print('Sorry! That letter isn\'t in the word. You have %s more turn(s) left.' % (turnCount))
                print(*board, sep=' ')
    if turnCount == 0:
        print('You\'re out of turns! The word was %s. Thanks for playing!' % (answerWord))
turn()

"""
Peer Comments:

The number of turns is wrong sometimes
Sometimes even when the letter is correct it does not switch the letter and the underline
 - Aiyu

Sam: Just make it a different start or make it more clear that you are guessing the word and it would be really cool if you had a huge bank of words to choose from for the computer's generated word. Also, make sure you have your name and comments in the code.



"""