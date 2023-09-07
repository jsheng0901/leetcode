from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.total = 0
        self.result = 0

    def pre_traversal(self, node):
        if node is None:
            return
        # 计算树的总和
        self.total += node.val
        self.pre_traversal(node.left)
        self.pre_traversal(node.right)

        return

    def post_traversal(self, node):
        if node is None:
            return 0

        left = self.post_traversal(node.left)
        right = self.post_traversal(node.right)
        # 判断断开那一条边得到的乘积最大
        self.result = max(self.result, left * (self.total - left),
                          right * (self.total - right))
        # 返回子树总和
        return left + right + node.val

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """
        Time O(n)
        Space O(n)
        前序遍历计算出整个树的总和，后续遍历每次判断，断开左子树或者右子树，哪一种情况乘积最大，同时返回当前节点作为子树的总和。
        """
        modulo = 1000000007
        self.pre_traversal(root)
        self.post_traversal(root)

        return self.result % modulo


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.left = node2
node1.right = node3
node2.left = node4
node3.right = node5
s = Solution()
print(s.maxProduct(node1))
