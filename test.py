import unittest
from hangman import *


class WordGameSetupTest(unittest.TestCase):
    def setUp(self):
        self.g = Game()

    def test_easy_difficulty(self):
        with open('easy_hang_words.txt', 'r') as easy_file:
            easy_words = easy_file.read().split("\n")
        target = self.g.word_game_setup('e')
        self.assertIn(target, easy_words)

    def test_normal_difficulty(self):
        with open('normal_hang_words.txt', 'r') as normal_file:
            normal_words = normal_file.read().split("\n")
        target = self.g.word_game_setup('n')
        self.assertIn(target, normal_words)

    def test_hard_difficulty(self):
        with open('hang_words.txt', 'r') as hard_file:
            hard_words = hard_file.read().split("\n")
        target = self.g.word_game_setup('h')
        self.assertIn(target, hard_words)


if __name__ == '__main__':
    unittest.main()
