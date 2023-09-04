from typing import Optional, Union


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

        left = self.traversal(node.left)
        right = self.traversal(node.right)
        # 四种情况比较大小
        self.result = max(self.result, left + node.val, right + node.val,
                          left + right + node.val, node.val
                          )
        # 返回值一定要包含加入根节点的情况
        if left > right and left > 0:
            return left + node.val
        elif right >= left and right > 0:
            return right + node.val
        else:
            return node.val if node.val > 0 else 0

    def maxPathSum(self, root: Optional[TreeNode]) -> Optional[Union[int, float]]:
        """
        Time O(n)
        Space O(n)
        后续遍历思路，每次check左右节点，以及左右加上当前节点，以及当前节点本身，比大小，取最大值。
        """
        self.traversal(root)

        return self.result


t1 = TreeNode(val=1)
t2 = TreeNode(val=2)
t3 = TreeNode(val=4)
t1.left = t2
t1.right = t3
solution = Solution()
print(solution.maxPathSum(t1))
