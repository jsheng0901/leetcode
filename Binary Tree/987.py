# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        # self.hash_map = defaultdict(lambda: defaultdict(list))
        self.hash_map = defaultdict(list)
        self.min_col = 0
        self.max_col = 0

    def traversal(self, node, i, j):
        if node is None:
            return

        self.hash_map[j].append((i, node.val))
        self.min_col = min(self.min_col, j)
        self.max_col = max(self.max_col, j)

        self.traversal(node.left, i + 1, j - 1)
        self.traversal(node.right, i + 1, j + 1)

        return

    def verticalTraversal(self, root: [TreeNode]) -> [[int]]:
        """
        total: O(n long(n / k)) time, dfs take O(n), sorted in each subgroup take n log(n / k), total add together
        类似314的dfs搜索，不同的是sort同一column的同一层的value值
        """
        res = []
        if root:
            self.traversal(root, 0, 0)
            for i in range(self.min_col, self.max_col + 1):
                res.append([val for row, val in sorted(self.hash_map[i])])

        return res
