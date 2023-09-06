from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traversal(self, node, target):
        if node is None:
            return None

        node.left = self.traversal(node.left, target)
        node.right = self.traversal(node.right, target)

        if node.val == target and node.left is None and node.right is None:
            return None
        else:
            return node

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        """
        Time O(n)
        Space O(n)
        后续遍历同时赋值删除，当前node的值等于target值并且当前node是叶子结点的时候返回None执行删除节点逻辑，
        其它情况都保留当前node，返回node本身
        """

        return self.traversal(root, target)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(2)
node1.left = node2
node1.right = node3
node2.left = node4
s = Solution()
print(s.removeLeafNodes(root=node1, target=2))
