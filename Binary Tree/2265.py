# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def traversal(self, node):
        # 如果空节点则，返回0个子树，0的子树和
        if node is None:
            return [0, 0]

        left = self.traversal(node.left)
        right = self.traversal(node.right)

        # 当前节点子树节点个数
        num_nodes = left[0] + right[0] + 1
        # 当前节点子树节点总和
        sum_value = left[1] + right[1] + node.val
        # 计算当前节点的平均值
        avg = int(sum_value / num_nodes)
        # 判断是否是我们要找的节点
        if avg == node.val:
            # 如果是则全局变量计数
            self.res += 1

        # 返回当前节点的结果
        return [num_nodes, sum_value]

    def averageOfSubtree(self, root: TreeNode) -> int:
        """
        Time O(n)
        Space O(n)
        标准的二叉树后序遍历题，因为我们需要在当前节点进行一系列的操作判断并且需要子节点的结果，后续遍历很容易实现这个结果。
        每次返回当前节点作为root的子树的个数和子树的和。详细见注释。
        """
        self.traversal(root)

        return self.res


node1 = TreeNode(3)
node2 = TreeNode(5)
node3 = TreeNode(1)
node1.left = node2
node1.right = node3
s = Solution()
print(s.averageOfSubtree(node1))
