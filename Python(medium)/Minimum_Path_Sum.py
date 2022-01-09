# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

# Example:
# Input: [[1,3,1], [1,5,1], [4,2,1]]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.




class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        import numpy as np
        row = len(grid)
        col = len(grid[0])
        temp = np.zeros((row,col)).astype('int64')
        temp[0][0] = grid[0][0]
        
        for i in range(1,col):
            temp[0][i] = temp[0][i-1]+grid[0][i]
        for i in range(1,row):
            temp[i][0] = temp[i-1][0] + grid[i][0]
        
        for i in range(1,row):
            for j in range(1,col):
        
                temp[i][j] = min(temp[i][j-1]+ grid[i][j], temp[i-1][j] + grid[i][j])
            
        return temp[-1][-1]
