# 657 Robot Return to Origin
# https://leetcode.com/problems/robot-return-to-origin

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vertical, horizontal = 0, 0
        for m in moves:
            if m == 'U': vertical += 1
            elif m == 'D': vertical -= 1
            elif m == 'R': horizontal += 1
            else: horizontal -= 1
        
        return vertical == horizontal == 0
