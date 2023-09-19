from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.acc_map = {0: 1}

    def traversal(self, root, acc, sum):
        if not root:
            return 0

        current_acc = acc + root.val
        self.acc_map.setdefault(current_acc, 0)
        self.acc_map[current_acc] += 1  # 记录出现的次数
        left_sum = self.traversal(root.left, current_acc, sum)
        right_sum = self.traversal(root.right, current_acc, sum)
        self.acc_map[current_acc] -= 1  # 回溯出现过的次数，当回溯这个节点的时候

        return self.acc_map.get(current_acc - sum, 0) + left_sum + right_sum  # 统计rest的次数

    def pathSum(self, root: TreeNode, sum: int) -> int:
        """用hashmap来记录之前所有有过的path的sum的出现次数，统计是否有过路径的时候统计cur_sum - target是否出现过"""
        if root:
            return self.traversal(root, 0, sum)
        else:
            return 0


class Solution2:
    def __init__(self):
        self.count = 0
        self.sum_dict = defaultdict(int)

    def traversal(self, node, cur_sum, targetSum):
        if node is None:
            return

        # 记录到当前节点总和
        cur_sum += node.val
        # 检查差值是否出现过
        rest = cur_sum - targetSum
        # 如果有出现，则记录进结果
        if rest in self.sum_dict:
            self.count += self.sum_dict[rest]
        # 记录下当前总和频率 +1
        self.sum_dict[cur_sum] += 1
        # 左右递归
        self.traversal(node.left, cur_sum, targetSum)
        self.traversal(node.right, cur_sum, targetSum)
        # 离开当前节点，回溯，减去出现的频率 -1
        self.sum_dict[cur_sum] -= 1

        return

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Time O(n)
        Space O(n)
        前序遍历记录每到一个节点此时从root到此节点的总和，并且记录在全局变量中，记录出现的频率。同时检查root到当前节点离target值还差多少。
        如果这个值出现在我们的记录里面，说明之前有root到前面的节点path达到rest值。count全局变量记录 +frequency。这里因为是找符合条件
        的path，并且我们有全局变量dictionary来记录出现的值的频率，所以当离开此节点的时候要回溯，不然就会出现在另一条path里面check其它path
        之前出现的值。
        """
        # 初始化0的频率，因为可能会有走到底刚好等于target值的情况
        self.sum_dict[0] += 1
        self.traversal(root, 0, targetSum)

        return self.count


node1 = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(-3)
node4 = TreeNode(3)
node5 = TreeNode(2)
node6 = TreeNode(11)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
s = Solution2()
print(s.pathSum(root=node1, targetSum=8))
