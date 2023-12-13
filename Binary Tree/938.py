from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def __init__(self):
        self.result = 0

    def traversal(self, node, low, high):
        if node is None:
            return

        if node.val > low:
            self.traversal(node.left, low, high)

        if low <= node.val <= high:
            self.result += node.val

        if node.val < high:
            self.traversal(node.right, low, high)

        return

    def rangeSumBST(self, root: [TreeNode], low: int, high: int) -> int:
        """
        Time O(n)
        Space O(n)
        中序遍历，每次判断大小再进入不同的branch，然后中间节点计算sum
        """
        if root:
            self.traversal(root, low, high)

        return self.result


class Solution2:
    def __init__(self):
        self.res = 0

    def traversal(self, node, low, high):
        if node is None:
            return

        if low <= node.val <= high:
            self.res += node.val

        if node.val < low:
            self.traversal(node.right, low, high)
        elif node.val > high:
            self.traversal(node.left, low, high)
        else:
            self.traversal(node.left, low, high)
            self.traversal(node.right, low, high)

        return

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Time O(n)
        Space O(n)
        前序遍历，先判断节点，在判断大小要去那一边branch。
        """
        self.traversal(root, low, high)

        return self.res


node1 = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(15)
node4 = TreeNode(3)
node5 = TreeNode(7)
node6 = TreeNode(18)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
s = Solution2()
print(s.rangeSumBST(root=node1, low=7, high=15))
