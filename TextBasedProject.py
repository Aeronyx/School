# File: TextBasedProject.py
# Name: George Trammell
# Start Date: 9/12/19
# End Date: 9/25/19
# Desc: A classic hangman game! Complete with text-based board, turn counter, and missed letter tracker.
#       The program allows for either a random word from a list, or a user-generated word for a friend to play.
#       I thought it best to write out some pseudocode before starting on this project fully, and I spent both some
#       class time and personal time making sure I understood how I would tackle the 'board' prior to starting.
#       The game was also initially very difficult, so I changed from a turn-based counter to a mistake-based
#       counter, not punishing the user for correct guesses.
# Sources: https://www.hangmanwords.com/words for list of words
# On my honor, I have neither given nor received unauthorized aid.

from time import sleep
from sys import exit
from random import randint

# Variable definitions
userWord = input('\n')
mistakeCount = 10
answerWord = ''
missedChars = []

def turn(): # Runs main game
    global mistakeCount # Keeps track of the user's incorrect guesses
    global answerWord # The target word
    global board # The printed 'board' that the user sees in terminal
    global missedChars # Keeps track of the user's incorrect guesses as characters in a list

    print('\n', *board, sep=' ') # Prints the board with good formatting
    while mistakeCount > 0: # Loop for most of the game, when the user still has turns left
        if '_' not in board: # Checks if the user has filled out the word on their own
            print(*board, sep=' ')
            print('\nYou won! The word was %s. Thanks for playing!' % (answerWord))
            print('*' * 80)
            exit(1)
        elif mistakeCount <= 3: # Checks if the user has less than three errors remaining, and invites them to try and guess
            sleep(1)
            print('\n**Try to guess the word!**')
            print('**Type your guess here, or press \'Enter\' or \'Return\' to keep playing.**')
            guess = input('\n')
            sleep(1)
            if guess == answerWord:
                print('You won! The word was %s. Thank you for playing!\n' % (answerWord))
                print('*' * 80)
                exit(1)
            elif guess == '': # Allows the user to skip the guess step
                print(*board, sep=' ')
                print('Missed Letters: ', end='')
                print(*missedChars, sep=', ')
            elif guess != answerWord: # Revokes a turn for an incorrect guess
                if mistakeCount >= 2:
                    mistakeCount -= 1
                print('Nope! A turn has been revoked; you have %s mistake(s) remaining. Keep trying!' % (mistakeCount))

        while True: # Loop for picking a valid character
            char = input('\nPick a character: ').strip()
            if (char[0].upper() in missedChars) or (char[0].lower() in board): # Checks to make sure the user hasn't guessed that character before
                print('You already guessed that letter! Pick again.')
            elif char.isalpha() == True: # Makes sure the entered character is valid
                print('\n')
                sleep(1)
                break
            else:
                print('That isn\'t a valid character. Please try again.')

        char = char[0].lower()
        success = 0 # Simple variable to keep track of when a is letter successfully found in the answerWord
        for i in range(len(answerWord)): # Loop to iterate through the answerWord and check if the user's guess is correct
            if char == answerWord[i]:
                board[i] = char # Appends the correctly guessed character to the board
                success = 1
                if (i+1) == len(answerWord): # Edge case: the program encounters a problem if the guessed character is the last letter of answerWord; this solves the issue
                    print('Good Guess! %s\'s have been revealed. You have %s mistake(s) left.' % (char.upper(), mistakeCount))
                    print(*board, sep=' ')
                    print('Missed Letters: ', end='')
                    print(*missedChars, sep=', ')

            elif (success == 1) and ((i+1) == len(answerWord)): # Appends correctly guessed characters to the board
                print('Good Guess! %s\'s have been revealed. You have %s mistake(s) left.' % (char.upper(), mistakeCount))
                print(*board, sep=' ')
                print('Missed Letters: ', end='')
                print(*missedChars, sep=', ')
            elif (i+1) == len(answerWord): # Tells the user that the guess is incorrect, and revokes a turn
                mistakeCount -= 1
                print('Sorry! That letter isn\'t in the word. You have %s mistake(s) left.' % (mistakeCount))
                missedChars.append(char.upper()) # Appends the missed character to the missedChars list
                print(*board, sep=' ')
                print('Missed Letters: ', end='')
                print(*missedChars, sep=', ')
    if mistakeCount <= 0: # End of game
        print('You ran out of turns! You have one last chance to guess the word.\n')
        print(*board, sep=' ')
        print('Missed Letters: ', end='')
        print(*missedChars, sep=', ')
        guess = input('\nGuess: ') # Final guess; reveals word either way
        if guess.strip().lower() == answerWord:
            print('You won! The word was %s. Thanks for playing!' % (answerWord))
            print('*' * 80)
            exit(1)
        else:
            print('\nNope! The word was %s. Thanks for playing!' % (answerWord))
            print('*' * 80)
            exit(1)

