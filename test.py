import unittest
from unittest.mock import patch
from hangman import *


class TestChooseGameType(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
        self.g = Game()

    def test_valid_input_w(self):
        print("Type 'w'")
        self.assertEqual(self.g.choose_game_type(), 'w')

    def test_valid_input_p(self):
        print("Type 'p'")
        self.assertEqual(self.g.choose_game_type(), 'p')

    def test_invalid_input_1(self):
        print("Type '1'")
        with self.assertRaises(SystemExit):
            self.g.choose_game_type()

    def test_invalid_input_word(self):
        print("Type 'word'")
        with self.assertRaises(SystemExit):
            self.g.choose_game_type()

    def test_invalid_input_z(self):
        print("Type 'z'")
        with self.assertRaises(SystemExit):
            self.g.choose_game_type()


class WordGameSetupTest(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
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
