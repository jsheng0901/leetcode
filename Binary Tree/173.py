# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator1:

    def __init__(self, root: TreeNode):
        """
        Time O(n)
        Space O(n)
        in order store all value in sorted list, then return value from list
        """
        # Array containing all the nodes in the sorted order
        self.nodes_sorted = []

        # Pointer to the next smallest element in the BST
        self.index = -1

        # Call to flatten the input binary search tree
        self._inorder(root)

    def _inorder(self, root):
        """
        Time O(n)
        Space O(n)
        """
        if not root:
            return
        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        """
        Time O(1)
        Space O(n)
        """
        self.index += 1
        return self.nodes_sorted[self.index]

    def hasNext(self) -> bool:
        """
        Time O(1)
        Space O(n)
        """
        return self.index + 1 < len(self.nodes_sorted)


class BSTIterator2:
    def __init__(self, root: TreeNode):
        """
        Time O(n) -> worse    O(1) -> average
        Space O(h)
        构造一个最左边的node stack保证永远最上面的是当前最小的，top in stack就是最小node
        这里栈里面最多存储等于高度的节点个数，最差情况一个树只有左节点，也就是高度h等于节点个数n。
        """
        self.stack = []
        self.left_most(root)

    def left_most(self, root):
        """
        Time O(n) -> worse    O(1) -> average
        Space O(h)
        """
        # 一直叠加当前节点的左边节点，保证栈顶是最小值
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        Time O(n) -> worse    O(1) -> average
        Space O(h)
        """
        left_most_node = self.stack.pop()
        # 如果当前节点有右节点，则把右边的都加入进stack，因为右孩子节点肯定比当前节点大，比当前节点的parent节点小
        if left_most_node.right:
            self.left_most(left_most_node.right)

        return left_most_node.val

    def hasNext(self) -> bool:
        """
        Time O(1)
        Space O(h)
        """
        return len(self.stack) > 0


node1 = TreeNode(7)
node2 = TreeNode(3)
node3 = TreeNode(15)
node4 = TreeNode(9)
node5 = TreeNode(20)
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
obj = BSTIterator2(node1)
print(obj.next())
print(obj.hasNext())
