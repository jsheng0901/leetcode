from typing import List


class Solution1:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        """
        Time O(n + q)   q -> number of query
        Space O(n)
        位运算和前缀和的组合，这里有个技巧如果要计算 arr[i]...arr[j]的位运算和，
        只需要计算 (arr[1]...arr[i]) ^ (arr[1]...arr[j + 1])，也就是累计的位运算转化成O(1)的一次位运算。
        """
        prefix_xor = [0] * (len(arr) + 1)
        # 位运算版本的前缀和
        for i in range(len(arr)):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

        res = []

        for query in queries:
            left = query[0]
            right = query[1]
            # 利用公式快速计算某个区间内的位运算和
            res.append(prefix_xor[right + 1] ^ prefix_xor[left])

        return res


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


class Solution2:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        """
        Time O(n + q * log(n))    q -> number of query
        Space O(n)
        线段树的解法，因为我们是对一个区间进行频繁地计算，此类型题目一定都可转化成线段树的结构来做。只需要把聚合函数变成位运算函数即可。
        """
        # 构建线段树，聚合函数选择位运算
        segment_tree = SegmentTree(arr, lambda x, y: (x ^ y))
        res = []
        for query in queries:
            # 得到区间内的结果
            ans = segment_tree.query_interval(query[0], query[1])
            res.append(ans)
        return res


s = Solution2()
print(s.xorQueries(arr=[1, 3, 4, 8], queries=[[0, 1], [1, 2], [0, 3], [3, 3]]))
print(s.xorQueries(arr=[4, 8, 2, 10], queries=[[2, 3], [1, 3], [0, 0], [0, 3]]))
