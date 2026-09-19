# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        temp = TreeNode()
        while q:
            el = q.pop()
            if el.val == subRoot.val:
                if self.isSameTree(el, subRoot):
                    return True
            if el.left:
                q.append(el.left)
            if el.right:
                q.append(el.right)
        return False
    
    def isSameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        if root1 and root2 and root1.val == root2.val:
            return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
        else:
            return False




