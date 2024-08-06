from collections import defaultdict
from typing import List


class Solution1:
    def get_presum(self, nums):
        pre_sum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        return pre_sum

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        """
        Time O(n + n * d)  d -> range between lower and upper
        Space O(n)
        核心思想利用前缀和高效的计算区间和，我们可以遍历所有前缀和的数，然后在所有的range范围内计算需要的差值，也就是差值是否存在于前缀和数组
        内，然后统计频率，计算出现的个数。但是这里需要遍历整个range里面所有的数，如果range很大的话，非常费时，最终明显TLE.
        """
        # 得到前缀和数组
        pre_sum = self.get_presum(nums)

        # 统计前缀和里面出现的频率
        freq = defaultdict(int)
        res = 0
        for val in pre_sum:
            # target值是我们需要找到的两个前缀和只差
            for target in range(lower, upper + 1):
                # 如果另一个前缀和数出现过，则说明有符合要求的区间
                if val - target in freq:
                    # 加入结果
                    res += freq[val - target]
            # 记录出现频率
            freq[val] += 1

        return res


class Solution2:
    def __init__(self):
        self.count = 0

    def get_presum(self, nums):
        pre_sum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        return pre_sum

    def merge(self, left, right, lower, upper):
        # 计算有多少个区间和在范围内，核心思路在这
        start = 0
        end = 0
        # 我们遍历左边的所有元素
        # 这里我们只需要对比右数组和左数组的差值区间，因为左右数组内的所有组合已经在之前的递归下计算完了所有符合条件的情况
        for val in left:
            # 如果右边的元素减左边的当前元素小于最小值，说明我们需要继续找左边界，因为左数组是有序的
            while start < len(right) and right[start] - val < lower:
                # 移动左边界指针
                start += 1
            # 同理找右边界，我们需要找到大于最大值的界限
            while end < len(right) and right[end] - val <= upper:
                end += 1
            # 此区间内，所有右数组的数都可以和当前左数组数构成区间和满足条件
            self.count += end - start

        # 合并后的数组
        result = []
        while left and right:
            # 对比两个数组的第一个元素
            # 小的数字弹出并放进去结果数组
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        # 如果左边还有数字，一定是有序的直接加到结果后面
        if left:
            result.extend(left)
        # 同理右边
        if right:
            result.extend(right)

        return result

    def merge_sort(self, nums, lower, upper):
        # 归并排序标准模版
        # 走到底，只有一个元素，直接返回
        if len(nums) < 2:
            return nums
        # 找中间节点
        mid = len(nums) // 2
        # 左右递归，拿到合并成功的数组
        left = self.merge_sort(nums[:mid], lower, upper)
        right = self.merge_sort(nums[mid:], lower, upper)
        # 合并当前节点的左右子树数组
        sub_res = self.merge(left, right, lower, upper)

        return sub_res

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        """
        Time O(n + n * log(n))
        Space O(n)
        对一个数组频繁计算一个区间的和，明显要使用前缀和数组。之后就是在一个前缀和数组内找到所有区间组合在给定的范围内。这里参考315，找到
        一个数后面所有比它小的数的思路，我们完全可以使用归并排序的思路，每次左右数组合并的时候，刚好可以判断右数组有多少个数字可以和左数组
        差值在给定的范围内，详细见注释。
        """
        # 得到前缀和数组
        pre_sum = self.get_presum(nums)
        # 归并排序计算个数
        _ = self.merge_sort(pre_sum, lower, upper)

        return self.count


# 线段树的节点类
class TreeNode:
    def __init__(self, val=0):
        self.left = -1  # 区间左边界
        self.right = -1  # 区间右边界
        self.val = val  # 节点值（区间值）
        self.lazy_tag = None  # 区间和问题的延迟更新标记


# 线段树类
class SegmentTreeArray:
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
            node.val += val
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


class Solution3:
    def get_presum(self, nums):
        pre_sum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        return pre_sum

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        """
        Time O(n * log(c))  c -> 线段树根节点维护的区间长度
        Space O(n * log(c))
        同样线段树的思路，同思路4，只是这里的线段树是数组类型实现的线段树，遇到比较大的数的范围时候会memory超出。其次这里因为是数组，
        需要保证数的值对应index是一样的，所以我们要用shift offset来实现。
        """
        pre_sum = self.get_presum(nums)
        # 平移的距离
        offset = 2 * 32 - 1
        # 总共多少个可能的数值在数组里面
        size = 2 * offset + 1
        # 构建线段数数组
        tree = [0] * size
        # 初始化线段数
        segment_tree = SegmentTreeArray(tree, lambda x, y: x + y)

        res = 0
        for val in pre_sum:
            left = val - upper
            right = val - lower
            # 注意要shift
            res += segment_tree.query_interval(left + offset, right + offset)
            # 更新当前数对应的线段数内的index的值，要shift先
            segment_tree.update_point(val + offset, 1)

        return res


class SegTreeNode:
    def __init__(self, left=-1, right=-1, val=0, lazy_tag=None, left_node=None, right_node=None):
        self.left = left  # 区间左边界
        self.right = right  # 区间右边界
        self.mid = left + (right - left) // 2  # 区间中间点
        self.left_node = left_node  # 区间左节点
        self.right_node = right_node  # 区间右节点
        self.val = val  # 节点值（区间值）
        self.lazy_tag = lazy_tag  # 区间问题的延迟更新标记


