from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        # 全局变量，记录 BST 最大节点之和
        self.result = 0

    def traversal(self, node):
        # 遇到空节点的时候返回情况
        if node is None:
            return [True, float('inf'), float('-inf'), 0]

        # 递归计算左右子树
        left = self.traversal(node.left)
        right = self.traversal(node.right)

        # 后续遍历中间节点开始处理逻辑，记录返回数组
        res = [0] * 4
        # 这个 if 在判断以 root 为根的二叉树是不是 BST
        if left[0] and right[0] and left[2] < node.val < right[1]:
            # 以 root 为根的二叉树是 BST
            res[0] = True
            # 计算以 root 为根的这棵 BST 的最小值
            res[1] = min(left[1], node.val)
            # 计算以 root 为根的这棵 BST 的最大值
            res[2] = max(right[2], node.val)
            # 计算以 root 为根的这棵 BST 所有节点之和
            res[3] = left[3] + right[3] + node.val
            # 更新全局变量
            self.result = max(self.result, res[3])
        else:
            # 以 root 为根的二叉树不是 BST
            res[0] = False
            # 其他的值都没必要计算了，因为用不到

        return res

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        """
        Time O(n)
        Space O(n)
        后序遍历，每次返回一个数组记录四个数据：
        res[0] 记录以 root 为根的二叉树是否是 BST，若为 True 则说明是 BST，若为 False 则说明不是 BST；
        res[1] 记录以 root 为根的二叉树所有节点中的最小值；
        res[2] 记录以 root 为根的二叉树所有节点中的最大值；
        res[3] 记录以 root 为根的二叉树所有节点值之和。
        """

        self.traversal(root)

        return self.result


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)
node4 = TreeNode(3)
node5 = TreeNode(4)
node6 = TreeNode(4)
node7 = TreeNode(4)
node8 = TreeNode(5)
node9 = TreeNode(6)
node1.left = node5
node1.right = node4
node5.left = node2
node5.right = node6
node4.left = node3
node4.right = node8
node8.left = node7
node8.right = node9

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n4.left = n3
n3.left = n1
n3.right = n2
s = Solution()
print(s.maxSumBST(n4))
