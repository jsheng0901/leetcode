class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def compare(left, right):
    """
    left: left node, right: right node
    return true or false
    """
    # 首先排除空节点的情况
    if left is None and right is not None:
        return False
    elif left is not None and right is None:
        return False
    elif left is None and right is None:
        return True
    # 排除了空节点，再排除数值不相同的情况
    elif left.val != right.val:
        return False

    # 此时才做递归，做下一层的判断
    outside = compare(left.left, right.right)  # 左子树：左、 右子树：右
    inside = compare(left.right, right.left)  # 左子树：右、 右子树：左
    is_same = outside and inside  # 左子树：中、 右子树：中 （逻辑处理）

    return is_same


def isSymmetric(root: TreeNode) -> bool:
    if root is None:
        return False

    return compare(root.left, root.right)


def isSymmetricQueue(root: TreeNode) -> bool:
    """
    while loop 方法，用 queue 或者stack一摸一样，因为同时pop两个node，并且顺序并不重要
    """
    if root is None:
        return True
    queue = [root.left, root.right]
    while len(queue) > 0:
        left_node = queue.pop(0)
        right_node = queue.pop(0)
        if left_node is None and right_node is None:
            continue

        elif left_node is None or right_node is None or left_node.val != right_node.val:
            return False

        queue.append(left_node.left)  # 加入左节点左孩
        queue.append(right_node.right)  # 加入右节点右孩子
        queue.append(left_node.right)  # 加入左节点右孩子
        queue.append(right_node.left)  # 加入右节点左孩子

    return True


t1 = TreeNode(val=1)
t2 = TreeNode(val=2)
t3 = TreeNode(val=4)
t1.left = t2
t1.right = t3
print(isSymmetricQueue(t1))
