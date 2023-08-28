from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def same_tree(self, node1, node2):
        """
        判断两颗树是不是完全相同的树
        """
        if node1 is None and node2 is None:
            return True
        elif node1 is None and node2 is not None:
            return False
        elif node1 is not None and node2 is None:
            return False
        elif node1.val != node2.val:
            return False

        left = self.same_tree(node1.left, node2.left)
        right = self.same_tree(node1.right, node2.right)

        return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Time O(n * m) n = number of node in root, m = number of node in sub root
        Space O(n)
        前序遍历树，如果找到相同的节点，判断相同节点的子树是否相同。
        但此时不能立马停止遍历树，如果找到相同子树则停止遍历，如果不同，继续左右子树查找。
        """
        # 如果走到底都没有相同子树，则直接返回false
        if root is None:
            return False

        # 如果找到相同节点，开始判断此节点为root的子树是否相同
        if root.val == subRoot.val:
            mid = self.same_tree(root, subRoot)
        else:
            mid = False
        # 如果找到直接返回true，如果没有找到，则继续左右子树查找
        if mid:
            return mid
        else:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)

            return left or right

