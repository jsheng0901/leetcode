class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """
    后序遍历，从下到上loop所有node
    :param root:
    :param p:
    :param q:
    :return:
    """
    if root == p or root == q or root is None:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left is not None and right is not None:
        return root

    if left is None and right is not None:
        return right
    elif left is not None and right is None:
        return left
    else:
        return None


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.right = t2
t1.left = t3
print(lowestCommonAncestor(t1, t2, t3).val)
