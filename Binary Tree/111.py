class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getDepth(node):
    if node is None:
        return 0

    left_depth = getDepth(node.left);       # 左
    right_depth = getDepth(node.right);     # 右

    # 当一个左子树为空，右不为空，这时并不是最低点
    if node.left is None and node.right is not None:
        return 1 + right_depth
    # 当一个右子树为空，左不为空，这时并不是最低点
    elif node.left is not None and node.right is None:
        return 1 + left_depth

    depth = 1 + min(left_depth, right_depth) # 中

    return depth


def minDepth(root: TreeNode) -> int:
    """
    后序遍历，区别在于左右有一个为None的时候不是最小depth，因为要找到左右同时为None的叶子节点的深度，深度是有一个node就是一层
    """

    return getDepth(root)


def minDepthQueue(root: TreeNode):
    """
    层序遍历，记录到那一层的时候有node的左右节点都为None
    """
    queue = [root]
    depth = 0
    has_empty_node = False

    while len(queue) > 0:
        size = len(queue)
        depth += 1
        for i in range(size):
            front_node = queue.pop(0)
            if front_node.left:
                queue.append(front_node.left)
            if front_node.right:
                queue.append(front_node.right)
            elif front_node.left is None and front_node.right is None:
                has_empty_node = True
                break

        if has_empty_node:
            break

    return depth


t1 = TreeNode(val=1)
t2 = TreeNode(val=2)
t3 = TreeNode(val=4)
t4 = TreeNode(val=5)
t5 = TreeNode(val=6)
t1.left = t2
t1.right = t3
t3.left = t4
t3.right = t5
print(minDepthQueue(t1))