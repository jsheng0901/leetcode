from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.moves = 0

    def traversal(self, node):
        # 空节点不需要移动，直接返回0
        if node is None:
            return 0

        left = self.traversal(node.left)
        right = self.traversal(node.right)

        # 需要移动的步骤和
        self.moves += abs(left) + abs(right)

        # abs(此节点所有coins - 1)
        return left + right + node.val - 1

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        """
        Time O(n)
        Space O(n)
        后序遍历。这里有一个核心思想，无论从哪里移动硬币，一个node需要移动的最小步骤是abs(此节点所有coins - 1)。
        因为无论是没有coins，从其它地方移动一个过来，还是多个coins比如4，都需要移除多余1的部分，因为最终每个节点只能有1个coin。
        所以后续遍历每次返回需要移动的步骤根据上面的核心思想。
        """
        self.traversal(root)

        return self.moves


node1 = TreeNode(3)
node2 = TreeNode(0)
node3 = TreeNode(0)
node1.left = node2
node1.right = node3
s = Solution()
print(s.distributeCoins(node1))
