from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traversal(self, node, val, depth):
        # 空节点返回None
        if node is None:
            return node

        # 走到符合要求的depth
        if depth - 1 == 1:
            # 构建新左右节点
            left_new_node = TreeNode(val)
            right_new_node = TreeNode(val)

            # 按要求复制原来左右节点给新左右节点
            left_new_node.left = node.left
            right_new_node.right = node.right

            # 新节点接入当前节点
            node.left = left_new_node
            node.right = right_new_node
        else:
            node.left = self.traversal(node.left, val, depth - 1)
            node.right = self.traversal(node.right, val, depth - 1)

        # 返回当前节点
        return node

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        """
        Time O(2^depth - 1)
        Space O(2^depth - 1)
        最多走到depth的深度的时候，构建新的树然后返回新的节点，不会走到最底端。所以最多走过depth深度的node个数，及2^depth - 1个node。
        前序遍历，走到符合要求及depth - 1 == 1的时候开始构建新的节点，然后同时接入新的左右节点。此时已经达到要求，直接返回当前node即可，
        如果没走到符合要求的depth，则通过递归返回值继续赋值给左右节点。
        """
        # 特殊情况，按照要求赋值新的root
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        return self.traversal(root, val, depth)


node1 = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(1)
node1.left = node2
node2.left = node3
node2.right = node4
s = Solution()
print(s.addOneRow(node1, 1, 3))


