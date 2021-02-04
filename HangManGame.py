import random
HANGMAN_PICS = ['''
    +--+
       |
       |
       |
      ===''', '''
    +--+
    0  |
       |
       |
      ===''', '''
    +--+
    0  |
    |  |
       |
      ===''', '''
    +--+
    0  |
   /|  |
       |
      ===''', '''
    +--+
    0  |
   /|\ |
       |
      ===''', '''
    +--+
    0  |
   /|\ |
   /   |
      ===''', '''
    +--+
    0  |
   /|\ |
   / \ |
      ===''']

words = "ant baboon bear beaver cat clam cobra coyote rabbit ram spider toad trout turtle whale zebra".split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print("Missed Letters:", end="")
    for letter in missedLetters:
        print(letter, end="")
    print()
    blanks = "_" * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    for letter in blanks:
        print(letter, end="")
    print()

def getGuess(alreadyGuessed):
    while True:
        print("guess a letter")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("please enter a single letter")
        elif guess in alreadyGuessed:
            print("you have guessed it, choose again")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("please enter a LETTER")
        else:
            return guess

def playAgain():
    print("play again?")
    return input().lower().startswith("y")

print("HANGMAN")

difficulty = "x"
while difficulty not in ["E", "M", "H"]:
    print("enter difficulty: E - easy, M - medium, H - hard")
    difficulty = input().upper()
if difficulty == "M":
    del HANGMAN_PICS[3]
if difficulty == "H":
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ""
correctLetters = ""
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("yes, the secret word is " + secretWord + "!" )
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print("you have run out of guesses!\nAfter " +
                str(len(missedLetters)) + " missed letters and " +
                str(len(correctLetters)) + " correct guesses, the word was " + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ""
            correctLetters = ""
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
