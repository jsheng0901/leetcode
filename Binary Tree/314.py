from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.column_table = defaultdict(list)
        self.min_col = 0
        self.max_col = 0

    def traversal(self, node, row, column):
        if node is None:
            return

        self.column_table[column].append((row, node.val))       # 加入每个节点的row和value进对应的column
        self.min_col = min(self.min_col, column)                # 更新最小column
        self.max_col = max(self.max_col, column)                # 更新最大column

        self.traversal(node.left, row + 1, column - 1)          # 进左节点，row + 1, column - 1
        self.traversal(node.right, row + 1, column + 1)         # 进右节点, row + 1， column + 1

        return

    def verticalOrder(self, root: [TreeNode]) -> [[int]]:
        """
        Time O(w * h log(h))    w: width of tree, h: height of tree
        Space O(log(h))
        binary tree的垂直遍历，构造一个dictionary存储 {col : [(row, value)]}的关系
        每个column对应的node节点的row和value，最后sort by row, 越小的在越前面，在一次把每个column的对应的list的sorted后
        的value加入result。这里同一行不用担心从左到右的顺序，因为前序遍历同一行，天然是从左到右添加节点。所以sort的时候要选第一个index，
        也就是sort by row就可以了。
        """
        # 空节点直接返回
        if root is None:
            return None

        self.traversal(root, 0, 0)
        result = []
        for i in range(self.min_col, self.max_col + 1):
            self.column_table[i].sort(key=lambda x: x[0])       # sort同一个column对应的node by row value
            result.append([val for row, val in self.column_table[i]])   # 加入sort过后的结果

        # 或者这样写
        # res = []
        # for col in range(self.min_col, self.max_col + 1):
        #     val = [node[1] for node in sorted(self.column_table[col], key=lambda x: x[0])]
        #     res.append(val)

        return result
