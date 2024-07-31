from typing import List


class TreeNode:
    def __init__(self, val=0):
        self.left = -1  # 区间左边界
        self.right = -1  # 区间右边界
        self.val = val  # 节点值（区间值）


class SegmentTree:
    def __init__(self, nums, functon):
        # 树的大小
        self.size = len(nums)
        # 构建 TreeNode 数组，也就是线段树数组
        self.tree = [TreeNode() for _ in range(4 * self.size)]
        # 原始数据
        self.nums = nums
        self.function = functon

        # 构建树
        if self.size > 0:
            self._build(0, 0, self.size - 1)

    def _build(self, index, left, right):
        node = self.tree[index]
        node.left = left
        node.right = right

        # 叶子节点，节点值为对应位置的元素值
        if left == right:
            node.val = self.nums[left]
            return

        mid = left + (right - left) // 2
        left_index = index * 2 + 1
        right_index = index * 2 + 2

        # 递归创建左子树
        self._build(left_index, left, mid)
        # 递归创建右子树
        self._build(right_index, mid + 1, right)
        # 向上更新节点的区间值，此处相当于是后续遍历更新当前节点区间值
        self._push_up(index)

        return

    def _push_up(self, index):
        # 向上更新下标为 index 的节点区间值，节点的区间值等于该节点左右子节点元素值的聚合计算结果
        # 左子节点的存储下标
        left_index = index * 2 + 1
        # 右子节点的存储下标
        right_index = index * 2 + 2
        # 当前树节点
        node = self.tree[index]
        left_node = self.tree[left_index]
        right_node = self.tree[right_index]
        # 赋值
        node.val = self.function(left_node.val, right_node.val)

        return

    def update_point(self, i, val):
        # 单点更新，将 nums[i] 更改为 val
        self.nums[i] = val
        self._update_point(i, val, 0, 0, self.size - 1)

    def _update_point(self, i, val, index, left, right):
        node = self.tree[index]

        if node.left == node.right:
            node.val = val
            return

        # 递归找到要更新的节点
        # 左右节点划分点
        mid = left + (right - left) // 2
        # 左子节点的存储下标
        left_index = index * 2 + 1
        # 右子节点的存储下标
        right_index = index * 2 + 2

        if i <= mid:
            self._update_point(i, val, left_index, left, mid)
        else:
            self._update_point(i, val, right_index, mid + 1, right)

        self._push_up(index)

    def query_interval(self, q_left, q_right):
        # 区间查询，查询区间为 [q_left, q_right] 的区间值
        return self._query_interval(q_left, q_right, 0, 0, self.size - 1)

    def _query_interval(self, q_left, q_right, index, left, right):
        # 区间查询，在线段树的 [left, right] 区间范围中搜索区间为 [q_left, q_right] 的区间值

        # 节点所在区间被 [q_left, q_right] 完全覆盖
        if left >= q_left and right <= q_right:
            # 直接返回节点值
            return self.tree[index].val
        # 节点所在区间与 [q_left, q_right] 无关，节点完全在查询区间外
        if right < q_left or left > q_right:
            return 0

        # 左右节点划分点
        mid = left + (right - left) // 2
        # 左子节点的存储下标
        left_index = index * 2 + 1
        # 右子节点的存储下标
        right_index = index * 2 + 2

        # 左子树查询结果
        res_left = 0
        # 右子树查询结果
        res_right = 0
        # 在左子树中查询
        if q_left <= mid:
            res_left = self._query_interval(q_left, q_right, left_index, left, mid)
        # 在右子树中查询
        if q_right > mid:
            res_right = self._query_interval(q_left, q_right, right_index, mid + 1, right)

        # 返回左右子树元素值的聚合计算结果
        return self.function(res_left, res_right)


class NumArray:

    def __init__(self, nums: List[int]):
        """
        Time O(n)
        space O(n)
        此题可以用O(n)的方式进行遍历得到答案，但是当数据量很大的时候明显太慢了，
        对于所有RSQ的问题都可以使用线段树把 O(n) 的时间降低到 O(log(n))
        构建线段树，需要遍历所有元素并计算和。
        """
        self.nums = nums
        self.segment_tree = SegmentTree(self.nums, lambda x, y: x + y)

    def update(self, index: int, val: int) -> None:
        """
        Time O(log(n)）
        Space O(1)
        更新线段树中的某个节点的值
        """
        self.segment_tree.update_point(index, val)

    def sumRange(self, left: int, right: int) -> int:
        """
        Time O(log(n)
        Space O(1)
        查询数组中某个范围的和，也就是线段树中的某个几个节点的和
        """
        return self.segment_tree.query_interval(left, right)


obj = NumArray(nums=[1, 3, 5])
print(obj.sumRange(left=0, right=2))
obj.update(index=1, val=2)
print(obj.sumRange(left=0, right=2))
