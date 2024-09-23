
from typing import List
from collections import deque

class PrefixNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False
    
    def insert(self,word):
        node =self
        
        for char in word:
            if char not in node.children:
                node.children[char] = PrefixNode()
            node=node.children[char]
        node.end = True
        
    def search(self,word) -> bool:
        node  = self
        
        for char in word:
            if char not in node:
                return False
            node = node.children[char]
        return node.end
        
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        n = len(board)
        m = len(board[0])
        
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        
        
        
                        