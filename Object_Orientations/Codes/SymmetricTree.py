class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True 
        
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True 
        if not left or not right:
            return False 
        return (left.val == right.val and
                self.isMirror(left.left, right.right) and
                self.isMirror(left.right, right.left))


root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(2, TreeNode(4), TreeNode(3))

sol = Solution()
print(sol.isSymmetric(root))  # Output: True


root2 = TreeNode(1)
root2.left = TreeNode(2, right=TreeNode(3))
root2.right = TreeNode(2, right=TreeNode(3))

print(sol.isSymmetric(root2))  # Output: False
