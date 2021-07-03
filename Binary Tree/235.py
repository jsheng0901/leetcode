class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def traversal(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """
    前序遍历，因为二个是二叉搜索树，有顺序
    :param q:
    :param p:
    :param root:
    :return:
    """
    if root is None:
        return root

    if root.val > p.val and root.val > q.val:
        left = traversal(root.left, p, q)
        if left is not None:
            return left

    if root.val < p.val and root.val < q.val:
        right = traversal(root.right, p, q)
        if right is not None:
            return right

    return root


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

    return traversal(root, p, q)


def lowestCommonAncestorLoop(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root


t1 = TreeNode(2)
t2 = TreeNode(1)
t3 = TreeNode(3)
t1.right = t2
t1.left = t3
print(lowestCommonAncestorLoop(t1, t2, t3).val)