from random import choice

class WordList:
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


class Word:
    """Represents an English word."""

    def __init__(self, content: str):
        """Initializes the content of the word."""

        self.__content = content
        
        
    def get_content(self) -> str:
        """Returns the content of the word."""

        return self.__content

        
    def get_unique_count(self) -> int:
        """Returns the number of unique letters."""

        return len(set(self.__content))


    def get_freq_letter(self, index: int=0) -> str:
        """
        Returns the letter with the highest frequency.

        If 'index' is specified, the letter at 'index' of the sorted list of
        tuples of letters and their frequency is returned.
        """

        letters_freq = self.get_letters_sort_freq()

        return letters_freq[index][0]

    
    def get_letters_sort_freq(self) -> list:
        """
        Returns a list of tuples of letter and its frequency in
        descending order based on frequency. 
        """
        
        letters_count = dict()
        
        for letter in self.__content:
            if letter in letters_count:
                letters_count[letter] += 1
            else:
                letters_count[letter] = 1
        
        letters_count = sorted(
            letters_count.items(), key=lambda x: x[1], reverse=True)
            
        return letters_count