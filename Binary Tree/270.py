from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = None
        self.min_dist = float('inf')

    def traversal(self, node, target):
        if node is None:
            return

        # 当前节点距离target的距离
        dist = abs(node.val - target)
        # 如果找到距离更小的则更新结果和最小距离
        if dist < self.min_dist:
            self.min_dist = dist
            self.res = node.val
        # 如果找到距离相等的则取节点value的最小值
        if dist == self.min_dist:
            self.res = min(self.res, node.val)

        # target更小，向左走
        if target < node.val:
            self.traversal(node.left, target)
        # target更大，向右走
        if target > node.val:
            self.traversal(node.right, target)

        return

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """
        Time O(H), H --> tree height
        BST时间复杂度，如果不是balance的树，worse case是树的高度，如果是balance的树，average来说是log(n)。
        前序遍历，找到一个path，根据节点的值和target的数值大小，每次判断更新最近的节点的值。利用BST的树的特质判断走左边还是右边。
        """
        if root:
            self.traversal(root, target)

        return self.res


node1 = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(5)
node4 = TreeNode(1)
node5 = TreeNode(3)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
s = Solution()
print(s.closestValue(root=node1, target=3.5))
