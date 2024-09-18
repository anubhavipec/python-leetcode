
from collections import deque
from typing import List,Tuple

class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        def reachable(q):
            out = set()
            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while q :
                i,j = q.popleft()
                if (i,j) in out:
                    continue
                out.add((i,j))
                for move in moves:
                    y,x = i+move[0],j+move[1]
                    if y<0 or y >= m or x<0 or x >=n or heights[y][x] < heights[i][j]:
                        continue
                    q.append((y,x))
            return out
        
        pacific = deque()
        atlantic = deque()
        
        for i in range(m):
            pacific.append((i,0))
            atlantic.append((i,n-1))
        for j in range(n):
            pacific.append((0,j))
            atlantic.append((m-1,j))
        return reachable(pacific).intersection(reachable(atlantic))
        
    
sol = Solution()
sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
    