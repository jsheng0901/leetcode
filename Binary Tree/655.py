# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_height(self, root):
        # 层序遍历拿到树的高度，这里初始值为 -1， 因为树的高度这里root为0
        queue = [root]
        height = -1
        while queue:
            size = len(queue)
            height += 1
            for _ in range(size):
                top = queue.pop(0)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)

        return height

    def traversal(self, root, res, row, col, height):
        # 叶子结点，直接结束
        if root is None:
            return
        # 赋值
        res[row][col] = str(root.val)
        # 遍历左右节点，这里row 和 col都依照题目的意思计算
        self.traversal(root.left, res, row + 1, col - 2 ** (height - row - 1), height)
        self.traversal(root.right, res, row + 1, col + 2 ** (height - row - 1), height)

        return

    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        """
        Time O(n)
        Space O(n)
        层序遍历或者各种遍历都行，拿到树的高度先。然后set好result数组，之后前序遍历插入结果。很直观的题目。
        """
        # 拿到高度
        height = self.get_height(root)
        m = height + 1
        n = 2 ** (height + 1) - 1
        # assign result数组
        res = [[""] * n for _ in range(m)]
        # 前序遍历插入结果
        self.traversal(root, res, 0, int((n - 1) / 2), height)

        return res


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node1.left = node2
node1.right = node3
node2.right = node4
s = Solution()
print(s.printTree(node1))
