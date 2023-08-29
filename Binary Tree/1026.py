from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traversal(self, node, cur_max, cur_min):
        # 走到底，计算一个path下的最大差值
        if node is None:
            return cur_max - cur_min

        # 更新一个path里面最大值，最小值
        cur_max = max(cur_max, node.val)
        cur_min = min(cur_min, node.val)
        # 左右递归，找到左右path的最大值
        left = self.traversal(node.left, cur_max, cur_min)
        right = self.traversal(node.right, cur_max, cur_min)
        # 返回最大值
        return max(left, right)

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        Time O(n)
        Space O(n)
        前序遍历记录每一个path中的最大值最小值，走到底的时候计算这个path下的最大值最小值差，然后返回结果，
        左右子树判断哪个path的差值最大，然后返回最终结果。
        """
        result = self.traversal(root, root.val, root.val)

        return result


node0 = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.right = node2
node2.right = node0
node0.left = node3
s = Solution()
print(s.maxAncestorDiff(node1))
