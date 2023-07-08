class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: TreeNode) -> TreeNode:
    """
    二叉树的前序遍历，每次反转左右节点的连接
    """
    if root is None:
        return

    root.right, root.left = root.left, root.right    # 中， 交替left right
    invertTree(root.left)                            # 左
    invertTree(root.right)                           # 右

    return root


def invertTreeStack(root: TreeNode) -> TreeNode:
    """
    stack的写法，遍历tree
    """
    stack = [root]
    while len(stack) > 0:
        front_node = stack.pop()
        front_node.right, front_node.left = front_node.left, front_node.right   # 中
        stack.append(front_node.right)                                          # 右  空节点入栈
        stack.append(front_node.left)                                           # 左

    return root


def invertTreeLevelOrder(root: TreeNode) -> TreeNode:
    """
    level order遍历的写法，遍历tree
    """
    queue = [root]
    while len(queue) > 0:
        size = len(queue)
        for i in range(size):
            front_node = queue.pop(0)
            front_node.right, front_node.left = front_node.left, front_node.right   # 中
            if front_node.left:                                                         # 空节点不入栈
                queue.append(front_node.left)                                           # 左
            if front_node.right:
                queue.append(front_node.right)                                          # 右

    return root


t1 = TreeNode(val=1)
t2 = TreeNode(val=2)
t3 = TreeNode(val=3)
t1.left = t2
t1.right = t3
invertTreeLevelOrder(t1)
print(t1.left.val)
print(t1.right.val)

