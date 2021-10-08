# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = float('-inf')

    def traversal(self, node):
        if node is None:
            return 0
        # or left = max(self.traversal(node.left), 0) 负数的话直接取0，return 返回上一层的时候就直接取当前node的值
        left = self.traversal(node.left)
        # if left > self.result:
        #     self.result = left
        right = self.traversal(node.right)
        # if right > self.result:
        #     self.reuslt = right
        # 最大值可以由当前节点为新的根节点组成的树，或者left path, right path, or current node val
        new_root_sum = left + right + node.val
        self.result = max(self.result, new_root_sum, node.val, max(left, right) + node.val)

        return max(max(left, right) + node.val, node.val)

    def maxPathSum(self, root: [TreeNode]) -> int:

        if root:
            self.traversal(root)

        return self.result
