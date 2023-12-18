from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_bst = 0

    def traversal(self, node):
        # 当前节点为空的情况
        if node is None:
            return True, 0, 0, 0

        left = self.traversal(node.left)
        right = self.traversal(node.right)

        # 只有当前节点左右子树都是BST的时候才判断当前节点作为root是不是BST
        if left[0] and right[0]:
            # 如果当前节点左右都存在，并且当前节点符合大于左边最大值，小于右边最小值
            if node.left and node.right and left[2] < node.val < right[1]:
                # 记录目前BST的节点个数
                num_nodes = left[3] + right[3] + 1
                # 更新全局变量记录最大值
                self.max_bst = max(self.max_bst, num_nodes)
                # 返回新的节点结果
                return True, min(node.val, left[1], right[1]), max(node.val, left[2], right[2]), num_nodes
            # 如果当前节点左存在，并且当前节点符合大于左边最大值
            elif node.left and node.right is None and left[2] < node.val:
                num_nodes = left[3] + 1
                self.max_bst = max(self.max_bst, num_nodes)
                return True, min(node.val, left[1]), max(node.val, left[2]), num_nodes
            # 如果当前节点右存在，并且当前节点符合小于右边最小值
            elif node.right and node.left is None and node.val < right[1]:
                num_nodes = right[3] + 1
                self.max_bst = max(self.max_bst, num_nodes)
                return True, min(node.val, right[1]), max(node.val, right[2]), num_nodes
            # 如果当前节点左右都不存在，此情况就是叶子结点
            elif node.right is None and node.left is None:
                num_nodes = 1
                self.max_bst = max(self.max_bst, num_nodes)
                return True, node.val, node.val, num_nodes
            # 如果当前节点左右是BST，但是当前节点作为root后不符合BST
            else:
                return False, 0, 0, 0
        # 当前节点左右子树至少有一个不是BST，则当前节点不可能是BST
        else:
            return False, 0, 0, 0

    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        """
        Time O(n)
        Space O(n)
        后续遍历一次，返回节点所需的所有值，注意这里返回值包含四个状态：子树是否是BST，当前节点最小值，当前节点最大值，当前节点个数。
        拿到左右节点后判断所有情况，详细见注释。
        """
        self.traversal(root)

        return self.max_bst


node1 = TreeNode(3)
node2 = TreeNode(2)
node3 = TreeNode(4)
node4 = TreeNode(1)
node1.left = node2
node2.right = node3
node3.left = node4
s = Solution()
print(s.largestBSTSubtree(root=node1))
