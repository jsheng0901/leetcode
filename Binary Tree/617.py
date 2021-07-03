class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTrees(root1: TreeNode, root2: TreeNode) -> TreeNode:
    """
    同时传入两个tree的node，同时做前序遍历
    :param root1:
    :param root2:
    :return:  tree node
    """
    if root1 is None:
        return root2
    if root2 is None:
        return root1

    root1.val += root2.val
    root1.left = mergeTrees(root1.left, root2.left)
    root1.right = mergeTrees(root1.right, root2.right)

    return root1


def mergeTreesQueue(root1: TreeNode, root2: TreeNode) -> TreeNode:
    """
    同时传入两个tree的node，同时加入queue并且同时判断
    :param root1:
    :param root2:
    :return:  tree node
    """
    if root1 is None:
        return root2
    if root2 is None:
        return root1

    queue = [root1, root2]

    while len(queue) > 0:
        t1 = queue.pop(0)
        t2 = queue.pop(0)
        t1.val += t2.val

        # 如果两棵树左节点都不为空，加入队列
        if t1.left is not None and t2.left is not None:
            queue.append(t1.left)
            queue.append(t2.left)

        # 如果两棵树右节点都不为空，加入队列
        if t1.right is not None and t2.right is not None:
            queue.append(t1.right)
            queue.append(t2.right)

        if t1.left is None and t2.left is not None:
            t1.left = t2.left

        if t1.right is None and t2.right is not None:
            t1.right = t2.right

    return root1


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)

t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)

t1.left = t2
t1.right = t3

t4.left = t5
t4.right = t6

print(mergeTreesQueue(t1, t4).val)

