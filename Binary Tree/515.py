# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    层序遍历，每次处理同一层的时候找一下最大值
    """
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        result = []
        if root:
            queue.append(root)

        while queue:
            size = len(queue)
            level_max = float('-inf')
            for _ in range(size):
                front = queue.pop(0)
                level_max = max(level_max, front.val)
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
            result.append(level_max)
        return result
