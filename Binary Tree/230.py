from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.step = 0
        self.result = 0

    def traversal(self, node, k):
        if node is None:
            return

        self.traversal(node.left, k)
        self.step += 1
        if self.step == k:
            self.result = node.val
            return
        self.traversal(node.right, k)

        return

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Time O(n)
        Space O(n)
        中序遍历整个树，然后记录走了多少步，找到第K步元素，全局记录返回结果。并不高效，因为要loop整个BST。
        如果改动tree节点，可以记录size，这样就可以使用BST特性达到O(logn)时间复杂度
        """
        self.traversal(root, k)

        return self.result


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node3.left = node1
node3.right = node4
node1.right = node2
s = Solution()
print(s.kthSmallest(root=node3, k=2))


