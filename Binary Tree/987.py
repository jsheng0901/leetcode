# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.hash_map = defaultdict(list)
        self.min_col = 0
        self.max_col = 0

    def traversal(self, node, i, j):
        if node is None:
            return

        # 前序遍历记录每个节点的行，列 和值
        self.hash_map[j].append((i, node.val))
        # 统计最大最小列的值，方便后续遍历每一列
        self.min_col = min(self.min_col, j)
        self.max_col = max(self.max_col, j)

        self.traversal(node.left, i + 1, j - 1)
        self.traversal(node.right, i + 1, j + 1)

        return

    def verticalTraversal(self, root: [TreeNode]) -> [[int]]:
        """
        Time: O(n * log(n/k)), dfs take O(n), sorted in each subgroup take n * log(n/k)
        Space: O(n)
        前序遍历的思路，类似314的dfs搜索，不同的是sort同一column的同一层的value值。用一个dictionary来记录每列对应的节点的行数和值。
        这里需要注意的是sorted一个tuple的list，会sort每一个tuple里面的顺序而不是整个list的顺序。
        """
        res = []
        if root:
            self.traversal(root, 0, 0)
            for i in range(self.min_col, self.max_col + 1):
                # sorted会对list里面每个tuple进行排序
                res.append([val for row, val in sorted(self.hash_map[i])])

        return res
