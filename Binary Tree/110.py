class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_depth(self, node):
        if node is None:
            return 0

        left_depth = self.get_depth(node.left)            # 左
        if left_depth == -1:
            return -1
        right_depth = self.get_depth(node.right)          # 右
        if right_depth == -1:
            return -1

        if abs(left_depth - right_depth) > 1:
            depth = -1
        else:
            depth = 1 + max(left_depth, right_depth)    # 中

        return depth

    def isBalanced(self, root: TreeNode) -> int:
        """
        Time O(n)
        Space O(n)
        依然是后序遍历，每一次遍历的时候记录深度，如果不满足平衡的时候就return -1 标记，否则就check深度差,
        此题目可以用stack的层序遍历，loop发，逻辑就是模拟前序遍历，每一次经过每一层的node时候就计算一次左右node的深度然后算差，
        但是方法复杂，因为要单独写一个算depth的function，推荐用递归
        """

        return self.get_depth(root) != -1


t1 = TreeNode(val=1)
t2 = TreeNode(val=2)
t3 = TreeNode(val=4)
t1.left = t2
t1.right = t3
s = Solution()
print(s.isBalanced(t1))
