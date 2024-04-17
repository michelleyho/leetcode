# 54 Spiral Matrix
# https://leetcode.com/problems/spiral-matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, n-1
        up, down = 0, m-1
        result = []
        
        while len(result) < m*n:
            for c in range(left, right+1):
                result.append(matrix[up][c])
            #print(result)
            
            for r in range(up+1, down+1):
                result.append(matrix[r][right])
            #print(result)
            
            if down != up:
                for c in range(right-1, left-1, -1):
                    result.append(matrix[down][c])
            #print(result)
                
            if left != right:
                for r in range(down-1, up, -1):
                    result.append(matrix[r][left])
            #print(result)
            left += 1
            right -=1
            up +=1
            down -=1
            
            
        
        return result
