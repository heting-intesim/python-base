class Game():
    top_score_info = {'player':'','score':0}
    @staticmethod
    def show_help():
        print('帮助信息：\n...\n...')
    
    @classmethod
    def show_top_score(cls):
        print(f'游戏最高记录：[{cls.top_score_info["player"]}] --- {cls.top_score_info["score"]}')
    
    def __init__(self, player_name):
        self.player_name = player_name
    
    def start_game(self):
        print('starting game ...')
        Game.top_score_info['score'] += 1
        Game.top_score_info['player'] = self.player_name

Game.show_help()
g1 = Game('player-A')
g2 = Game('player-B')
for i in range(3):
    g1.start_game()
g2.start_game()
Game.show_top_score()