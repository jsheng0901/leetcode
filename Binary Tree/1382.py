# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
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
        """
        Time O(n)
        Space O(n)
        先中序遍历构建有序的二叉树list，在前序遍历构建BST，利用BST特性，类似二分法构造。
        """
        if root:
            self.dfs(root)

            return self.build(self.list, 0, len(self.list) - 1)


class Solution2:

    def traversal(self, node, path):
        if node is None:
            return

        self.traversal(node.left, path)
        path.append(node.val)
        self.traversal(node.right, path)

        return

    def build(self, arr, left, right):
        if left > right:
            return None

        mid = left + (right - left) // 2
        value = arr[mid]
        node = TreeNode(value)
        node.left = self.build(arr, left, mid - 1)
        node.right = self.build(arr, mid + 1, right)

        return node

    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
        Time O(n)
        Space O(n)
        同方法一，区别在于不用全局变量。先中序遍历构建有序的二叉树list，在前序遍历构建BST，利用BST特性，类似二分法构造。
        """
        path = []
        self.traversal(root, path)

        return self.build(path, 0, len(path) - 1)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node1.right = node2
node2.right = node3
node3.right = node4
s = Solution2()
print(s.balanceBST(node1))

