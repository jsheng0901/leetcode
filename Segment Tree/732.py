from sortedcontainers import SortedDict


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
            if node.left_node is None:
                node.left_node = SegTreeNode(node.left, node.mid)
            self._update_point(i, val, node.left_node)
        else:  # 在右子树中更新节点值
            if node.right_node is None:
                node.right_node = SegTreeNode(node.mid + 1, node.right)
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
            if node.left_node is None:
                node.left_node = SegTreeNode(node.left, node.mid)
            self._update_interval(q_left, q_right, val, node.left_node)
        if q_right > node.mid:  # 在右子树中更新区间值
            if node.right_node is None:
                node.right_node = SegTreeNode(node.mid + 1, node.right)
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


class MyCalendarThree1:

    def __init__(self):
        # 线段树的聚合函数选择取最大值，表示记录当前区间保存了最多多少个日程区间个数
        self.segment_tree = SegmentTree(lambda x, y: max(x, y))

    def book(self, start: int, end: int) -> int:
        """
        Time O(log(n)) -> n time book O(n * log(n))
        Space O(log(n)) -> n time book O(n * log(n))
        还是线段树的写法，和731一模一样的思路，只是这里需要最多多少个同时发生的event，我们query的时候需要query整个区间
        """
        self.segment_tree.update_interval(start, end - 1, 1)

        # query整个区间，这里是O(1)的速度，因为query根节点的时候update已经更新了整个区间节点聚合函数之后的结果
        k = self.segment_tree.query_interval(0, int(1e9))

        return k


class MyCalendarThree2:

    def __init__(self):
        self.diff = SortedDict()

    def book(self, start: int, end: int) -> int:
        """
        Time O(log(n) + n)  -> n time book O(n * (log(n) + n)) -> O(n^2)
        Space O(n)
        有序数组或者有序字典，按照key的大小进行排序，和731的思路一样，如果起始和终止同时发现那么累计就是0，同时统计最大同时起始的值。
        但是每次需要遍历整个有序字典，所以很费时。
        """
        # 累计当前时间点作为起点的次数
        self.diff[start] = self.diff.get(start, 0) + 1
        # 累计当前时间点作为终点的次数
        self.diff[end] = self.diff.get(end, 0) - 1
        cur = res = 0
        # 遍历整个有序数组
        for delta in self.diff.values():
            # 累计时间差
            cur += delta
            # 统计最多的时候有多少个同时发生的起点
            res = max(cur, res)

        return res


obj = MyCalendarThree2()
print(obj.book(start=10, end=20))
print(obj.book(start=50, end=60))
print(obj.book(start=10, end=40))
print(obj.book(start=5, end=15))
print(obj.book(start=5, end=10))
print(obj.book(start=25, end=55))


