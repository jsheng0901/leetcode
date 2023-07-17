from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertIntoBST(root: TreeNode, val: int) -> TreeNode:
    """
    二叉搜索树，不需要遍历所有路劲，根据大小加入value，遇到None的时候就加入新的node
    此时要return node这样可以把父节点对子节点的赋值一并实现
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
    # 跳出循环时候，previous刚好是插入新节点的parent节点，current则为None

    if previous.val > val:          # 此时是用parent节点的进行赋值
        previous.left = TreeNode(val)
    else:
        previous.right = TreeNode(val)

    return root


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        此方法为不需要返回任何值当递归的时候，类似前序遍历，在一开始进行中间节点判断并赋值
        """
        if root:
            if root.val > val and root.left is None:
                new_node = TreeNode(val)
                root.left = new_node

            if root.val < val and root.right is None:
                new_node = TreeNode(val)
                root.right = new_node

            if root.val < val:
                self.insertIntoBST(root.right, val)
            elif root.val > val:
                self.insertIntoBST(root.left, val)

            return root
        else:
            return TreeNode(val)


t1 = TreeNode(2)
t2 = TreeNode(1)
t3 = TreeNode(3)
t1.right = t2
t1.left = t3
print(insertIntoBST(t1, 5).val)


