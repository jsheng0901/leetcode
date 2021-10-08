# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = float('-inf')

    def traversal(self, node):
        if node is None:
            return (0, 0)

        left_number, left_sum = self.traversal(node.left)
        right_number, right_sum = self.traversal(node.right)

        curr_sum = left_sum + right_sum + node.val
        curr_number = left_number + right_number + 1

        mean = curr_sum / curr_number
        self.res = max(self.res, mean)

        return (curr_number, curr_sum)

    def maximumAverageSubtree(self, root: [TreeNode]) -> float:
        """
        O(n) time, O(n) space
        后续遍历，记录当前节点的个数和总和
        """
        if root:
            self.traversal(root)

        return self.res
