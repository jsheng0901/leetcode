from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def __init__(self):
        self.result = 0

    def traversal(self, node, path):
        # 记录当前节点的path，可以放在叶子结点判断前后都行，因为不valid的node不会进递归函数
        path += str(node.val)

        if node.left is None and node.right is None:
            self.result += int(path)
            return

        # 空节点不入递归
        if node.left:
            self.traversal(node.left, path)
        if node.right:
            self.traversal(node.right, path)

        return

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Time O(n)
        Space O(n)
        前序遍历写法，此处把path当做参数往下传，因为path是string，在Python里面是immutable的，所以当前函数下的path不会被下一个递归函数
        改动path的值，所以不需要递归后加回溯pop。
        """
        path = ""
        self.traversal(root, path)

        return self.result


class Solution2:
    def __init__(self):
        self.result = 0
        self.path = ''

    def traversal(self, node):
        if node.left is None and node.right is None:
            self.path += str(node.val)
            self.result += int(self.path)
            return

        self.path += str(node.val)

        if node.left:
            self.traversal(node.left)
            self.path = self.path[:-1]      # 递归后回溯

        if node.right:
            self.traversal(node.right)
            self.path = self.path[:-1]

        return

    def sumNumbers(self, root: TreeNode) -> int:
        """
        Time O(n)
        Space O(n)
        同第一种，区别在于path是全局参数，需要递归后回溯到上一个节点的值。
        """
        self.traversal(root)
        return self.result


t1 = TreeNode(val=1)
t2 = TreeNode(val=2)
t3 = TreeNode(val=4)
t1.left = t2
t1.right = t3
solution = Solution1()
print(solution.sumNumbers(t1))
