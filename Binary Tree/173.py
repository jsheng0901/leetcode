# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator1:
    """in order store all value in sorted list, then return value from list"""

    def __init__(self, root: TreeNode):
        # Array containing all the nodes in the sorted order
        self.nodes_sorted = []

        # Pointer to the next smallest element in the BST
        self.index = -1

        # Call to flatten the input binary search tree
        self._inorder(root)

    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        return self.nodes_sorted[self.index]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index + 1 < len(self.nodes_sorted)


class BSTIterator2:
    """构造一个最左边的node stack保证永远最上面的是当前最小的，top in stack就是最小node"""
    def __init__(self, root: TreeNode):

        self.stack = []
        self.left_most(root)

    def left_most(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        left_most_node = self.stack.pop()
        # 如果当前节点有右节点，则把右边的都加入进stack，因为右孩子节点肯定比当前节点大，比当前节点的parent节点小
        if left_most_node.right:
            self.left_most(left_most_node.right)

        return left_most_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
