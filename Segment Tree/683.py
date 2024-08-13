from typing import List

from sortedcontainers import SortedList


class TreeNode:
    def __init__(self, val=0):
        self.left = -1  # 区间左边界
        self.right = -1  # 区间右边界
        self.val = val  # 节点值（区间值）
        self.lazy_tag = None  # 区间和问题的延迟更新标记


# 线段树类
class SegmentTreeArray:
    def __init__(self, nums, function):
        # 整个线段树，构造的时候需要遍历所有区间单点，单点更新的时候其实是二叉搜索树，二分发的思路，时间上是 O(log(n)) 的复杂度，
        # 区间更新和区间查询利用延迟标记，达到平均下来也都是 O(log(n) 的时间复杂度。
        # 如果只有单点更新加区间查询，带不带延迟标记都一样，因为区间查询和区间更新才是配套使用延迟标记的组合，达到降低时间复杂度的效果。
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
            self.__build(0, 0, self.size - 1)

    def __build(self, index, left, right):
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
        self.__build(left_index, left, mid)
        # 递归创建右子树
        self.__build(right_index, mid + 1, right)
        # 向上更新节点的区间值，此处相当于是后续遍历更新当前节点区间值
        self.__push_up(index)

        return

    def __push_up(self, index):
        # 向上更新下标为 index 的节点区间值，节点的区间值等于该节点左右子节点元素值的聚合计算结果，只更新当前节点
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
        self.__update_point(i, val, 0, 0, self.size - 1)

    def __update_point(self, i, val, index, left, right):
        # 单点更新，将 nums[i] 更改为 val。节点的存储下标为 index，节点的区间为 [left, right]
        # 单点更新和区间更新不一样得地方在于，单点更新不需要push down，不需要查看延迟标记，更新完叶子结点后，每一层都会通过push up，
        # 向上更新，来实现当前节点也就是父节点的更新
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
            self.__update_point(i, val, left_index, left, mid)
        # 在右子树中更新节点值
        else:
            self.__update_point(i, val, right_index, mid + 1, right)
        # 向上更新节点的区间值，类似构建的过程
        self.__push_up(index)

    def query_interval(self, q_left, q_right):
        # 区间查询，查询区间为 [q_left, q_right] 的区间值
        return self.__query_interval(q_left, q_right, 0, 0, self.size - 1)

    def __query_interval(self, q_left, q_right, index, left, right):
        # 区间查询，在线段树的 [left, right] 区间范围中搜索区间为 [q_left, q_right] 的区间值

        # 节点所在区间被 [q_left, q_right] 完全覆盖
        if left >= q_left and right <= q_right:
            # 直接返回节点值
            return self.tree[index].val
        # 节点所在区间与 [q_left, q_right] 无关，节点完全在查询区间外，一定要有这个返回值，为后续遍历位置左右返回值聚合函数使用
        if right < q_left or left > q_right:
            return 0

        # 向下更新当前节点的子节点，同理 update interval 的逻辑
        self.__push_down(index)

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
            res_left = self.__query_interval(q_left, q_right, left_index, left, mid)
        # 在右子树中查询
        if q_right > mid:
            res_right = self.__query_interval(q_left, q_right, right_index, mid + 1, right)

        # 返回左右子树元素值的聚合计算结果
        return self.function(res_left, res_right)

    def __push_down(self, index):
        # 向下更新下标为 index 的节点所在区间的左右子节点的值和懒惰标记，当我们在查询此区间或者更新区间的时候才会进行这个操作
        # 在向下更新的时候，其实我们只更新当前节点的左右子节点的值，
        # 当前节点的值，在update interval的时候结束当前节点的时候，向上更新会更新当前节点的值

        # 先判断一下当前节点是否被标记过，如果没有被标记过说明并没有更新到此区间，直接跳过
        node = self.tree[index]
        lazy_tag = node.lazy_tag
        if lazy_tag is None:
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
        # 更新左子节点值，比如val是3，左子树的控制的区间长度为3，那么我们更新左子树值应该是控制区间内每个元素都会 +3，也就是长度 * val
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


