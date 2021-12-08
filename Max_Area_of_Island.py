# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# 
# The area of an island is the number of cells with a value 1 in the island.
# 
# Return the maximum area of an island in grid. If there is no island, return 0.
# 
# Example 1:
# 
# Input: grid = 
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,1,1,0,1,0,0,0,0,0,0,0,0],
# [0,1,0,0,1,1,0,0,1,0,1,0,0],
# [0,1,0,0,1,1,0,0,1,1,1,0,0],
# [0,0,0,0,0,0,0,0,0,0,1,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# 
# Example 2:
# 
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
# 
# 


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rl, cl = len(grid), len(grid[0])
        max_area = 0
        
        def get_area(r, c):
            self.area += 1
            grid[r][c] = 0
            neighbors = [[-1,0],[0,-1],[1,0],[0,1]]
            for neighbor in neighbors:
                rd, cd = r + neighbor[0], c + neighbor[1]
                if rd in range(rl) and cd in range(cl) and grid[rd][cd] == 1:
                    get_area(rd, cd)
                    
        for row in range(rl):
            for col in range(cl):
                if grid[row][col] == 1:
                    self.area = 0
                    get_area(row, col)
                    max_area = max(self.area, max_area)
                    
        return max_area
