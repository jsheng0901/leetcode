# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.count = 0

    def traversal(self, node, max_value):
        if node is None:
            return

        if node.val >= max_value:
            self.count += 1
            max_value = node.val

        self.traversal(node.left, max_value)
        self.traversal(node.right, max_value)

        return

    def goodNodes(self, root: TreeNode) -> int:
        """
        Time O(n)
        Space O(n)
        前序遍历整个树，找最大值在每个path的时候，并且传给下一个子树，然后判断是不是good node
        """
        if root:
            self.traversal(root, float('-inf'))

        return self.count


node1 = TreeNode(3)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(2)
node1.left = node2
node2.left = node3
node2.right = node4
s = Solution()
print(s.goodNodes(root=node1))
