from typing import List


class NumMatrix1:

    def __init__(self, matrix: List[List[int]]):
        """
        Time O(1)
        Space O(1)
        暴力法，直接每个数叠加。
        """
        self.matrix = matrix

    def update(self, row: int, col: int, val: int) -> None:
        """
        Time O(n)
        """
        self.matrix[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Time O(m * n)
        """
        total = 0
        # 遍历区间里面每个数
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                # 叠加每个数
                total += self.matrix[i][j]

        return total


# 线段树的节点类
class TreeNode:
    def __init__(self, val=0):
        self.left = -1  # 区间左边界
        self.right = -1  # 区间右边界
        self.val = val  # 节点值（区间值）
        self.lazy_tag = None  # 区间和问题的延迟更新标记


# 线段树类
class SegmentTree:
    def __init__(self, nums, function):
        # 树的大小
        self.size = len(nums)
        # 构建 TreeNode 数组，也就是线段树数组
        self.tree = [TreeNode() for _ in range(4 * self.size)]
        # 原始数据
        self.nums = nums
        # function 是一个函数，左右区间的聚合方法
        self.function = function

        # 构建树
        if self.size > 0:
            self._build(0, 0, self.size - 1)

    def _build(self, index, left, right):
        # 构建线段树，节点的存储下标为 index，节点的区间为 [left, right]，此处相当于是前序遍历构建树
        node = self.tree[index]
        node.left = left
        node.right = right

        # 叶子节点，节点值为对应位置的元素值
        if left == right:
            node.val = self.nums[left]
            return

        # 左右节点划分点，分裂点
        mid = left + (right - left) // 2
        # 左子节点的存储下标
        left_index = index * 2 + 1
        # 右子节点的存储下标
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

    def update_point(self, i, val):
        # 单点更新，将 nums[i] 更改为 val
        self.nums[i] = val
        self._update_point(i, val, 0, 0, self.size - 1)

    def _update_point(self, i, val, index, left, right):
        # 单点更新，将 nums[i] 叠加 val。节点的存储下标为 index，节点的区间为 [left, right]

        # 当前节点
        node = self.tree[index]

        # 如果是叶子节点，则更新该节点的值
        if node.left == node.right:
            # 叶子节点，节点值修改为 val
            node.val = val
            return

        # 递归找到要更新的节点
        # 左右节点划分点
        mid = left + (right - left) // 2
        # 左子节点的存储下标
        left_index = index * 2 + 1
        # 右子节点的存储下标
        right_index = index * 2 + 2

        # 在左子树中更新节点值
        if i <= mid:
            self._update_point(i, val, left_index, left, mid)
        # 在右子树中更新节点值
        else:
            self._update_point(i, val, right_index, mid + 1, right)
        # 向上更新节点的区间值，类似构建的过程
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

        self._push_down(index)

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

    def _push_down(self, index):
        # 向下更新下标为 index 的节点所在区间的左右子节点的值和懒惰标记，当我们在查询此区间的时候才会进行这个操作

        node = self.tree[index]
        lazy_tag = node.lazy_tag
        if not lazy_tag:
            return

        # 左子节点的存储下标
        left_index = index * 2 + 1
        # 右子节点的存储下标
        right_index = index * 2 + 2

        left_node = self.tree[left_index]
        # 更新左子节点懒惰标记
        left_node.lazy_tag = lazy_tag
        # 左子树区间长度
        left_size = (left_node.right - left_node.left + 1)
        # 更新左子节点值
        left_node.val = lazy_tag * left_size

        right_node = self.tree[right_index]
        # 更新右子节点懒惰标记
        right_node.lazy_tag = lazy_tag
        # 右子树区间长度
        right_size = (right_node.right - right_node.left + 1)
        # 更新右子节点值
        right_node.val = lazy_tag * right_size

        # 更新当前节点的懒惰标记
        node.lazy_tag = None


class NumMatrix2:

    def __init__(self, matrix: List[List[int]]):
        """
        Time O(m * n)
        Space O(m * n)
        此题思路其实和307一样，只是307是一维的，这里是二维的，我们对每一行构建一个线段树，之后更新和求和就可以找到对应的行，然后对这一行
        进行高效的RSQ的算法。
        """
        rows, cols = len(matrix), len(matrix[0])
        # 存储每一行的线段数
        self.segment_trees = []
        for i in range(rows):
            nums = matrix[i]
            # 构建线段数对当前行
            segment_tree = SegmentTree(nums, lambda x, y: x + y)
            self.segment_trees.append(segment_tree)

    def update(self, row: int, col: int, val: int) -> None:
        """
        Time O(log(n))
        """
        # 拿到需要更新的树
        tree = self.segment_trees[row]
        # 更新对应的点
        tree.update_point(col, val)

        return

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Time O(m * log(n))
        """
        total = 0
        for i in range(row1, row2 + 1):
            tree = self.segment_trees[i]
            # 累计叠加每一行线段数RQS的结果
            total += tree.query_interval(col1, col2)

        return total


obj = NumMatrix2(matrix=[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(obj.sumRegion(2, 1, 4, 3))
obj.update(3, 2, 2)
print(obj.sumRegion(2, 1, 4, 3))
