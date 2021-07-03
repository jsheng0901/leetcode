class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traversal(root, vec):
    """
    中序遍历并记录所有数值
    :param root:
    :return:
    """
    if root is None:
        return
    traversal(root.left, vec)
    vec.append(root.val)    # 将二叉搜索树转换为有序数组
    traversal(root.right, vec)


def getMinimumDifference(root: TreeNode) -> int:
    """
    中序遍历，BTS一般饿哦们都采用中序遍历，因为中序遍历出来的结果刚好是从小到大的有序list
    :param root:
    :return:
    """
    vec = []
    traversal(root, vec)

    if len(vec) < 2:
        return 0

    # 计算有序数组的最小差值，直接找相邻两个数的差值，因为不相邻的两个数的差一定大于相邻两个的差
    results = vec[-1] - vec[0]
    for i in range(1, len(vec)):
        if vec[i] - vec[i-1] < results:
            results = vec[i] - vec[i-1]

    return results


class Solution:
    def __init__(self):
        self.result = float('inf')
        self.pre = None

    def traversal(self, root):
        if root is None:
            return

        self.traversal(root.left)    # 左
        if self.pre is not None:
            self.result = min(self.result, root.val - self.pre.val)

        # 记录前一个
        self.pre = root
        self.traversal(root.right)   # 右

    def getMinimumDifference(self, root: TreeNode) -> int:
        """
        此方法可以节约空间，不需要额外记录list数组，也不需要额外loop一遍list，记录previous node和current node然后比较大小并更新result
        :param root:
        :return:
        """

        self.traversal(root)

        return self.result


t1 = TreeNode(3)
t2 = TreeNode(1)
t3 = TreeNode(6)
t1.left = t2
t1.right = t3
print(getMinimumDifference(t1))
