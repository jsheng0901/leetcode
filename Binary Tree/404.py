class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getSum(node):
    if node is None:
        return 0

    left_value = getSum(node.left)
    right_value = getSum(node.right)

    mid_value = 0
    if node.left is not None and node.left.left is None and node.left.right is None:
        mid_value = node.left.val

    return left_value + right_value + mid_value


def sumOfLeftLeaves(root: TreeNode) -> int:
    """
    后序遍历， 每次判断当前node的left有没有，并且node left的children是否存在，来确定左叶子
    """

    return getSum(root)


def sumOfLeftLeavesStack(root: TreeNode) -> int:
    """
    后序遍历， 每次判断当前node的left有没有，并且node left的children是否存在，来确定左叶子
    """
    if root is None:
        return 0

    stack = [root]
    result = 0

    while len(stack) > 0:
        top_node = stack.pop()
        if top_node.left is not None and top_node.left.left is None and top_node.left.right is None:
            result += top_node.left.val

        if top_node.right:
            stack.append(top_node.right)

        if top_node.left:
            stack.append(top_node.left)

    return result


class Solution:
    def __init__(self):
        self.result = 0

    def getLeftSum(self, node, direction):
        if direction == 'left' and node.left is None and node.right is None:
            self.result += node.val
            return

        if node.left:
            self.getLeftSum(node.left, 'left')
        if node.right:
            self.getLeftSum(node.right, 'right')

        return

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root:
            self.getLeftSum(root, 'root')

        return self.result


t1 = TreeNode(val=1)
t2 = TreeNode(val=2)
t3 = TreeNode(val=4)
t1.left = t2
t1.right = t3
print(sumOfLeftLeavesStack(t1))