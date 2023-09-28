from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traversal(self, node1, node2):
        # 一定要先check都是None或者一个为None的情况，这样才可以判断空节点逻辑
        if node1 is None and node2 is None:
            return True
        elif node1 is None and node2:
            return False
        elif node2 is None and node1:
            return False
        elif node1.val != node2.val:
            return False

        # 如果不翻转子树的情况
        no_flip_left = self.traversal(node1.left, node2.left)
        no_flip_right = self.traversal(node1.right, node2.right)

        # 如果翻转子树的情况
        flip_left = self.traversal(node1.left, node2.right)
        flip_right = self.traversal(node1.right, node2.left)

        # 满足任意一种情况就可以返回true
        return (no_flip_left and no_flip_right) or (flip_left and flip_right)

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        Time O(min(n1, n2)) 最短的树的node个数
        Space O(min(n1, n2))
        同时遍历两棵树的节点，如果都是空则返回true，其它情况都返回false，当value相等的时候不需要返回，继续遍历直到走到空节点。
        前序遍历通过返回值来处理结果，其实就是走到底然后回溯传给父节点，此处其实就是后序遍历的返回逻辑。
        这里需要check的就是两种情况的返回值，一种是不翻转，另一种是翻转左右子树，只要满足一种情况即可返回true。
        """

        return self.traversal(root1, root2)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3

node4 = TreeNode(1)
node5 = TreeNode(2)
node6 = TreeNode(3)
node4.left = node6
node4.right = node5

s = Solution()
print(s.flipEquiv(node1, node4))
