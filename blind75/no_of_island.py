from collections import deque
from typing import List


class Solution:
        
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        def get_neighbours(coord):
            row,col = coord
            delta_rows = [-1,0,1,0]
            delta_cols = [0,1,0,-1]
            res = []
            for i in range(len(delta_rows)):
                r = row + delta_rows[i]
                c = col + delta_cols[i]
                
                if 0 <= r < num_rows and 0<= c < num_cols:
                    res.append((r,c))
            return res
            
        
        def bfs(start):
            q = deque([start])
            r,c = start
            grid[r][c] = '0'
            while len(q) > 0:
                node = q.popleft()
                for neighbours in get_neighbours(node):
                    r,c = neighbours
                    if grid[r][c] == '0':
                        continue
                    q.append(neighbours)
                    grid[r][c] = '0'
        
        count = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == '0':
                    continue
                bfs((r,c))
                count += 1
        return count

                                    
        
        