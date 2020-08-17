from random import choice

class Words:
    """Holds the list of words to be used in the game."""
    
    def __init__(self):
        """Initializes the list of words."""

        self.list = self.load()


    def get_rand_word(self) -> str:
        """Returns a random word from the list of words."""

        return choice(self.list)

    
    def get_letters_frequency(self, word: str) -> list:
        """
        Returns a list of tuples of letter and its frequency in 'word'. 
        """
        
        # To store letters and their frequency as keys and values,
        # respectively.
        letters_count = dict()
        
        for letter in word:
            if letter in letters_count:
                letters_count[letter] += 1
            else:
                letters_count[letter] = 1
        
        # Sorts 'letters_count' in descending order based on the frequency,
        # not letters.
        letters_count = sorted(
            letters_count.items(), key=lambda x: x[1], reverse=True)

        return letters_count

        
    def load(self) -> list:
        """Loads words from 'words_alpha.txt'."""
        
        with open('resources/words_alpha.txt') as f:
            words = f.readlines()
        
        return words