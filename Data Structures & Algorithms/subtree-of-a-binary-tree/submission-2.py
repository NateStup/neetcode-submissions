# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
      if not t: return True
      if not s: return False

      if self.sameTree(s, t):
        return True

      return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
      
    def sameTree(self, p, q):
      if not p and not q:
          return True
      if not p or not q or p.val != q.val:
        return False

      return(self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right))
        