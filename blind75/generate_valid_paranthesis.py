from typing import List


'''
   ( )
  ( ) ( )
( )
n-matching paranthesis, n =2 , ()(), (()) 
it will have n/2 (  and n/2 )
'''
def generate_parentheses(n: int) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    res = []
    path: List[str] = []
    def dfs(i,open_paran,close_paran):
        
        if i == 2*n:
            res.append("".join(path))
            return
        
        if open_paran < n:
            path.append("(")
            dfs(i+1,open_paran+1,close_paran)
            path.pop()
        if close_paran < open_paran:
            path.append(")")
            dfs(i+1,open_paran,close_paran+1)
            path.pop()
        
            
    dfs(0,0,0)
    return res

if __name__ == "__main__":
    n = int(input())
    res = generate_parentheses(n)
    for line in sorted(res):
        print(line)
