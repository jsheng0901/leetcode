from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deleteNode(root: TreeNode, key: int) -> Optional[TreeNode]:
    """
    五种特殊情况对应的删除要搞清楚怎么操作，同样还是利用二叉搜索树额特性
    """
    if root is None:
        return root         # 第一种情况：没找到删除的节点，遍历到空节点直接返回了

    if root.val == key:
        # 第二种情况：左右孩子都为空（叶子节点），直接删除节点， 返回NULL为根节点
        if root.left is None and root.right is None:
            return None
        # 第三种情况：其左孩子为空，右孩子不为空，删除节点，右孩子补位 ，返回右孩子为根节点
        elif root.left is None:
            return root.right
        # 第四种情况：其右孩子为空，左孩子不为空，删除节点，左孩子补位，返回左孩子为根节点
        elif root.right is None:
            return root.left
        # 第五种情况：左右孩子节点都不为空，则将删除节点的左子树放到删除节点的右子树的最左面节点的左孩子的位置
        # 并返回删除节点右孩子为新的根节点。
        else:
            cur = root.right     # 找右子树最左面的节点
            while cur.left is not None:
                cur = cur.left
            cur.left = root.left    # 把要删除的节点（root）左子树放在cur的左孩子的位置
            # tmp = root              # 把root节点保存一下，下面来删除
            # root = root.right       # 返回旧root的右孩子作为新root

            return root.right         # 返回旧root的右孩子作为新root

    if root.val > key:  # return node同时实现实现赋值和删除
        root.left = deleteNode(root.left, key)

    if root.val < key:
        root.right = deleteNode(root.right, key)

    return root