class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        """
        Time O(n * log(n))
        Space O(n)
        对于每个灯泡，我们需要计算的是在这个灯泡的左右两边可能构成区间是k个长度的区间内，是否所有灯泡都是关的。我们可以初始化所有灯泡为1，
        开一个灯泡变成0，则符合区间内的和应该刚好等于k值。而这个值我们可以通过线段是高效的计算区间和，并且同时进行单点更新。
        """
        # 初始化线段树需要存储的数组，初始化值为1
        trees = [1] * (len(bulbs) + 1)
        # 构建线段树
        segment_tree = SegmentTreeArray(trees, lambda x, y: x + y)

        # 遍历每一个灯泡
        for i, bulb in enumerate(bulbs):
            # 标记是否需要check灯泡两边的区间
            left_side_check = True
            right_side_check = True
            # 单点更新灯泡为打开
            segment_tree.update_point(bulb, 0)
            # 灯泡左边的需要查询的区间
            left_side_left = bulb - k
            left_side_right = bulb - 1
            # 灯泡右边的需要查询的区间
            right_side_left = bulb + 1
            right_side_right = bulb + k

            # 如果左边查询区间越界，或者左边两个端点的灯泡没有打开，则不需要查左边的区间
            if left_side_left < 1 or trees[left_side_left - 1] == 1:
                left_side_check = False
            # 同理右边的区间也不需要查
            if right_side_right >= len(trees) - 1 or trees[right_side_right + 1] == 1:
                right_side_check = False

            # query left side
            # 查左边的区间和
            if left_side_check:
                # 线段树高效查区间聚合结果
                num = segment_tree.query_interval(left_side_left, left_side_right)
                # 如果符合要求，说明找到第一个最短时间的结果
                if num == k:
                    # 注意要 +1，变成对应的天
                    day = i + 1
                    # 直接返回结果
                    return day

            # query right side
            # 同理上面左区间的查找
            if right_side_check:
                num = segment_tree.query_interval(right_side_left, right_side_right)
                if num == k:
                    day = i + 1
                    return day

        # 如果都没有，则说明不存在，返回 -1
        return -1


class Solution2:
    def kEmptySlots(self, bulbs, k):
        """
        Time O(n * log(n))
        Space O(n)
        利用有序数组，我们每次需要知道的是一个灯泡两边都打开的灯泡区间内，是否有符合要求的区间，计算多少个关的灯泡，可以直接利用两个开灯泡的
        端点进行相减得到。这里最重要的是需要高效的直接一个灯泡两边开的灯泡是哪个，利用有序数组插入的方式快速找到。
        """
        # 存储已经打开的灯泡是哪个
        active = SortedList()

        # 遍历所有灯泡
        for day, flower in enumerate(bulbs, 1):
            # 当前灯泡插入进有序数组的时候位置
            i = active.bisect_left(bulbs)
            # 当前插入位置的左右端点
            for neighbor in active[i - (i > 0):i + 1]:
                # 计算长度，是否满足k
                if abs(neighbor - bulbs) - 1 == k:
                    # 满足直接返回
                    return day
            # 插入当前开的灯泡
            active.add(bulbs)

        # 如果都没有，则说明不存在，返回 -1
        return -1


class Solution3:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        """
        Time O(n)
        Space O(n)
        其实这题还可以换一个角度，我们记录所有灯泡开的时间，维护一个k大小的区间，表示区间有k个灯泡，现在只需要知道这个区间内所有灯泡是否
        开的时间都大于两个端点灯泡开的时间，都大于的话，说明两个端点开灯泡的时候是符合条件的，k个区间内的灯泡都是关的。如果区间内有灯泡开的
        时间更早，说明不符合全是关的条件，此时我们找到一个更小的开灯泡的时间，直接继续在这个新地开灯泡的时间区间遍历。详细见注释
        """
        # days[i]表示第i个灯泡打开的时间
        days = [0] * len(bulbs)
        for i, bulb in enumerate(bulbs, 1):
            # 整体shift一位左边，因为灯泡是index-1位底的
            days[bulb - 1] = i

        # 区间左右端点
        left = 0
        right = left + k + 1
        # 记录最小时间
        res = float('inf')

        # 遍历整个days数组
        while right < len(days):
            # 遍历区间窗口内所有灯泡开的时间
            for i in range(left + 1, right):
                # 如果有不符合条件的灯泡，也就是有灯泡开得更早
                if days[i] < days[left] or days[i] < days[right]:
                    # 找到更早开的灯泡位置，作为新的窗口端点
                    left = i
                    right = i + k + 1
                    break
            # 如果没有进入break，说明找到合理的窗口，此时统计最早构建此区间的时间，最大值是代表这个左右区间构成的时间，
            # 最小值是记录全局最早符合条件的区间
            else:
                res = min(res, max(days[left], days[right]))
                # 更新下一个搜索区间
                left = right
                right = left + k + 1

        # 如果都没有，则说明不存在，返回 -1
        return res if res != float('inf') else -1


s = Solution3()
print(s.kEmptySlots(bulbs=[1, 3, 2], k=1))
print(s.kEmptySlots(bulbs=[1, 2, 3], k=1))
print(s.kEmptySlots(bulbs=[6, 5, 8, 9, 7, 1, 10, 2, 3, 4], k=2))