# 动态开点线段树类，不带延迟更新标记的版本
class SegmentTree:
    # 初始化线段树接口
    def __init__(self, function):
        self.tree = SegTreeNode(-2 ** 31, 2 ** 31 - 1)
        self.function = function  # function 是一个函数，左右区间的聚合方法

    # 单点更新，将 nums[i] 更改为 val
    def update_point(self, i, val):
        self._update_point(i, val, self.tree)

    # 区间查询，查询区间为 [q_left, q_right] 的区间值
    def query_interval(self, q_left, q_right):
        return self._query_interval(q_left, q_right, self.tree)

    # 以下为内部实现方法
    # 单点更新，将 nums[i] 更改为 val。node 节点的区间为 [node.left, node.right]
    def _update_point(self, i, val, node):
        if node.left == node.right:
            node.val += val  # 叶子节点，节点值修改为 val
            return

        if i <= node.mid:  # 在左子树中更新节点值
            if node.left_node is None:
                node.left_node = SegTreeNode(node.left, node.mid)
            self._update_point(i, val, node.left_node)
        else:  # 在右子树中更新节点值
            if node.right_node is None:
                node.right_node = SegTreeNode(node.mid + 1, node.right)
            self._update_point(i, val, node.right_node)
        self._push_up(node)  # 向上更新节点的区间值

    # 区间查询，在线段树的 [left, right] 区间范围中搜索区间为 [q_left, q_right] 的区间值
    def _query_interval(self, q_left, q_right, node):
        if node.left >= q_left and node.right <= q_right:  # 节点所在区间被 [q_left, q_right] 所覆盖
            return node.val  # 直接返回节点值
        if node.right < q_left or node.left > q_right:  # 节点所在区间与 [q_left, q_right] 无关
            return 0

        res_left = 0  # 左子树查询结果
        res_right = 0  # 右子树查询结果
        if q_left <= node.mid:  # 在左子树中查询
            if node.left_node is None:
                node.left_node = SegTreeNode(node.left, node.mid)
            res_left = self._query_interval(q_left, q_right, node.left_node)
        if q_right > node.mid:  # 在右子树中查询
            if node.right_node is None:
                node.right_node = SegTreeNode(node.mid + 1, node.right)
            res_right = self._query_interval(q_left, q_right, node.right_node)
        return self.function(res_left, res_right)  # 返回左右子树元素值的聚合计算结果

    # 向上更新 node 节点区间值，节点的区间值等于该节点左右子节点元素值的聚合计算结果
    def _push_up(self, node):
        # 注意这里没有延迟标记的写法
        left_node = node.left_node
        right_node = node.right_node
        # 动态开点，遇到不存在的节点，直接赋值0
        left_node_val = left_node.val if left_node else 0
        right_node_val = right_node.val if right_node else 0

        node.val = self.function(left_node_val, right_node_val)


class Solution4:
    def get_presum(self, nums):
        pre_sum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        return pre_sum

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        """
        Time O(n * log(c))  c -> 线段树根节点维护的区间长度
        Space O(n * log(c))
        此题可以转化成线段树的思路，还是前缀和的数组，当我们遍历到pre_sum[i]的时候，我们需要找到的另一个pre_sum[j]，一定要符合
        lower <= pre_sum[i] - pre_sum[j] <= upper，j < i 这个不等式，也就是说我们需要落在这个区间内有多少个数
        [pre_sum[i] - upper, pre_sum[i] - lower]，区间内所有的数都符合上面不等式，对此我们可以利用线段数RQS的方式，对一个区间快速的
        提取结果，需要注意的是这里的数可能很大，所以我们采用动态开点线段树，离散化存储，不需要开一个会超memory的连续数组。详细见注释。
        """
        # 得到前缀和数组
        pre_sum = self.get_presum(nums)
        # 初始化线段数，这里写的是动态开点线段树不带延迟标记的版本，区间的长度为题目给的最大范围
        segment_tree = SegmentTree(lambda x, y: x + y)

        res = 0
        # 从左到右遍历前缀和数组，保证不会计算重复
        for val in pre_sum:
            # 需要查询的区间下限
            left = val - upper
            # 需要查询的区间上限
            right = val - lower
            # 累加查询结果，也就是落在这个区间的里面数的个数，
            # 注意这里要先查询，再更新，因为前缀和自己不能算在里面，我们需要的是 j < i 对应的index
            res += segment_tree.query_interval(left, right)
            # 注意这里一定要判断一个更新的时候的数是不是在区间内，否则会重复累加，比如测试数据1的情况
            if -2 ** 31 <= val <= 2 ** 31 - 1:
                # 更新当前数对应的线段数内的index的值
                segment_tree.update_point(val, 1)

        return res


s = Solution4()
print(s.countRangeSum(nums=[-2147483647, 0, -2147483647, 2147483647], lower=-564, upper=3864))
print(s.countRangeSum(nums=[-2, 5, -1], lower=-2, upper=2))
print(s.countRangeSum(nums=[0], lower=0, upper=0))
