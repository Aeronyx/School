# File: TextBasedProject.py
# Name: George Trammell
# Start Date: 9/12/19
# End Date: 
# Desc: Problems: mistake count can go below zero, user can't guess word on last mistake, corret letters shouldn't take off mistakes
# Sources: None
# On my honor, I have neither given nor received unauthorized aid.

from time import sleep
from sys import exit
from random import randint

# Word list taken from https://www.hangmanwords.com/words
wordList = 'abruptly absurd abyss affix askew avenue awkward axiom azure bagpipes bandwagon banjo bayou beekeeper bikini blitz blizzard boggle bookworm boxcar boxful buckaroo buffalo buffoon buxom buzzard buzzing buzzwords caliph cobweb cockiness croquet crypt curacao cycle daiquiri dirndl disavow dizzying duplex dwarves embezzle equip espionage euouae exodus faking fishhook fixable fjord flapjack flopping fluffiness flyby foxglove frazzled frizzled fuchsia funny gabby galaxy galvanize gazebo giaour gizmo glowworm glyph gnarly gnostic gossip grogginess haiku haphazard hyphen iatrogenic icebox injury ivory ivy jackpot jaundice jawbreaker jaywalk jazziest jazzy jelly jigsaw jinx jiujitsu jockey jogging joking jovial joyful juicy jukebox jumbo kayak kazoo keyhole khaki kilobyte kiosk kitsch kiwifruit klutz knapsack larynx lengths lucky luxury lymph marquis matrix megahertz microwave mnemonic mystify naphtha nightclub nowadays numbskull nymph onyx ovary oxidize oxygen pajama peekaboo phlegm pixel pizazz pneumonia polka pshaw psyche puppy puzzling quartz queue quips quixotic quiz quizzes quorum razzmatazz rhubarb rhythm rickshaw schnapps scratch shiv snazzy sphinx spritz squawk staff strength strengths stretch stronghold stymied subway swivel syndrome thriftless thumbscrew topaz transcript transgress transplant triphthong twelfth twelfths unknown unworthy unzip uptown vaporize vixen vodka voodoo vortex voyeurism walkway waltz wave wavy waxy wellspring wheezy whiskey whizzing whomever wimpy witchcraft wizard woozy wristwatch wyvern xylophone yachtsman yippee yoked youthful yummy zephyr zigzag zigzagging zilch zipper zodiac zombie'
wordList = wordList.split()

print('\n' * 5)
print(' Hangman! '.center(80, '*'))
print('\n\n\n\nWelcome to a text-based Hangman game! Please either type a word you\'d like a friend to guess,\nor just press \'Enter\' or \'Return\' to have the computer generate a word for you.')
userWord = input('\n')
mistakeCount = 10
answerWord = ''
missedChars = []

if userWord == '':
    # Generate Random English Word
    print('We\'ll generate a word for you. Get ready!')
    answerWord = wordList[randint(0, len(wordList))]
elif userWord > '':
    # Check if userWord is in English dictionary
    # If it is, return userWord  
    # If it's not, ask them to type another word
    if userWord.isalpha() == True:
        answerWord = userWord.strip().lower()
        print('We\'ll use that word! Let\'s begin.' + ('\n' * 10))
    else:
        print('That\'s not a valid word! Play by the rules next time.')
        exit(1)
    

sleep(1)
print('Here\'s the board for your word. It has %s letters!' % (len(answerWord)))
board = ['_'] * len(answerWord)

def turn():
    global mistakeCount
    global answerWord
    global board
    global missedChars

    print(*board, sep=' ')
    while mistakeCount > 0:
        mistakeCount -= 1
        if mistakeCount <= 3:
            sleep(1)
            print('\n**Try to guess the word!**')
            print('**Type your guess here, or press \'Enter\' or \'Return\' to keep playing.')
            guess = input('\n')
            sleep(1)
            if guess == answerWord:
                print('You won! The word was %s. Thank you for playing!\n' % (answerWord))
                print('*' * 80)
                exit(1)
            elif guess == '':
                print(*board, sep=' ')
                print('Missed Letters: ', end='')
                print(*missedChars, sep=', ')
            elif guess != answerWord:
                mistakeCount -= 1
                print('Nope! A turn has been revoked; you have %s mistake(s) remaining. Keep trying!' % (mistakeCount))

        while True:
            char = input('\nPick a character: ')
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
                    print('Good Guess! %s\'s have been revealed. You have %s mistake(s) left.' % (char.upper(), mistakeCount))
                    print(*board, sep=' ')
                    print('Missed Letters: ', end='')
                    print(*missedChars, sep=', ')

            elif (success == 1) and ((i+1) == len(answerWord)):
                print('Good Guess! %s\'s have been revealed. You have %s mistake(s) left.' % (char.upper(), mistakeCount))
                print(*board, sep=' ')
                print('Missed Letters: ', end='')
                print(*missedChars, sep=', ')
            elif (i+1) == len(answerWord):
                print('Sorry! That letter isn\'t in the word. You have %s mistake(s) left.' % (mistakeCount))
                missedChars.append(char.upper())
                print(*board, sep=' ')
                print('Missed Letters: ', end='')
                print(*missedChars, sep=', ')
    if mistakeCount <= 0:
        print('You\'re out of turns! The word was %s. Thanks for playing!' % (answerWord))
turn()

"""
Peer Comments:

The number of turns is wrong sometimes
Sometimes even when the letter is correct it does not switch the letter and the underline
 - Aiyu

Sam: Just make it a different start or make it more clear that you are guessing the word and it 
would be really cool if you had a huge bank of words to choose from for the computer's generated word.
Also, make sure you have your name and comments in the code.
"""