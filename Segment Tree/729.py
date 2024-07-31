from sortedcontainers import SortedList


class MyCalendar1:

    def __init__(self):
        self.calendar = []

    def binary_search_right_bound(self, start):
        # 标准二分法查找右边界的写法
        left = 0
        right = len(self.calendar) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if self.calendar[mid][0] < start:
                left = mid + 1
            # 核心不一样的地方在这里，因为是右边界，等于的时候我们移动左指针
            elif self.calendar[mid][0] == start:
                left = mid + 1
            elif self.calendar[mid][0] > start:
                right = mid - 1

        # 出循环的时候是 right < left + 1
        # 此时右指针是边界，左指针是第一个比target大的index，我们需要左指针的结果
        return left

    def book(self, start: int, end: int) -> bool:
        """
        Time O(n * log(n))
        Space O(n)
        本质上是构建以start为有序的数组，每次插入的时候进行二分法查找，找到二分法的插入空间，如果不是第一个也不是最后一个，check插入index
        的前一位，如果新的start小于前一个的end，或者原理插入index的start小于当前插入的end，也说明一定有交集，如果不是上述情况说明一个可以。
        """
        # 二分法找右边界的写法，找到第一个大于当前target值的index，也就是我们要插入的index
        # 如果是空日志，不需要额外判断，得到右边界是0，此时会直接加入日志并且返回true
        idx = self.binary_search_right_bound(start)

        # case1：当前start和前一个的end有交集
        # case2：当前end和原始要插入的位置的start有交集
        if (idx > 0 and self.calendar[idx - 1][1] > start) or (
                idx < len(self.calendar) and self.calendar[idx][0] < end):
            return False

        # 插入找到的位置
        self.calendar.insert(idx, (start, end))

        return True


class MyCalendar2:

    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        """
        Time O(n * log(n))
        Space O(n)
        一模一样的思路，只是换成build in的有序数组来实现。
        """
        # 找到需要插入的右边界，同思路1的二分法查找边界
        idx = self.calendar.bisect_right((start, end))

        if (idx > 0 and self.calendar[idx - 1][1] > start) or (
                idx < len(self.calendar) and self.calendar[idx][0] < end):
            return False

        self.calendar.add((start, end))

        return True


# 线段树的节点类
class SegTreeNode:
    def __init__(self, left=-1, right=-1, val=0, lazy_tag=None, left_node=None, right_node=None):
        self.left = left  # 区间左边界
        self.right = right  # 区间右边界
        self.mid = left + (right - left) // 2   # 区间中间点
        self.left_node = left_node  # 区间左节点
        self.right_node = right_node  # 区间右节点
        self.val = val  # 节点值（区间值）
        self.lazy_tag = lazy_tag  # 区间问题的延迟更新标记


