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
        if node is None:
            return

        if node.val % 2 == 0:
            left = node.left
            if left:
                if left.left:
                    self.result += left.left.val
                if left.right:
                    self.result += left.right.val
            right = node.right
            if right:
                if right.left:
                    self.result += right.left.val
                if right.right:
                    self.result += right.right.val

        self.traversal(node.left)
        self.traversal(node.right)

        return

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        """
        Time O(n)
        Space O(n)
        前序遍历思路，遇到符合条件的祖父节点，判断孙节点是否存在并累加进最终结果
        """
        self.traversal(root)

        return self.result


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node6.left = node1
node6.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
s = Solution()
print(s.sumEvenGrandparent(root=node6))
