class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traversal(node, count):
    """
    后序遍历，count是用来判断当前node是否满足总和，用减法来判断
    """
    if node.left is None and node.right is None and count == 0:
        return True
    if node.left is None and node.right is None:
        return False

    if node.left:
        count -= node.left.val            # 此处体现回溯的逻辑，减去后不满足这要加回来，等于回到上一个node
        if traversal(node.left, count):
            return True
        count += node.left.val

    if node.right:
        count -= node.right.val  # 此处体现回溯的逻辑，减去后不满足这要加回来，等于回到上一个node
        if traversal(node.right, count):
            return True
        count += node.right.val

    return False


def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    """
    如果需要搜索整棵二叉树且需要处理递归返回值，递归函数就需要返回值
    如果要搜索其中一条符合条件的路径，那么递归一定需要返回值，因为遇到符合条件的路径了就要及时返回。此题情况。
    """
    if root is None:
        return False

    return traversal(root, targetSum - root.val)


class Solution:
    def getSum(self, node, value, target):
        """
        前序遍历的方法，累加当前节点，遇到叶子节点的时候判断剩下的value是不是刚好是此时叶子节点的val
        此方法没有回溯，因为下一次的逻辑在下一层处理，并没有影响这一次节点当前value总和
        """
        if node.left is None and node.right is None:
            if target - value == node.val:
                return True
            else:
                return False

        value += node.val

        if node.left:   # 此处没有回溯，因为value就是当前节点总和，下一层再处理下一层的节点总和
            left = self.getSum(node.left, value, target)
        else:
            left = False

        if node.right:
            right = self.getSum(node.right, value, target)
        else:
            right = False

        return left or right

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

        if root is not None:
            return self.getSum(root, 0, targetSum)
        else:
            return False


t1 = TreeNode(val=1)
t2 = TreeNode(val=2)
t3 = TreeNode(val=4)
t1.left = t2
t1.right = t3
print(hasPathSum(t1, 5))
