from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traversal(self, node):
        if node is None:
            return None, 0

        left = self.traversal(node.left)
        right = self.traversal(node.right)

        if left[1] > right[1]:
            return left[0], left[1] + 1
        elif right[1] > left[1]:
            return right[0], right[1] + 1
        else:
            return node, left[1] + 1

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Time O(n)
        Space O(n)
        同865，一模一样。
        """

        return self.traversal(root)[0]


node1 = TreeNode(0)
node2 = TreeNode(1)
node3 = TreeNode(3)
node4 = TreeNode(2)
node1.left = node2
node1.right = node3
node2.right = node4
s = Solution()
print(s.lcaDeepestLeaves(root=node1))
