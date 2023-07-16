from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """
    1. 二叉树，只能通过后序遍历（即：回溯）实现从底向上的遍历方式。
    2. 在回溯的过程中，必然要遍历整棵二叉树，即使已经找到结果了，依然要把其他节点遍历完，
    因为要使用递归函数的返回值（也就是代码中的left和right）做逻辑判断。
    3. 在递归函数有返回值的情况下：如果要搜索一条边，递归函数返回值不为空的时候，立刻返回，
    ex: if (递归函数(root->left)) return ; if (递归函数(root->right)) return
    如果搜索整个树，直接用一个变量left、right接住返回值，这个left、right后序还有逻辑处理的需要，也就是后序遍历中处理中间节点的逻辑（也是回溯）
    ex: 下题中left and right 的接法
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
