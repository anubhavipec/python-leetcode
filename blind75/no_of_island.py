from collections import deque
from typing import List


class Solution:
        
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        def get_neighbours(coord:tuple) -> list:
            row,col = coord
            delta_rows = [-1,0,1,0]
            delta_cols = [0,1,0,-1]
            res = []
            for i in range(len(delta_rows)):
                neighbour_row = row + delta_rows[i];
                neighbour_col = col + delta_cols[i];
                if 0<= neighbour_row <num_rows and 0<= neighbour_col <num_cols:
                    res.append((neighbour_row,neighbour_col))
            return res
        
        def bfs(start):
            
            q = deque([start])            
            r,c = start
            grid[r][c] = '0';
            while len(q) > 0:
                
                node = q.popleft()
                for neighbour in get_neighbours(node):
                    r,c = neighbour
                    if grid[r][c] == '0':
                        continue
                    q.append(neighbour)
                    grid[r][c] = '0'
        
        count = 0
        
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == '0':
                    continue
                bfs((r,c))
                count += 1
        return count
                                    
        
        