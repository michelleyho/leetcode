# 1232 Check if it is a straight line
# https://leetcode.com/problems/check-if-it-is-a-straight-line

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort()
        delta_x = coordinates[1][0]-coordinates[0][0]
        delta_y = coordinates[1][1]-coordinates[0][1]
        
        for i in range(2, len(coordinates)):
            d_x = coordinates[i][0]-coordinates[i-1][0]
            d_y = coordinates[i][1]-coordinates[i-1][1]
            
            if delta_y*d_x != delta_x*d_y:
                return False
        
        return True
            
