import unittest

from context import game 
from game.words import Words

class WordsTestCase(unittest.TestCase):
    """Test case for the 'game.Words' class."""

    def setUp(self):
        """Creates an instance of the 'Words' class."""

        self.words = Words()

    
    def test_get_rand_word(self):
        """Checks that a word was returned."""

        for i in range(50):
            word = self.words.get_rand_word()
            
            self.assertTrue(word)
    
    
    def test_load(self):
        """
        Checks that the file containing the words was loaded correctly.
        """

        with open('resources/words_alpha.txt') as f:
            actual_file = f.readlines()

        self.assertListEqual(self.words.list, actual_file)


if __name__ == '__main__':
    unittest.main()