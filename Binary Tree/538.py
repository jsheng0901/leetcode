class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.pre = 0

    def traversal(self, cur):
        """
        中序遍历反着来
        遍历整棵树不需要return任何值，也不需要对返回值做处理
        """
        if cur is None:
            return

        self.traversal(cur.right)
        cur.val += self.pre
        self.pre = cur.val
        self.traversal(cur.left)

    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        反中序遍历然后累加，右中左，用pre cur双指针记录累加, 用一个global variable
        """
        self.traversal(root)
        return root


class SolutionStack:
    def __init__(self):
        self.pre = 0

    def traversal(self, cur):
        """
        中序遍历反着来
        """
        stack = []
        while cur is not None or len(stack) > 0:
            if cur is not None:
                stack.append(cur)
                cur = cur.right             # 右
            else:
                cur = stack.pop()           # 中
                cur.val += self.pre
                self.pre = cur.val
                cur = cur.left              # 左

    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        反中序遍历然后累加，右中左，用pre cur双指针记录累加, 用一个global variable
        """
        self.traversal(root)
        return root





