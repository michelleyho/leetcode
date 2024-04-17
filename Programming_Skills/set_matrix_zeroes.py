# 73 Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row0 = matrix[0][0] == 0
        col0 = matrix[0][0] == 0
        M, N = len(matrix), len(matrix[0])
        
        for i in range(M):
            if matrix[i][0] == 0:
                col0 = True
            for j in range(1, N):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        #print(row0, col0, matrix)
        for i in range(1, M):
            for j in range(1,N):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if matrix[0][0]==0:
            #print(row0)
            for j in range(N):
                matrix[0][j] = 0
        if col0:
            for i in range(M):
                matrix[i][0] = 0
    
                    
        return matrix
