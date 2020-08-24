import controller
from words import WordList

# Number of chances given to guess the word.
CHANCES = 6

def main():
    """Runs the game."""

    word_list = WordList()
    
    while True:
        word = word_list.get_rand_word()
        success = controller.Round(word, CHANCES).run()

        # Display the word if it was not guessed.
        if not success:
            print(f'\nThe word was {word}!')
        
        user_input = \
            input("Press ENTER to continue or 'q' or 'Q' to quit: ")
        
        if user_input == 'q' or user_input == 'Q':
            print('Exiting game...')
            break


if __name__ == '__main__':
    main()