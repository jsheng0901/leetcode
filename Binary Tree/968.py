# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = 0

    def traversal(self, cur):
        # 空节点，该节点有覆盖
        if cur is None:
            return 2

        left = self.traversal(cur.left)     # 左
        right = self.traversal(cur.right)       # 右

        # 情况1
        # 左右节点都有覆盖
        if left == 2 and right == 2:
            return 0

        # 情况2
        # left == 0 & & right == 0
        # 左右节点无覆盖
        # left == 1 & & right == 0
        # 左节点有摄像头，右节点无覆盖
        # left == 0 & & right == 1
        # 左节点有无覆盖，右节点摄像头
        # left == 0 & & right == 2
        # 左节点无覆盖，右节点覆盖
        # left == 2 & & right == 0
        # 左节点覆盖，右节点无覆盖
        if left == 0 or right == 0:
            self.result += 1
            return 1

        # 情况3
        # left == 1 & & right == 2
        # 左节点有摄像头，右节点有覆盖
        # left == 2 & & right == 1
        # 左节点有覆盖，右节点有摄像头
        # left == 1 & & right == 1
        # 左右节点都有摄像头
        # 其他情况前段代码均已覆盖
        if left == 1 or right == 1:
            return 2

        # 这个 return -1 逻辑不会走到这里。
        # return -1

    def minCameraCover(self, root: TreeNode) -> int:
        """
        Time O(n)
        Space O(n)
        局部最优：让叶子节点的父节点安摄像头，所用摄像头最少，整体最优：全部摄像头数量所用最少！
        大体思路就是从低到上，先给叶子节点父节点放个摄像头，然后隔两个节点放一个摄像头，直至到二叉树头结点。
        0，1，2 代表三种状态，0：无覆盖，1：有摄像头，2：有覆盖
        """

        #   情况4
        if self.traversal(root) == 0:    # root 无覆盖
            self.result += 1

        return self.result


node1 = TreeNode()
node2 = TreeNode()
node3 = TreeNode()
node4 = TreeNode()
node1.left = node2
node2.left = node3
node2.right = node4
s = Solution()
print(s.minCameraCover(node1))
