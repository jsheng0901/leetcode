class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traversal(root, vec):
    if root is None:
        return
    traversal(root.left, vec)
    vec.append(root.val)  # 将二叉搜索树转换为有序数组
    traversal(root.right, vec)


def isValidBST(root: TreeNode) -> bool:
    """
    中序遍历转化成vector来判断大小，因为中序遍历后一定是从小到大的顺序
    Time O(n)
    Space O(n)
    n == number of node
    """

    vec = []
    traversal(root, vec)

    for i in range(1, len(vec)):
        if vec[i] <= vec[i - 1]:
            return False

    return True


class Solution:
    def __init__(self):
        self.pre = None  # 用一个指针来指代前一个节点

    def traversal(self, node):
        """
        同样是中序遍历，中间的时候处理逻辑
        Time O(n)
        Space O(1)
        n == number of node
        """
        if node is None:
            return True

        left = self.traversal(node.left)

        if self.pre is not None and self.pre.val >= node.val:  # 判断前一个value是不是比这个小
            return False
        self.pre = node

        right = self.traversal(node.right)

        return left and right

    def isValidBST(self, root: TreeNode) -> bool:

        if root:
            return self.traversal(root)
        else:
            return False


t1 = TreeNode(2)
t2 = TreeNode(1)
t3 = TreeNode(3)
t1.left = t2
t1.right = t3
print(isValidBST(t1))
