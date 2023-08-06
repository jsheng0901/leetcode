# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree_rob(self, node):
        if node is None:
            return [0, 0]

        left = self.tree_rob(node.left)
        right = self.tree_rob(node.right)

        # 偷当前node
        val1 = node.val + left[0] + right[0]
        # 不偷当前node
        val2 = max(left[0], left[1]) + max(right[0], right[1])

        return [val2, val1]

    def rob(self, root: TreeNode) -> int:
        """
        Time O(n)
        Space O(logn) 递归系统占用空间
        树形结构的动态规划问题, 结合递归步骤和动态规划步骤, 一定要用后序遍历，因为要在中序的时候处理逻辑，
        每一步node虑两种状态偷或不偷两种状态，用长度为2的数组记录[不偷当前节点，偷当前节点]
        """
        result = self.tree_rob(root)

        return max(result)
