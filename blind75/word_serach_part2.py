
from typing import List
from collections import deque

class PrefixNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False
        self.ref = 0
    
    def insert(self,word):
        node =self
        
        for char in word:
            if char not in node.children:
                node.children[char] = PrefixNode()
            node=node.children[char]
            node.ref += 1
        node.end = True
        
    def search(self,word) -> bool:
        node  = self
        
        for char in word:
            if char not in node:
                return False
            node = node.children[char]
        return node.end
    
    def remove(self,word):
        node = self
        node.ref -= 1
        for char in word:
            if char in node.children:
                node=node.children[char]
                node.ref -= 1
        
        
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        n = len(board)
        m = len(board[0])
        
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        result , visit = set(), set()
        trie = PrefixNode()
        for word in words:
            trie.insert(word)
            
        def dfs(r,c,node, word):
            
            if(
                r not in range(n) or
                c not in range(m) or
                board[r][c] not in node.children or
                node.children[board[r][c]].ref < 1 or
                (r,c ) in visit
            ):
                return
            
            visit.add(r,c)
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                node.end = False
                result.add(word)
                trie.remove(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r,c))
            
        for r in range(n):
            for c in range(m):
                dfs(r,c,trie,"")
        return list(result)
            
        
        
        
        
                        