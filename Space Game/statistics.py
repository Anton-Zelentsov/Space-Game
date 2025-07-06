class Statistics():
    def __init__(self):
        self.reset_statistics()
        self.game_run = True
        with open('Best record', 'r') as f:
            self.best_score = int(f.readline())
    def reset_statistics(self):
       self.lazer_gun_life = 3
       self.score = 0