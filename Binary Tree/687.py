from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = 0

    def traversal(self, node):
        # 如果空节点，则为0
        if node is None:
            return 0

        left = self.traversal(node.left)
        right = self.traversal(node.right)

        # 记录当前节点下最长path的长度，初始值为0，避免可能子树不存在的情况。
        left_path = 0
        right_path = 0

        # 如果左节点存在并且相等，左节点path长度等于左子树返回值 +1
        if node.left and node.val == node.left.val:
            left_path = left + 1

        # 同左节点
        if node.right and node.val == node.right.val:
            right_path = right + 1

        # 随时记录最长的path，这里左右相加是因为有可能左右都存在并且都相等，如果不存在或者不等 +0 也不影响结果对比
        self.result = max(self.result, left_path + right_path)

        # 只能选择返回左或者右最长的path值，不能返回当前节点和子节点都相等的情况，因为这不是一个合理的path
        return max(left_path, right_path)

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        """
        Time O(n)
        Space O(n)
        后序遍历，返回当前左右子树满足等于情况下的最长path长度，如果左右子树没有等于当前节点，则返回值为0，
        因为当前节点及为新的起始相同path节点。
        """
        self.traversal(root)

        return self.result


node1 = TreeNode(1)
node2 = TreeNode(4)
node3 = TreeNode(5)
node4 = TreeNode(4)
node5 = TreeNode(4)
node6 = TreeNode(5)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
s = Solution()
print(s.longestUnivaluePath(root=node1))

