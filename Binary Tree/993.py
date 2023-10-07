from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.x_depth = 0
        self.y_depth = 0
        self.x_parent_val = None
        self.y_parent_val = None

    def traversal(self, node, x, y, depth, parent_val):
        if node is None:
            return

        # 记录深度
        depth += 1
        # 遇到节点是x，记录x的深度和父节点的值
        if node.val == x:
            self.x_depth = depth
            self.x_parent_val = parent_val
            return
        # 同理遇到y节点
        if node.val == y:
            self.y_depth = depth
            self.y_parent_val = parent_val
            return

        # 继续遍历子节点
        self.traversal(node.left, x, y, depth, node.val)
        self.traversal(node.right, x, y, depth, node.val)

        return

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        """
        Time O(n)
        Space O(n)
        前序遍历所有节点，每次从父节点传入子节点此时的深度和父节点的值，如果此节点是x或者y，那就全局记录下来，并且结束遍历，
        因为我们已经找到目标节点。最后对比两个节点是否满足表兄弟的定义。
        """

        self.traversal(root, x, y, 0, None)

        # 判断是否符合表兄弟的定义
        if self.y_depth == self.x_depth and self.x_parent_val != self.y_parent_val:
            return True
        else:
            return False


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node1.left = node2
node1.right = node3
node2.right = node4
s = Solution()
print(s.isCousins(node1, 2, 3))
