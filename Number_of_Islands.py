# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
# Input: grid = [
#  ["1","1","1","1","0"],
#  ["1","1","0","1","0"],
#  ["1","1","0","0","0"],
#  ["0","0","0","0","0"]
# ]
# Output: 1
#
# Example 2:
# Input: grid = [
#  ["1","1","0","0","0"],
#  ["1","1","0","0","0"],
#  ["0","0","1","0","0"],
#  ["0","0","0","1","1"]
# ]
# Output: 3


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rl, cl = len(grid), len(grid[0])
        island_count = 0
        def dfs(r, c):
            neighbors = [[-1,0],[0,-1],[1,0],[0,1]]
            for neighbor in neighbors:
                rd, cd = r + neighbor[0], c + neighbor[1]
                if rd in range(rl) and cd in range(cl) and grid[rd][cd] == "1":
                    grid[rd][cd] = "0"
                    dfs(rd, cd)
            
        for row in range(rl):
            for col in range(cl):
                if grid[row][col] == "1":
                    island_count += 1
                    dfs(row, col)
        return island_count
