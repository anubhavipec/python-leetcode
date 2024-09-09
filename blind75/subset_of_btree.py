

from tree_utils import TreeNode
from typing import Optional

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if root is not None and subRoot is None:
            return False
        if root is  None and subRoot is not None:
            return False
        else:
            if root.val == subRoot.val:
                return self.isSameTree(root,subRoot)
            else:
                return self.isSubtree(root.left,subRoot) and self.isSubtree(root.right,subRoot)
             
        
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