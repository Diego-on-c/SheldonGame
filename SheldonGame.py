class Game:

    def calculate(self, player1, player2):
        if player1 == player2:
            return 'tie'

        if player1 == 'stone' and (player2 == 'scissors' or player2 == 'lizard'):
            return 'win player1'

        if player1 == 'scissors' and (player2 == 'paper' or player2 == 'lizard'):
            return 'win player1'

        if player1 == 'paper' and (player2 == 'stone' or player2 == 'spock'):
            return 'win player1'

        if player1 == 'spock' and (player2 == 'stone' or player2 == 'scissors'):
            return 'win player1'

        if player1 == 'lizard' and (player2 == 'spock' or player2 == 'paper'):
            return 'win player1'

        return 'win player 2'



