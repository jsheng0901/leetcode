from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = "~"

    def traversal(self, node, path):
        # 空节点直接跳过
        if node is None:
            return

        # 进入前序遍历头节点，转化成character储存起来
        path.append(chr(node.val + ord('a')))

        # 如果遇到叶子节点，比较大小然后存存起来
        if node.left is None and node.right is None:
            self.result = min(self.result, "".join(reversed(path)))
            # 记得要回溯，因此处结束了递归
            path.pop()
            return

        # 递归子节点
        self.traversal(node.left, path)
        self.traversal(node.right, path)

        # 离开此节点，结束本次递归，回溯弹出当前节点
        path.pop()

        return

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        """
        Time O(n)
        Space O(n)
        前序遍历所有节点，记录进path，然后走到leaf的时候我们check一下最小值，存储reversed的情况，及为leaf -> root顺序。
        这里判断character的大小Python直接用不等号比大小可以。初始值设置为"~"，因为转化成character是126大于任意字母转换。
        """

        self.traversal(root, [])

        return self.result


node1 = TreeNode(4)
node2 = TreeNode(0)
node3 = TreeNode(1)
node4 = TreeNode(1)
node1.left = node2
node1.right = node3
node2.left = node4
s = Solution()
print(s.smallestFromLeaf(node1))
