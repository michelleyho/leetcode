# 1275 Find Winner on a Tic Tac Toe Game
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game

offset = [0, 3, 6, 7]
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def update(player_index, index):
            scores[player_index][index] += 1
            
            return scores[player_index][index] == 3
               
        #[r1, r2, r3, , c1, c2, c3, b_diag, f_diag]
        num_players, num_lines = 2, 8
        scores = [[0 for l in range(num_lines)] for p in range(num_players)]
        
        win = False
        for i, (x, y) in enumerate(moves):
            #Row
            win |= update(i%2, x)
            
            #Col
            win |= update(i%2, 3+y)
            #back Diag
            if x==y:
                win |= update(i%2, 6)
            #for Diag
            if x+y == 2:
                win |= update(i%2, 7)
            
            if win: 
                return 'A' if i%2 == 0 else 'B'
        
        return 'Draw' if len(moves) == 9 else 'Pending'
