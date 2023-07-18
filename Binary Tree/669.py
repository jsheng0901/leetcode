from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def trimBST(root: TreeNode, low: int, high: int) -> Optional[TreeNode]:
    """
    如果遇到不符合的节点，则直接把父节点连接给子节点下面符合结果的root节点
    """
    if root is None:
        return None

    if root.val < low:
        node = trimBST(root.right, low, high)
        return node

    if root.val > high:
        node = trimBST(root.left, low, high)
        return node

    root.left = trimBST(root.left, low, high)
    root.right = trimBST(root.right, low, high)

    return root


def trimBSTLoop(root: TreeNode, low: int, high: int) -> Optional[TreeNode]:
    if root is None:
        return None

    while root is not None and (root.val < low or root.val > high):
        if root.val < low:
            root = root.right          # 小于L往右走
        if root.val > high:
            root = root.left           # 大于R往左走

    cur = root
    # 此时root已经在[L, R]
    # 范围内，处理左孩子元素小于L的情况
    while cur is not None:
        while cur.left and cur.left.val < low:
            cur.left = cur.left.right
        cur = cur.left

    cur = root
    # 此时root已经在[L, R]
    # 范围内，处理右孩子大于R的情况
    while cur is not None:
        while cur.right and cur.right.val > high:
            cur.right = cur.right.left
        cur = cur.right

    return root