# 动态开点线段树类
class SegmentTree:
    # 初始化线段树接口
    def __init__(self, function):
        self.tree = SegTreeNode(0, int(1e9))
        self.function = function  # function 是一个函数，左右区间的聚合方法

    # 单点更新，将 nums[i] 更改为 val
    def update_point(self, i, val):
        self._update_point(i, val, self.tree)

    # 区间更新，将区间为 [q_left, q_right] 上的元素值修改为 val
    def update_interval(self, q_left, q_right, val):
        self._update_interval(q_left, q_right, val, self.tree)

    # 区间查询，查询区间为 [q_left, q_right] 的区间值
    def query_interval(self, q_left, q_right):
        return self._query_interval(q_left, q_right, self.tree)

    # 获取 nums 数组接口：返回 nums 数组
    def get_nums(self, length):
        nums = [0 for _ in range(length)]
        for i in range(length):
            nums[i] = self.query_interval(i, i)
        return nums

    # 以下为内部实现方法

    # 单点更新，将 nums[i] 更改为 val。node 节点的区间为 [node.left, node.right]
    def _update_point(self, i, val, node):
        if node.left == node.right:
            node.val = val  # 叶子节点，节点值修改为 val
            return

        if i <= node.mid:  # 在左子树中更新节点值
            self._update_point(i, val, node.left_node)
        else:  # 在右子树中更新节点值
            self._update_point(i, val, node.right_node)
        self._push_up(node)  # 向上更新节点的区间值

    # 区间更新
    def _update_interval(self, q_left, q_right, val, node):
        if node.left >= q_left and node.right <= q_right:  # 节点所在区间被 [q_left, q_right] 所覆盖
            if node.lazy_tag is not None:
                node.lazy_tag += val  # 将当前节点的延迟标记增加 val
            else:
                node.lazy_tag = val  # 将当前节点的延迟标记增加 val
            node.val += val  # 当前节点所在区间每个元素值增加 val
            return
        if node.right < q_left or node.left > q_right:  # 节点所在区间与 [q_left, q_right] 无关
            return 0

        self._push_down(node)  # 向下更新节点所在区间的左右子节点的值和懒惰标记

        if q_left <= node.mid:  # 在左子树中更新区间值
            self._update_interval(q_left, q_right, val, node.left_node)
        if q_right > node.mid:  # 在右子树中更新区间值
            self._update_interval(q_left, q_right, val, node.right_node)

        self._push_up(node)

    # 区间查询，在线段树的 [left, right] 区间范围中搜索区间为 [q_left, q_right] 的区间值
    def _query_interval(self, q_left, q_right, node):
        if node.left >= q_left and node.right <= q_right:  # 节点所在区间被 [q_left, q_right] 所覆盖
            return node.val  # 直接返回节点值
        if node.right < q_left or node.left > q_right:  # 节点所在区间与 [q_left, q_right] 无关
            return 0

        self._push_down(node)  # 向下更新节点所在区间的左右子节点的值和懒惰标记

        res_left = 0  # 左子树查询结果
        res_right = 0  # 右子树查询结果
        if q_left <= node.mid:  # 在左子树中查询
            res_left = self._query_interval(q_left, q_right, node.left_node)
        if q_right > node.mid:  # 在右子树中查询
            res_right = self._query_interval(q_left, q_right, node.right_node)
        return self.function(res_left, res_right)  # 返回左右子树元素值的聚合计算结果

    # 向上更新 node 节点区间值，节点的区间值等于该节点左右子节点元素值的聚合计算结果
    def _push_up(self, node):
        if node.left_node and node.right_node:
            node.val = self.function(node.left_node.val, node.right_node.val)

    # 向下更新 node 节点所在区间的左右子节点的值和懒惰标记
    def _push_down(self, node):
        if node.left_node is None:
            node.left_node = SegTreeNode(node.left, node.mid)
        if node.right_node is None:
            node.right_node = SegTreeNode(node.mid + 1, node.right)

        lazy_tag = node.lazy_tag
        if node.lazy_tag is None:
            return

        if node.left_node.lazy_tag is not None:
            node.left_node.lazy_tag += lazy_tag  # 更新左子节点懒惰标记
        else:
            node.left_node.lazy_tag = lazy_tag  # 更新左子节点懒惰标记
        node.left_node.val += lazy_tag  # 左子节点每个元素值增加 lazy_tag

        if node.right_node.lazy_tag is not None:
            node.right_node.lazy_tag += lazy_tag  # 更新右子节点懒惰标记
        else:
            node.right_node.lazy_tag = lazy_tag  # 更新右子节点懒惰标记
        node.right_node.val += lazy_tag  # 右子节点每个元素值增加 lazy_tag

        node.lazy_tag = None  # 更新当前节点的懒惰标记


class MyCalendar3:

    def __init__(self):
        # 线段树的聚合函数选择取最大值，表示记录当前区间保存了多少个日程区间个数
        self.segment_tree = SegmentTree(lambda x, y: x + y)

    def book(self, start: int, end: int) -> bool:
        """
        Time O(n * log(n)) n -> 10^9
        Space O(1)
        每次都是一次二分法搜索，不过这里区间的长度远大于思路一和二的长度，因为线段树的区间取值是从0到最大值。
        核心思路，构建一棵线段树。每个线段树的节点类存储当前区间中保存的日程区间个数。
        每次booking，从线段树中查询 [start, end - 1] 区间上保存的日程区间个数，
        如果日程区间个数大于等于 1，则说明该日程添加到日历中会导致重复预订，则直接返回 False，
        如果日程区间个数小于 1，则说明该日程添加到日历中不会导致重复预定，则在线段树中将区间 [start, end - 1] 的日程区间个数 + 1，返回True
        """
        # 如果大于等于1
        if self.segment_tree.query_interval(start, end - 1) >= 1:
            return False

        # 没有重复区间，进行此区间的更新
        self.segment_tree.update_interval(start, end - 1, 1)
        return True


obj = MyCalendar3()
print(obj.book(start=10, end=20))
print(obj.book(start=15, end=25))
print(obj.book(start=20, end=30))
