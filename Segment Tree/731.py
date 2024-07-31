from sortedcontainers import SortedList


class SegTreeNode:
    def __init__(self, left=-1, right=-1, val=0, lazy_tag=None, left_node=None, right_node=None):
        self.left = left  # 区间左边界
        self.right = right  # 区间右边界
        self.mid = left + (right - left) // 2  # 区间中间点
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


class MyCalendarTwo1:

    def __init__(self):
        # 线段树的聚合函数选择取最大值，表示记录当前区间保存了最多多少个日程区间个数
        self.segment_tree = SegmentTree(lambda x, y: max(x, y))

    def book(self, start: int, end: int) -> bool:
        """
        Time O(log(n)) n -> 10^9
        Space O(1)
        同729，只是换一种聚合函数的写法，但是729也可以用731这个聚合函数。
        每次都是一次二分法搜索，不过这里区间的长度远大于思路一和二的长度，因为线段树的区间取值是从0到最大值。
        核心思路，构建一棵线段树。每个线段树的节点类存储当前区间中保存的日程区间最多个数。
        每次booking，从线段树中查询 [start, end - 1] 区间上保存的日程区间个数，
        如果日程区间个数大于等于 1，则说明该日程添加到日历中会导致重复预订，则直接返回 False，
        如果日程区间个数小于 1，则说明该日程添加到日历中不会导致重复预定，则在线段树中将区间 [start, end - 1] 的日程区间个数 + 1，返回True
        """
        # 如果大于等于1
        if self.segment_tree.query_interval(start, end - 1) >= 2:
            return False

        # 没有重复区间，进行此区间的更新
        self.segment_tree.update_interval(start, end - 1, 1)

        return True


class MyCalendarTwo2:

    def __init__(self):
        self.single_booked = []
        self.double_booked = []

    def book(self, start: int, end: int) -> bool:
        """
        Time O(n)
        Space O(n)
        用两个数组存储单一日志，和出现过的有交集的日志区间。每次先check两次的区间是否有交集，如果没有进入check单一次数区间。
        如果有交集取出最小交集并存入第二个数组，如果没有交集加入加入单一次数数组。
        """
        # first check for a overlap interval in double booked
        for booking in self.double_booked:
            s, e = booking[0], booking[1]
            # 如果有交集，说明此区间已经被book了两次了
            if start < e and end > s:
                # 直接返回false
                return False
        # 如果两次book数组没有交集，开始判断一次数组
        for booking in self.single_booked:
            s, e = booking[0], booking[1]
            # 如果有交集，存入最小交集区间
            if start < e and end > s:
                self.double_booked.append((max(s, start), min(e, end)))

        # 如果都没有交集，直接存进单一book数组
        self.single_booked.append((start, end))

        return True


class MyCalendarTwo3:

    def __init__(self):
        self.calendar = SortedList()

    def book(self, start, end):
        """
        Time O(log(n) + n)
        Space O(n)
        把起始点和结束点都直接加入有序list，如果起点跟着终点，说明叠加后状态是0，如果叠加后状态等于3说明有多次book的区间，直接返回false。
        """
        # 把起点和终点直接加入有序list，并且带状态
        self.calendar.add((start, 1))
        self.calendar.add((end, -1))

        total = 0

        for i, j in self.calendar:
            # 记录当前状态
            total += j
            # 如果等于3了，说明有区间多次重复
            if total == 3:
                # 移除加入进来的区间
                self.calendar.remove((start, 1))
                self.calendar.remove((end, -1))
                return False

        return True


obj = MyCalendarTwo2()
print(obj.book(start=10, end=20))
print(obj.book(start=50, end=60))
print(obj.book(start=10, end=40))
print(obj.book(start=5, end=15))
print(obj.book(start=5, end=10))
print(obj.book(start=25, end=55))
