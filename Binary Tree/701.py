class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBST(root: TreeNode, val: int) -> TreeNode:
    """
    二叉搜索树，不需要遍历所有路劲，根据大小加入value，遇到None的时候就加入新的node
    此时要return node这样可以把父节点对子节点的赋值一并实现
    :param root:
    :param val:
    :return:
    """
    if root is None:
        return TreeNode(val)

    if root.val > val:
        root.left = insertIntoBST(root.left, val)
    if root.val < val:
        root.right = insertIntoBST(root.right, val)

    return root


def insertIntoBSTLoop(root: TreeNode, val: int) -> TreeNode:
    """
    loop方法，基本上一样就是需要两个node来记录parent和children实现到None的时候指针指向
    迭代的方法就需要记录当前遍历节点的父节点了，这个和没有返回值的递归函数实现的代码逻辑是一样的
    :param root:
    :param val:
    :return:
    """

    if root is None:
        return TreeNode(val)

    previous = root
    current = root

    while current:
        previous = current

        if current.val > val:
            current = current.left
        else:
            current = current.right

    if previous.val > val:          # 此时是用parent节点的进行赋值
        previous.left = TreeNode(val)
    else:
        previous.right = TreeNode(val)

    return root


t1 = TreeNode(2)
t2 = TreeNode(1)
t3 = TreeNode(3)
t1.right = t2
t1.left = t3
print(insertIntoBST(t1, 5).val)


