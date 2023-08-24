# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.cur_sum = 0

    def traversal(self, node):
        if node is None:
            return

        self.traversal(node.right)
        self.cur_sum += node.val
        node.val = self.cur_sum
        self.traversal(node.left)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
        Time O(n)
        Space O(n)
        反中序遍历然后累加，右中左，用全局变量记录current sum value，此题和538一模一样
        """
        self.traversal(root)

        return root

