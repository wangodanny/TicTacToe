class State:
     def __init__(self):
         self.players = ["X", "O"]
         self.player = self.players[0]
         self.grid = [[None, None, None], [None, None, None], [None, None, None]]

         def reset(self):
             self.player = self.switch_player(self.player)
             self.grid = [[None, None, None], [None, None, None], [None, None, None]]

         def get_grid_item(self, x, y):
            dict = {
                (-200, 66) : [0,0],
                (-67, 66) : [0,1],
                (66, 66) : [0,2],
                (-200, -67) : [1,0],
                (-67, -67) : [1,1],
                (66, -67): [1,2],
                (-200, -200) : [2,0],
                (-67, 200) : [2,1],
                (66,-200) [2:2]
            }

            return dict[x, y]

         def switch_player(self, player):
            if (player == self.players[0]):
                return self.player[1]
            else:
                return self.player[0]

            
    
