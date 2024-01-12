# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diameter = float('-inf')

    def traversal(self, node, depth):
        if node is None:
            return 0

        # 左右子树对应的最大深度
        left = self.traversal(node.left, depth)
        right = self.traversal(node.right, depth)

        # 当前节点的最大直径为左右子树的深度和
        if left + right > self.diameter:
            self.diameter = left + right

        # 返回当前节点的最大深度
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: [TreeNode]) -> float:
        """
        Time O(n) 遍历所有node
        Space O(n) 递归占用
        最大直径为左右子树的最大深度和，同时利用后续遍历返回左右子树的最大深度，记录每个节点的最大深度，同时记录最大diameter。
        """
        if root:
            self.traversal(root, 0)

        return self.diameter


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
s = Solution()
print(s.diameterOfBinaryTree(node1))
