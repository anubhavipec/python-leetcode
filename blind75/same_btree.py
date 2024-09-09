class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      if p is None and q is None :
          return True
      if p is None and q is not None:
          return False
      if p is not None and q is None:
          return False
      
      if p.val == q.val:
          return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
      else: 
          return False
      
 
    