from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
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


class Solution2:
    def __init__(self):
        self.column_table = defaultdict(list)
        self.min_col = 0
        self.max_col = 0

    def traversal(self, node):
        # 当前节点对应的column
        queue = [(node, 0)]
        while queue:
            node, column = queue.pop(0)
            self.column_table[column].append(node.val)              # 加入每个节点的row和value进对应的column
            self.min_col = min(self.min_col, column)                # 更新最小column
            self.max_col = max(self.max_col, column)                # 更新最大column
            # 空节点不入列队
            if node.left:
                # 左节点
                queue.append((node.left, column - 1))
            if node.right:
                # 右节点
                queue.append((node.right, column + 1))

        return

    def verticalOrder(self, root: [TreeNode]) -> [[int]]:
        """
        Time O(n)
        Space O(n)
        binary tree的垂直遍历，构造一个dictionary存储 {col : [value]}的关系
        整体思路和解法1一样，只是这里我们用BFS达到层序遍历，因为层序遍历的时候row是有序的遍历的，一定是从上到下加入列队，所以此时，
        column对应的list天然是已经按照row的顺序排序好的。所以直接返回所有keys即可。
        """
        # 空节点直接返回
        if root is None:
            return None

        self.traversal(root)
        result = []
        for i in range(self.min_col, self.max_col + 1):
            result.append([val for val in self.column_table[i]])

        return result


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3
s = Solution2()
print(s.verticalOrder(node1))
