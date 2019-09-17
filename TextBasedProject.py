# File: TextBasedProject.py
# Name: George Trammell
# Start Date: 9/12/19
# End Date: 
# Desc:
# Sources: None
# On my honor, I have neither given nor received unauthorized aid.
"""
Idea: Hangman!

Needed Modules: 
- Random word generation from an English dictionary, or
user selected word

- Text art hangman with several art iterations for various mistakes

- Text based interface for selecting and keeping track of selected letters

"""

print(' Hangman! '.center(80, '*'))
print('\n\nWelcome to a text-based Hangman game! Please either \
    type a word you\'d like a friend to guess, or just press \'Enter\' to \
    have the computer generate a word for you.')
userWord = input('\n')
turnCount = 0
answerWord = ''

if userWord == '':
    # Generate Random English Word
    print('We\'ll generate a word for you. Get ready!')
    answerWord = 'randomWord'
elif userWord > '':
    # Check if userWord is in English dictionary
    # If it is, return userWord  
    # If it's not, ask them to type another word
    answerWord = userWord.strip().lower()
    print('We\'ll use that word! Let\'s begin.')

board = ['_'] * len(answerWord)

def turn():
    global turnCount
    global answerWord
    global board

    while turnCount <= 9:
        turnCount += 1
        print('theBoard')
        if turnCount > 3:
            print('Would you like to guess the word? If you\'re wrong, it will cost you a turn!')

        while True:
            char = input('Pick a character: ')
            if char.isalpha() == True:
                print('\n')
                break
            else:
                print('That isn\'t a valid character. Please try again.')

        char = char[0].lower()
        indexChecker = 0
        for i in range(len(answerWord)):
            if char == i:
                board[indexChecker] = char
                print('Good Guess! %s\'s have been revealed.' % (char))
            else:
                print('Sorry! That letter isn\'t in the word. You have %s more turn(s) left.' % (9 - turnCount))
            indexChecker += 1
        # if char in answerWord:
        #     print('Good guess! We\'ll add that to the list.')
turn()
