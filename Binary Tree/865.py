from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traversal(self, node):
        # 遇到空节点，返回None和深度为0
        if node is None:
            return None, 0

        left = self.traversal(node.left)
        right = self.traversal(node.right)

        # 如果左边更深，说明左边子节点单独成一个公共先祖，返回左边子节点和新的深度
        if left[1] > right[1]:
            return left[0], left[1] + 1
        # 同理右边更深
        elif right[1] > left[1]:
            return right[0], right[1] + 1
        # 如果一样深，说明当前节点是最小公共先祖，返回当前节点和新的深度
        else:
            return node, left[1] + 1

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Time O(n)
        Space O(n)
        后序遍历方法，每次返回一个tuple，记录当前最小公共先祖节点，和当前自底向上的深度。
        如果深度一样，说明当前节点是最小公共先祖，如果左右的深度不一样，说明当前节点不是最小公共先祖，而长的那一边存在最小公共先祖。
        此时返回长的那一边的node，及子节点。
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
print(s.subtreeWithAllDeepest(root=node1))
