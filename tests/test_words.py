import unittest

from context import game 
from game.words import WordList, Word

class WordListTestCase(unittest.TestCase):
    """Test case for the 'game.WordList' class."""

    def setUp(self):
        """Creates an instance of 'WordList'."""

        self.words = WordList()

    
    def test_get_rand_word(self):
        """Checks that a word was returned."""

        for i in range(50):
            word = self.words.get_rand_word()
            
            self.assertTrue(word)
    
    
    def test_load(self):
        """
        Checks that the file containing the words was loaded correctly.
        """

        with open('../resources/words_alpha.txt') as f:
            actual_file = f.readlines()

        self.assertListEqual(self.words._WordList__list, actual_file)


class WordTestCase(unittest.TestCase):
    """Test case for the 'game.Word' class."""

    def setUp(self):
        """Sets up words to test."""

        self.std_word = 'responsible'
        self.len_one_word = 'a'
        self.one_uniq_word = 'aaaaaaaaaaa'

    
    def test_init(self):
        """Checks that the 'Word' class was properly instantiated."""

        self.assertEqual(
            self.std_word, Word(self.std_word)._Word__content)
        
        self.assertEqual(
            self.len_one_word, Word(self.len_one_word)._Word__content)

        self.assertEqual(
            self.one_uniq_word, Word(self.one_uniq_word)._Word__content)

    
    def test_get_content(self):
        """Checks that word content is returned correctly."""

        self.assertEqual(self.std_word, Word(self.std_word).get_content())

    
    def test_get_unique_count(self):
        """Checks that the number of unique letters is correctly counted."""

        self.assertEqual(
            9, Word(self.std_word).get_unique_count())
        
        self.assertEqual(
            1, Word(self.len_one_word).get_unique_count())

        self.assertEqual(
            1, Word(self.one_uniq_word).get_unique_count())


    def test_get_letters_sort_freq(self):
        """
        Checks that the list of tuples of letters and their frequency is
        properly sorted. 
        """

        std_word_count = [('e', 2), ('s', 2), ('r', 1), ('p', 1), ('o', 1),
            ('n', 1), ('i', 1), ('b', 1), ('l', 1)]
        len_one_word_count = [('a', 1)]
        one_uniq_word_count = [('a', 11)]

        self.assertListEqual(
            std_word_count,
            Word(self.std_word).get_letters_sort_freq())
        
        self.assertListEqual(
            len_one_word_count, 
            Word(self.len_one_word).get_letters_sort_freq())
        
        self.assertListEqual(
            one_uniq_word_count, 
            Word(self.one_uniq_word).get_letters_sort_freq())


    def test_get_freq_letter_default(self):
        """Checks that the letter with the highest frequency is returned."""

        self.assertEqual('e', Word(self.std_word).get_freq_letter())
        self.assertEqual('a', Word(self.len_one_word).get_freq_letter())
        self.assertEqual('a', Word(self.one_uniq_word).get_freq_letter())


    def test_get_freq_letter_not_default(self):
        """Checks that the letter at the correct index is returned."""

        self.assertEqual('s', Word(self.std_word).get_freq_letter(1))
        self.assertEqual('l', Word(self.std_word).get_freq_letter(8))
        
        
if __name__ == '__main__':
    unittest.main()