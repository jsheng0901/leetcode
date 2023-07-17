from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def traversal(root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """
    前序遍历，因为二个是二叉搜索树，有顺序，当root的value在PQ中间的时候说明找到了最小公共先祖
    """
    if root is None:
        return root

    if root.val > p.val and root.val > q.val:
        left = traversal(root.left, p, q)
        if left is not None:    # 递归函数有返回值，搜索一条边的写法，遇到递归函数的返回值，如果不为空，立刻返回
            return left

    if root.val < p.val and root.val < q.val:
        right = traversal(root.right, p, q)
        if right is not None:
            return right

    return root


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

    return traversal(root, p, q)


def lowestCommonAncestorLoop(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
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