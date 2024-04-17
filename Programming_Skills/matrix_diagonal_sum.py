# 1572 Matrix Diagonal Sum
# https://leetcode.com/problems/matrix-diagonal-sum

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        total = 0
        for i in range(N):
            total += mat[i][i]
            if i != N-1-i:
                total += mat[i][N-1-i]
        
        return total