# Word list taken from https://www.hangmanwords.com/words
wordList = 'abruptly absurd abyss affix askew avenue awkward axiom azure bagpipes bandwagon banjo bayou beekeeper bikini blitz blizzard boggle bookworm boxcar boxful buckaroo buffalo buffoon buxom buzzard buzzing buzzwords caliph cobweb cockiness croquet crypt curacao cycle daiquiri dirndl disavow dizzying duplex dwarves embezzle equip espionage euouae exodus faking fishhook fixable fjord flapjack flopping fluffiness flyby foxglove frazzled frizzled fuchsia funny gabby galaxy galvanize gazebo giaour gizmo glowworm glyph gnarly gnostic gossip grogginess haiku haphazard hyphen iatrogenic icebox injury ivory ivy jackpot jaundice jawbreaker jaywalk jazziest jazzy jelly jigsaw jinx jiujitsu jockey jogging joking jovial joyful juicy jukebox jumbo kayak kazoo keyhole khaki kilobyte kiosk kitsch kiwifruit klutz knapsack larynx lengths lucky luxury lymph marquis matrix megahertz microwave mnemonic mystify naphtha nightclub nowadays numbskull nymph onyx ovary oxidize oxygen pajama peekaboo phlegm pixel pizazz pneumonia polka pshaw psyche puppy puzzling quartz queue quips quixotic quiz quizzes quorum razzmatazz rhubarb rhythm rickshaw schnapps scratch shiv snazzy sphinx spritz squawk staff strength strengths stretch stronghold stymied subway swivel syndrome thriftless thumbscrew topaz transcript transgress transplant triphthong twelfth twelfths unknown unworthy unzip uptown vaporize vixen vodka voodoo vortex voyeurism walkway waltz wave wavy waxy wellspring wheezy whiskey whizzing whomever wimpy witchcraft wizard woozy wristwatch wyvern xylophone yachtsman yippee yoked youthful yummy zephyr zigzag zigzagging zilch zipper zodiac zombie'
wordList = wordList.split() # Creates a list of words from cited source

print('\n' * 5)
print(' Hangman! '.center(80, '*')) # Title card
print('\n\nWelcome to a text-based Hangman game! Please either type a word you\'d like a friend to guess,\nor just press \'Enter\' or \'Return\' to have the computer generate a word for you.')
userWord = input('\n')

if userWord == '':
    print('We\'ll generate a word for you. Get ready!')
    answerWord = wordList[randint(0, len(wordList))] # Chooses a random word from wordList
elif userWord > '': # Uses user-generated word
    if userWord.isalpha() == True:
        answerWord = userWord.strip().lower()
        print('We\'ll use that word! Let\'s begin.' + ('\n' * 10)) # Moves user-generated word off screen
    else: # Terminates if the user enters an invalid word to begin with
        print('That\'s not a valid word! Play by the rules next time.')
        exit(1)
    

sleep(1)
print('Here\'s the board for your word. It has %s letters!' % (len(answerWord)))
board = ['_'] * len(answerWord)

turn()

"""
Peer Comments:

Aiyu: The number of turns is wrong sometimes
Sometimes even when the letter is correct it does not switch the letter and the underline
 
 - Fixed both these issues

Sam: Just make it a different start or make it more clear that you are guessing the word and it 
would be really cool if you had a huge bank of words to choose from for the computer's generated word.
Also, make sure you have your name and comments in the code.

 - Added both of these features
"""

"""
Issues:
Code cramming - When I started this project, I had no intention for the entire game to become operable
inside one sole function. The code is therefore hard to follow sometimes, and if I had more time, I would've
liked to refactor the code into multiple, less jam-packed functions.

Lack of ASCII Hangman Art - I intended to add this (and still do!), but I couldn't get it working well
before the submission deadline, so I decided to omit it.

Guessing system - I wanted the user to be able to attempt a guess at the word each turn, however I also didn't
want the user to be punished for accidentally pressing two letters on the keyboard before guessing a 
character, and I couldn't find an effective workaround.
"""