from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.x = None
        self.y = None
        self.prev = None

    def traversal(self, node):
        if node is None:
            return

        self.traversal(node.left)

        # 如果存在prev指针并且，找到一个不符合的节点，
        # 说明此时prev指针和当前节点就是需要swap的x，y节点，因为题目有说保证就两个需要交换的节点
        if self.prev and node.val < self.prev.val:
            # 第一个需要swap的节点
            self.y = node

            # 如果已经存在一个不合理的节点，可以直接返回
            if self.x is None:
                # 第二个需要swap的节点
                # 这里需要继续判断是否后续还有不合理的节点，所有找到x之后不能直接return
                # ex: 输入 [2, 3, 1] -> 需要转化成[2, 1, 3]，需要转换的是2号节点的左右子节点，而不是2号节点本身。
                self.x = self.prev
            else:
                return

        self.prev = node

        self.traversal(node.right)

        return

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Time O(n)
        Space O(n)
        中序遍历，同时用x, y来记录需要swap的node，同时用prev指针来双指针同时中序遍历，找到x, y后，直接交换value即可，无需真正交换指针位置
        """

        self.traversal(root)

        self.x.val, self.y.val = self.y.val, self.x.val

        return root


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node2.left = node3
node2.right = node1
s = Solution()
print(s.recoverTree(node2))
