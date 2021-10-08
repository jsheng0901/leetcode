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
        self.acc_map[current_acc] += 1          # 记录出现的次数
        left_sum = self.traversal(root.left, current_acc, sum)
        right_sum = self.traversal(root.right, current_acc, sum)
        self.acc_map[current_acc] -= 1          # 回溯出现过的次数，当回溯这个节点的时候

        return self.acc_map.get(current_acc - sum, 0) + left_sum + right_sum    # 统计rest的次数

    def pathSum(self, root: TreeNode, sum: int) -> int:
        """用hashmap来记录之前所有有过的path的sum的出现次数，统计是否有过路径的时候统计cur_sum - target是否出现过"""
        if root:
            return self.traversal(root, 0, sum)
        else:
            return 0