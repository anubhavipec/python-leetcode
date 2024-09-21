#how do we know if we have reached a solution? , when we reach len n
# how do we branch (generate possible children)?, each letter is either 'a' or 'b'

from typing import List

def letter_combination(n: int) -> List[str]:
    
    res:List[str] = []
    
    def dfs(start_index:int,path:List[str]):
        
        if start_index == n:
            res.append("".join(path))
            return
        
        for letter in "ab":
            path.append(letter)
            dfs(start_index+1,path)
            path.pop()
    dfs(0,[])
    return res