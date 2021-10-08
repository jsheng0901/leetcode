# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.min = float('inf')
        self.val = None

    def traversal(self, node, target):
        if node is None:
            return

        if abs(node.val - target) < self.min:
            self.min = abs(node.val - target)
            self.val = node.val

        if node.val < target:
            self.traversal(node.right, target)

        if node.val > target:
            self.traversal(node.left, target)

        return

    def closestValue(self, root: [TreeNode], target: float) -> int:
        """
        O(H) time, H --> tree height
        前序遍历，找到一个path，根据节点的值和target的数值大小，每次判断更新最近的节点的值
        """
        if root:
            self.traversal(root, target)

        return self.val
