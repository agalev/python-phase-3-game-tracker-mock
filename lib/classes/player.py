from .result import Result
# from game import Game

class Player:
    all = []

    def __init__(self, username):
        if len(username) >= 2 and len(username) <= 16:
            self._username = username
        self.results_list = []
        Player.all.append(self)

    def get_username(self):
        return self._username
    def set_username(self, username):
        if len(username) >= 2 and len(username) <= 16:
            self._username = username
    username = property(get_username, set_username)

    def results(self):
        for result in Result.all:
            if result.player == self and result not in self.results_list:
                self.results_list.append(result)
        return self.results_list
    
    def games_played(self):
        return [result.game for result in self.results() if result.player == self]
    
    def played_game(self, game):
        return game in self.games_played()
    
    def num_times_played(self, game):
        result = None
        result = len([result for result in self.results() if result.game == game])
        return result
    
    def add_result(self, Game, score):
        Result(self, Game, score)

    @classmethod
    def highest_scored(cls, game):
        current_champ = None
        for player in cls.all:
            if current_champ == None and game.average_score(player) > 0:
                current_champ = player
            elif game.average_score(player) > game.average_score(current_champ):
                current_champ = player
        print(current_champ.username)
        return current_champ

# game = Game("Skribbl.io")
# game_2 = Game("Scattegories")
# player = Player('Saaammmm')
# player_2 = Player('ActuallyThomas')
# Result(player, game, 2000)
# Result(player, game_2, 19)
# Result(player, game, 1900)
# Result(player_2, game_2, 9)
    
# import ipdb; ipdb.set_trace()