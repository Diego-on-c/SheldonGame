import unittest

from SheldonGame import Game


class GameTest(unittest.TestCase):
    def test_if_stone_destroy_scissors(self):
        player1 = 'stone'
        player2 = 'scissors'
        game = Game()
        result = game.calculate(player1, player2)
        self.assertEqual(result, 'win player1')

    def test_if_stone_destroy_lizard(self):
        player1 = 'stone'
        player2 = 'lizard'
        game = Game()
        result = game.calculate(player1, player2)
        self.assertEqual(result, 'win player1')

    def test_if_scissors_destroy_paper(self):
        player1 = 'scissors'
        player2 = 'paper'
        game = Game()
        result = game.calculate(player1, player2)
        self.assertEqual(result, 'win player1')

    def test_if_scissors_destroy_lizard(self):
        player1 = 'scissors'
        player2 = 'lizard'
        game = Game()
        result = game.calculate(player1, player2)
        self.assertEqual(result, 'win player1')

    def test_if_paper_destroy_stone(self):
        player1 = 'paper'
        player2 = 'stone'
        game = Game()
        result = game.calculate(player1, player2)
        self.assertEqual(result, 'win player1')

    def test_if_paper_destroy_spock(self):
        player1 = 'paper'
        player2 = 'spock'
        game = Game()
        result = game.calculate(player1, player2)
        self.assertEqual(result, 'win player1')

    def test_if_spock_destroy_scissors(self):
        player1 = 'spock'
        player2 = 'scissors'
        game = Game()
        result = game.calculate(player1, player2)
        self.assertEqual(result, 'win player1')

    def test_if_spock_destroy_stone(self):
        player1 = 'spock'
        player2 = 'stone'
        game = Game()
        result = game.calculate(player1, player2)
        self.assertEqual(result, 'win player1')

    def test_if_lizard_destroy_spock(self):
        player1 = 'lizard'
        player2 = 'spock'
        game = Game()
        result = game.calculate(player1, player2)
        self.assertEqual(result, 'win player1')

    def test_if_lizard_destroy_paper(self):
        player1 = 'lizard'
        player2 = 'paper'
        game = Game()
        result = game.calculate(player1, player2)
        self.assertEqual(result, 'win player1')

    def test_if_player1_is_equals_player2(self):
        player1 = 'lizard'
        player2 = 'lizard'
        game = Game()
        result = game.calculate(player1, player2)
        self.assertEqual(result, 'tie')


if __name__ == '__main__':
    unittest.main()
