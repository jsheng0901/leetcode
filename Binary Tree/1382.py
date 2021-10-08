# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.list = []

    def dfs(self, node):
        if node is None:
            return

        self.dfs(node.left)
        self.list.append(node.val)
        self.dfs(node.right)

        return

    def build(self, arr, left, right):
        if left > right:
            return None

        mid = left + (right - left) // 2
        node = TreeNode(arr[mid])
        node.left = self.build(arr, left, mid - 1)
        node.right = self.build(arr, mid + 1, right)

        return node

    def balanceBST(self, root: TreeNode) -> TreeNode:
        """先中序遍历构建有序的二叉树list，在前序遍历构建BST"""
        if root:
            self.dfs(root)

            return self.build(self.list, 0, len(self.list) - 1)

