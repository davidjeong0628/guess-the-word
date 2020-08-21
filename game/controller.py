import re
from sys import exit

from words import Word

class Round:
    """
    Represents a round of guessing a word. 
    """

    def __init__(self, word: str, chances: int):
        """Sets up data pertaining to the round."""

        self.__word = Word(word)
        self.__chances = chances
        
        self.__hints = self.__load_hints()

        self.__guessed_letters = self.__load_guessed_letters(
            self.__word.get_letters_sort_freq())

        # Holds incorrect guesses. 
        self.__wrong_letters = list()
        
        self.__active = True
        
        # True iff the word was guessed.
        self.__success = False


    def run(self) -> bool:
        """
        Starts the round. Ends if the word is guessed or chances run out.

        Returns a bool indicating whether the word was guessed.
        """

        while self.__active:
            user_input = self.__get_valid_user_input()
            
            self.__process_input(user_input)
            self.__update_status()
            
            print(79 * '_')
        
        return self.__success


    def __get_valid_user_input(self) -> str:
        """Prompts the user for input until a valid input."""
        
        error = '\nInvalid input!'

        # Loops until valid input.
        while True:
            print(self.__get_prompt())

            try:
                # User may input uppercase letters and all words consist of
                # lowercase letters, so user's input must be made lowercase.
                user_input = input('\n>>> ').lower()
            except (EOFError, KeyboardInterrupt):
                exit()

            # Validates user input.
            if len(user_input) > 1 or len(user_input) <= 0:
                print(f'{error} Enter ONE character.')
                continue 
            elif re.search("[^a-z1-2]", user_input):
                print(f'{error}')
                continue
            # Checks if user's input has already been used as either an
            # incorrect or correct guess.
            elif user_input in self.__wrong_letters \
                    or \
                    (user_input in self.__guessed_letters 
                    and self.__guessed_letters[user_input]):
                
                print('\nLetter already used!')
                continue
            # If there are no hints available, '1' or '2' should not be 
            # inputted.
            elif len(self.__hints) <= 0 and \
                    (user_input == '1' or user_input == '2'):
                
                print(f'{error} No hints available.')
                continue
            elif len(self.__hints) <= 1 and (user_input == '2'):
                print(f'{error} Hint #2 not available.')
                continue
            # User's input was valid.
            else:
                break
        
        return user_input


    def __get_prompt(self) -> str:
        """
        Returns the prompt for input.
        """
        
        num_hints = len(self.__hints)

        prompt = '\nEnter a letter[a-zA-Z]'

        if num_hints > 0:
            prompt += " or '1' for Hint #1"
        
        if num_hints > 1:
            prompt += " or '2' for Hint #2"
        
        prompt += '\n'

        for letter in self.__word.get_content():
            # If the 'letter' has been guessed.
            if self.__guessed_letters[letter]: 
                prompt += letter + ' '
            else:
                prompt += '_ '
        
        prompt += f'\n\nIncorrect letters: {self.__wrong_letters}\n'

        prompt += f'{self.__chances} chances left'

        return prompt


    def __process_input(self, user_input: str):
        """Takes proper actions based on user's input."""
 
        if user_input == '1' or user_input == '2':
            hint_letter = self.__hints.pop(int(user_input) - 1)
            
            # Allows the hint letter to be visible in the next prompt. 
            self.__guessed_letters[hint_letter] = True

            return            
        
        for letter in self.__guessed_letters:
            # If user's input is in the word.
            if user_input == letter:
                self.__guessed_letters[letter] = True
                return
        
        # If user's input is not in the word.
        else:
            self.__wrong_letters.append(user_input)
            self.__chances -= 1


    def __update_status(self):
        """Determines whether the round is still active or not."""

        if self.__chances <= 0:
            self.__active = False
            return

        for letter in self.__guessed_letters:
            # If there are any letters which have not yet been guessed,
            # round should remain active.
            if not self.__guessed_letters[letter]:
                return
        else:
            self.__active = False
        

    def __load_guessed_letters(self, letter_set) -> dict:
        """
        Sets up a dictionary with letters and their guessed status
        as keys and values, respectively.
        """

        guessed_letters = dict()

        for key in letter_set:
            guessed_letters[key[0]] = False

        return guessed_letters


    def __load_hints(self) -> list:
        """
        Returns zero, one, or two hint(s) as a list depending on the number
        of unique characters in the word.

        The hints are a frequently occurring letter in the word.  
        """

        word_uniq_count = self.__word.get_unique_count()
        hints = list()

        if word_uniq_count > 3:
            hints += self.__word.get_freq_letter(),
        
        if word_uniq_count > 6:
            hints += self.__word.get_freq_letter(1),

        return hints