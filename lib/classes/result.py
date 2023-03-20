class Result:
    all = []
    def __init__(self, Player, Game, score):
        self.player = Player
        self.game = Game
        self._score = score
        Result.all.append(self)
    
    def get_score(self):
        return self._score
    def set_score(self, score):
        if score >= 1 and score <= 5000:
            self._score = score
    score = property(get_score, set_score)

    # def get_player(self):
    #     return self._player
    # def set_player(self, player):
    #     if isinstance(player, Player):
    #         self._player = player
    # player = property(get_player, set_player)

    # def get_game(self):
    #     return self._game
    # def set_game(self, game):
    #     if isinstance(game, Game):
    #         self._game = game
    # game = property(get_game, set_game)

