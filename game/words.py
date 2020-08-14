import random

class Words:
    """This class holds the list of words to be used in the game."""
    
    # List of words.
    __words = load()
    
    @staticmethod
    def get_rand_word() -> str:
        """Returns a random word from the list of words."""
        return random.choice(__words)
        
    
    @staticmethod
    def load() -> list:
        """Loads words from 'words_alpha.txt'."""
        
        with open('../resources/words_alpha.txt') as f:
            words = f.readlines()
        
        return words