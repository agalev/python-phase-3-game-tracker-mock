from .result import Result
class Game:
    def __init__(self, title):
        if len(title) > 0:
            self._title = title
        self.results_list = []

    def get_title(self):
        return self._title
    def set_title(self, title):
        print('Cannot set title of game')
    title = property(get_title, set_title)

    def results(self):
        for result in Result.all:
            if result.game == self and result not in self.results_list:
                self.results_list.append(result)
        return self.results_list
    
        
    def games_played(self):
        return [result.game for result in self.results() if result.player == self]
        
    def players(self):
        return [result.player for result in self.results() if result.game == self]
    
    def average_score(self, player):
        scores = [result.score for result in self.results() if result.player == player]
        return sum(scores) / len(scores)