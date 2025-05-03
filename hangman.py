import random

def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'openai']
    return random.choice(words)

def display_hangman(tries):
    stages = [
        '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
              ===
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
              ===
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
              |
              ===
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
              |
              ===
        ''',
        '''
           -----
           |   |
           O   |
           |   |
              |
              ===
        ''',
        '''
           -----
           |   |
           O   |
              |
              |
              ===
        ''',
        '''
           -----
           |   |
              |
              |
              |
              ===
        '''
    ]
    return stages[6 - tries]

def hangman():
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6

    print("Welcome to Hangman!")
    
    while tries > 0 and word_letters:
        print(display_hangman(tries))
        print("Word: ", ' '.join([letter if letter in guessed_letters else '_' for letter in word]))
        print("Guessed letters:", ' '.join(sorted(guessed_letters)))
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word_letters:
            word_letters.remove(guess)
            print("Correct!")
        else:
            tries -= 1
            print("Wrong! You have", tries, "tries left.")

    print(display_hangman(tries))
    if not word_letters:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Game Over! The word was:", word)

# Run the game
hangman()
