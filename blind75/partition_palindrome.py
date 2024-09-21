
from typing import List

def partition(s:str) -> List[List[str]]:
    
    
    res = []
    n = len(s)
    
    def is_palindrome(word):
        return word == word[::-1]
    
    def dfs(start,curr_path):
        
        if start==n:
            res.append(curr_path.copy())
            return
        
        for end in range(start+1,n+1):
            prefix = s[start:end]
            if is_palindrome(prefix):
                dfs(end,curr_path+[prefix])