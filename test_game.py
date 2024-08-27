import unittest
from unittest.mock import patch
from io import StringIO
import game

class TestGame(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_result(self, mock_stdout):
        game.display_result("rock", "scissors", "You win!")
        self.assertIn("You chose rock. The computer chose scissors. You win!", mock_stdout.getvalue())

    @patch('builtins.input', return_value='yes')
    def test_play_again_yes(self, mock_input):
        self.assertTrue(game.play_again())

    @patch('builtins.input', return_value='no')
    def test_play_again_no(self, mock_input):
        self.assertFalse(game.play_again())

if __name__ == '__main__':
    unittest.main()