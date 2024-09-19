from collections import deque
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        o = "O"
        
        n = len(board)
        m = len(board[0])
        
        Q = deque()
        
        for i in range(n):
            if board[i][0] == o:
                Q.append((i,0))
            if board[i][m-1] == o:
                Q.append((i,m-1))
                
        for j in range(m):
            if board[0][j] == o:
                Q.append((0,j))
            if board[n-1][j] == o:
                Q.append((n-1,j))
        
        
        def inbound(i,j):
            return 0<=i<n and 0<=j<m
        
        while Q:
            i,j = Q.popleft()
            board[i][j] = "#"
            
            for ii,jj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if not inbound(ii,jj):
                    continue
                if board[ii][jj] == o:
                    Q.append((ii,jj))
                    
        for i in range(n):
            for j in range(m):
                if board[n][m] == o:
                    board[n][m] = 'X'
                elif board[n][m] == "#":
                    board[n][m] = o
            
                    
                
        
        