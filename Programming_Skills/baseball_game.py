# 682 Baseball Game
# https://leetcode.com/problems/baseball-game/
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        data = []
        for op in operations:
            if op == '+':
                data.append(data[-1]+data[-2])
            elif op == 'D':
                data.append(2*data[-1])
            elif op == 'C':
                data.pop()
            else:
                data.append(int(op))
        
        return sum(data)
