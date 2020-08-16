from random import choice

class Words:
    """Holds the list of words to be used in the game."""
    
    def __init__(self):
        """Initializes the list of words."""

        self.list = self.load()


    def get_rand_word(self) -> str:
        """Returns a random word from the list of words."""

        return choice(self.list)

        
    def load(self) -> list:
        """Loads words from 'words_alpha.txt'."""
        
        with open('resources/words_alpha.txt') as f:
            words = f.readlines()
        
        return words