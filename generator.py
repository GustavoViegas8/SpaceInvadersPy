from alien import Alien
class Generator:
    def __init__(self, game):
        margin = 30  
        width = 50  
        for x in range(margin, game.width - margin, width):
            for y in range(margin, int(game.height / 2), width):
                game.aliens.append(Alien(game, x, y))

