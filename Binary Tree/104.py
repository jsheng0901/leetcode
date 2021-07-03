class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getDepth(node):
    if node is None:
        return 0

    left_depth = getDepth(node.left)            # 左
    right_depth = getDepth(node.right)          # 右
    depth = 1 + max(left_depth, right_depth)    # 中
    return depth


def maxDepth(root: TreeNode) -> int:
    """
    依然是后序遍历，每一次到最下面的时候记录深度
    """
    return getDepth(root)


def maxDepthQueue(root: TreeNode):
    """
    层序遍历，记录有多少层极为多深
    """
    queue = [root]
    depth = 0

    while len(queue) > 0:
        size = len(queue)
        depth += 1
        for i in range(size):
            front_node = queue.pop(0)
            if front_node.left:
                queue.append(front_node.left)
            if front_node.right:
                queue.append(front_node.right)

    return depth


t1 = TreeNode(val=1)
t2 = TreeNode(val=2)
t3 = TreeNode(val=4)
t1.left = t2
t1.right = t3
print(maxDepthQueue(t1))