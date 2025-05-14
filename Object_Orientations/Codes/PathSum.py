class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0

        def countPathsFromNode(node, currentSum):
            if not node:
                return 0
            count = 0
            if node.val == currentSum:
                count += 1
            count += countPathsFromNode(node.left, currentSum - node.val)
            count += countPathsFromNode(node.right, currentSum - node.val)
            return count

        return (countPathsFromNode(root, targetSum) +
                self.pathSum(root.left, targetSum) +
                self.pathSum(root.right, targetSum))


# ✅ Build the tree correctly
treeRoot = TreeNode(10)
treeRoot.left = TreeNode(5)
treeRoot.right = TreeNode(-3)
treeRoot.left.left = TreeNode(3)
treeRoot.left.right = TreeNode(2)
treeRoot.right.right = TreeNode(11)
treeRoot.left.left.left = TreeNode(3)
treeRoot.left.left.right = TreeNode(-2)
treeRoot.left.right.right = TreeNode(1)

sol = Solution()
print(sol.pathSum(treeRoot, 8))  # ✅ Output: 3
