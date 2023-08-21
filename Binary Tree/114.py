# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def traversal(self, node, node_list):
        if node is None:
            return None

        node_list.append(node)

        self.traversal(node.left, node_list)
        self.traversal(node.right, node_list)

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Time O(n)
        Space O(n) 需要额外的list空间来记录前序遍历顺序下的node
        先前序遍历存储下来所有node顺序，再通过loop list重新给每个node分配right和left指针
        """
        node_list = []
        self.traversal(root, node_list)

        for i in range(len(node_list) - 1):
            cur_node = node_list[i]
            next_node = node_list[i + 1]
            cur_node.right = next_node
            cur_node.left = None

        return root


class Solution2:
    def traversal(self, node):
        if node is None:
            return

        # 后续遍历，需要先左右节点先处理完再处理当前节点
        self.traversal(node.left)
        self.traversal(node.right)

        # 后序遍历位置
        # 1、此时左右子树已经被拉平成一条链表
        left = node.left
        right = node.right

        # 2、将左子树作为右子树
        node.left = None
        node.right = left

        # 3、将原先的右子树接到当前右子树(也就是之前的左子树)的末端，需要while loop一直走到当前右子树的底端先
        p = node
        while p.right:
            p = p.right
        p.right = right

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Time O(n)
        Space O(1)  不需要额外list空间存储顺序
        分解问题，分别解决左右子树，则解决了整个树。当前节点左节点变成右节点，然后原先的右节点接入左节点的右节点。
        """

        self.traversal(root)
