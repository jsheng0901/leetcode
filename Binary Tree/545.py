from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traversal_left(self, node, path):
        # 前序遍历找左边界
        if node is None:
            return

        if node.left is None and node.right is None:
            return

        if node.left:
            path.append(node.val)
            self.traversal_left(node.left, path)
        elif node.right:
            path.append(node.val)
            self.traversal_left(node.right, path)

        return

    def traversal_right(self, node, path):
        # 后序遍历找右边界
        if node is None:
            return

        if node.left is None and node.right is None:
            return

        if node.right:
            self.traversal_right(node.right, path)
            path.append(node.val)
        elif node.left:
            self.traversal_right(node.left, path)
            path.append(node.val)

        return

    def find_leaves(self, node, path):
        # 前序遍历找所有叶子节点，前序遍历找到的叶子节点顺序刚好是从左到右的叶子结点顺序
        if node is None:
            return

        if node.left is None and node.right is None:
            path.append(node.val)
            return

        self.find_leaves(node.left, path)
        self.find_leaves(node.right, path)

        return

    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        """
        Time O(n)
        Space O(n)
        基本上就是按照题目的定义来遍历树，题目的含义比较难理解。左边界用前序遍历，右边界用后续遍历，树叶用前序遍历。注意判断如果root没有
        子节点，不需要计算叶子节点。
        """
        left_boundary = []
        right_boundary = []
        leaves = []
        # 找左边界节点
        self.traversal_left(root.left, left_boundary)
        # 找右边界节点
        self.traversal_right(root.right, right_boundary)
        # 如果有叶子节点，找叶子节点
        if root.left or root.right:
            self.find_leaves(root, leaves)
        # 链接所有结果
        res = [root.val] + left_boundary + leaves + right_boundary

        return res


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node1.left = node2
node1.right = node7
node2.left = node3
node2.right = node5
node3.left = node4
node7.right = node6
s = Solution()
print(s.boundaryOfBinaryTree(root=node1))
