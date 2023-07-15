from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root: TreeNode, val: int) -> Optional[TreeNode]:
    """
    二叉搜索树，同遍历一样，左右顺序，只是我们每次不需要一定走左或者右，因为左右有大小顺序
    若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值
    若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
    """
    if root is None or root.val == val:
        return root

    if root.val > val:
        # 注意此处要return，因为我们是找到对应的就停止，而不是遍历整个二叉树
        return searchBST(root.left, val)
    if root.val < val:
        return searchBST(root.right, val)

    return None


def searchBSTLoop(root: TreeNode, val: int) -> Optional[TreeNode]:
    """
    迭代法，不用stack也不用queue，因为我们的路线是规划好的，因为搜索树有大小顺序
    对于二叉搜索树，不需要回溯的过程，因为节点的有序性就帮我们确定了搜索的方向。
    """
    while root is not None:
        if root.val > val:
            root = root.left
        if root.val < val:
            root = root.right
        if root.val == val:
            return root
    return None
