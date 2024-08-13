class RangeModule1:

    def __init__(self):
        """
        Space O(n)
        """
        self.ranges = []

    def binary_search_right_bound(self, start):
        # 标准二分法查找右边界的写法
        left = 0
        right = len(self.ranges) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if self.ranges[mid][0] < start:
                left = mid + 1
            # 核心不一样的地方在这里，因为是右边界，等于的时候我们移动左指针
            elif self.ranges[mid][0] == start:
                left = mid + 1
            elif self.ranges[mid][0] > start:
                right = mid - 1

        # 出循环的时候是 right < left + 1
        # 此时右指针是边界，左指针是第一个比target大的index，我们需要左指针的结果
        return left

    def merge(self, intervals: [[int]]) -> [[int]]:
        # 合并区间的标准写法
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])

        return result

    def addRange(self, left: int, right: int) -> None:
        """
        Time O(log(n) + n)  n -> number of element in ranges
        Space O(n)
        二分法找到第一个大于target值的index，然后insert进去后，进行区间合并。
        """
        # 找到右边界index
        right_bound = self.binary_search_right_bound(left)
        # insert进去
        self.ranges.insert(right_bound, [left, right])

        # 合并区间
        self.ranges = self.merge(self.ranges)

    def queryRange(self, left: int, right: int) -> bool:
        """
        Time O(log(n))  n -> number of element in ranges
        Space O(n)
        同理找到右边界，如果query的区间在我们边界的区间内，那么和边界前一个区间一定会有交集，并且是完全覆盖的交集。
        """
        # 特殊情况，还没有加入任何区间
        if len(self.ranges) == 0:
            return False
        # 找到右边界
        right_bound = self.binary_search_right_bound(left)

        # 上下界限
        lower = self.ranges[right_bound - 1][0]
        upper = self.ranges[right_bound - 1][1]

        # 必须是完全覆盖的交集
        return lower <= left and right <= upper

    def removeRange(self, left: int, right: int) -> None:
        """
        Time O(log(n) + n)  n -> number of element in ranges
        Space O(n)
        移除区间的特殊情况最多，找到边界后，当前右边界和前一个区间有两种情况，第一种有交集，那么我们需要对前一个区间进行去除交集，并且重组
        range的时候需要考虑到插入的位置。第二种情况，没有交集，那么插入的位置就是右边界的位置。详细见注释。
        """
        # 下限边界
        lower_bound = self.binary_search_right_bound(left)
        # 上线边界
        upper_bound = self.binary_search_right_bound(right)

        merge = []
        # 对有交集的区间进行合并区间，注意这里初始index是下限的前一个区间
        for k in range(max(lower_bound - 1, 0), upper_bound):
            # 如果和前一个区间没有任何交集
            if left >= self.ranges[k][1] or right <= self.ranges[k][0]:
                # 需要记录进这个区间，方便后续合并
                merge.append(self.ranges[k])
                # 跳过这个区间，否则有可能出现[6, 7]区间去除[8, 9]的时候，[8, 9]被记录进merge区间
                continue
            # 如果左边和区间有交集
            if self.ranges[k][0] < left:
                merge.append([self.ranges[k][0], left])
            # 如果右边和区间有交集
            if right < self.ranges[k][1]:
                merge.append([right, self.ranges[k][1]])
        # 最后合并的时候，一定要提取找到边界的前一个区间 + merge区间 + 上线边界后的区间
        self.ranges = self.ranges[:max(lower_bound - 1, 0)] + merge + self.ranges[upper_bound:]


# 线段树的节点类
class TreeNode:
    def __init__(self, left=-1, right=-1, val=0, lazy_tag=None, left_node=None, right_node=None):
        self.left = left  # 区间左边界
        self.right = right  # 区间右边界
        self.mid = left + (right - left) // 2  # 区间中间点
        self.left_node = left_node  # 区间左节点
        self.right_node = right_node  # 区间右节点
        self.val = val  # 节点值（区间值）
        self.lazy_tag = lazy_tag  # 区间问题的延迟更新标记


# 动态开点线段树类，带延迟更新标记的版本
class SegmentTree:
    # 初始化线段树接口
    def __init__(self, function):
        self.tree = TreeNode(0, int(1e9))
        self.function = function  # function 是一个函数，左右区间的聚合方法

    def __push_up(self, node):
        if node.left_node and node.right_node:
            node.val = node.left_node.val and node.right_node.val
        else:
            node.val = False

    # 向下更新 node 节点所在区间的左右子节点的值和懒惰标记
    def __push_down(self, node):
        if not node.left_node:
            node.left_node = TreeNode(node.left, node.mid)
        if not node.right_node:
            node.right_node = TreeNode(node.mid + 1, node.right)
        if node.lazy_tag is not None:
            node.left_node.lazy_tag = node.lazy_tag  # 更新左子节点懒惰标记
            node.left_node.val = node.lazy_tag  # 左子节点每个元素值增加 lazy_tag

            node.right_node.lazy_tag = node.lazy_tag  # 更新右子节点懒惰标记
            node.right_node.val = node.lazy_tag  # 右子节点每个元素值增加 lazy_tag

            node.lazy_tag = None  # 更新当前节点的懒惰标记

    # 区间更新，将区间为 [q_left, q_right] 上的元素值修改为 val
    def update_interval(self, q_left, q_right, val):
        self.__update_interval(q_left, q_right, val, self.tree)

    # 区间更新
    def __update_interval(self, q_left, q_right, val, node):
        if q_left <= node.left and node.right <= q_right:  # 节点所在区间被 [q_left, q_right] 所覆盖
            node.lazy_tag = val  # 将当前节点的延迟标记增加 val
            node.val = val  # 当前节点所在区间每个元素值增加 val
            return

        self.__push_down(node)

        if q_left <= node.mid:
            self.__update_interval(q_left, q_right, val, node.left_node)
        if q_right > node.mid:
            self.__update_interval(q_left, q_right, val, node.right_node)

        self.__push_up(node)

    # 区间查询，查询区间为 [q_left, q_right] 的区间值
    def query_interval(self, q_left, q_right):
        return self.__query_interval(q_left, q_right, self.tree)

    # 区间查询，在线段树的 [left, right] 区间范围中搜索区间为 [q_left, q_right] 的区间值
    def __query_interval(self, q_left, q_right, node):
        if q_left <= node.left and node.right <= q_right:  # 节点所在区间被 [q_left, q_right] 所覆盖
            return node.val  # 直接返回节点值

        # 需要向下更新节点所在区间的左右子节点的值和懒惰标记
        self.__push_down(node)

        if q_right <= node.mid:
            return self.__query_interval(q_left, q_right, node.left_node)
        if q_left > node.mid:
            return self.__query_interval(q_left, q_right, node.right_node)

        res_left = self.__query_interval(q_left, q_right, node.left_node)
        res_right = self.__query_interval(q_left, q_right, node.right_node)

        return res_left and res_right  # 返回左右子树元素值的聚合计算结果


class RangeModule2:
    def __init__(self):
        """
        Space O(n)
        存储的是所有区间的线段进线段树，此题用动态开点线段树，聚合函数思路是两个区间都必须满足一样的逻辑，True and True。
        另外注意此题要求是半开区间 [left, right) ，而线段树中常用的是闭合区间。
        但是我们可以将半开区间 [left, right) 转为 [left, right - 1] 的闭合空间。
        """
        self.ranges = SegmentTree(lambda x, y: x and y)

    def addRange(self, left: int, right: int) -> None:
        """
        Time O(log(n))
        添加的区间都标记为True
        """
        self.ranges.update_interval(left, right - 1, True)

    def queryRange(self, left: int, right: int) -> bool:
        """
        Time O(log(n))
        query的区间必须满足都是True才会返回True
        """
        return self.ranges.query_interval(left, right - 1)

    def removeRange(self, left: int, right: int) -> None:
        """
        Time O(log(n))
        移除的区间都标记为False
        """
        self.ranges.update_interval(left, right - 1, False)


obj = RangeModule2()
obj.addRange(left=6, right=8)
obj.removeRange(left=7, right=8)
obj.removeRange(left=8, right=9)
obj.addRange(left=8, right=9)
obj.removeRange(left=1, right=3)
obj.addRange(left=1, right=8)
print(obj.queryRange(left=2, right=4))
print(obj.queryRange(left=2, right=9))
print(obj.queryRange(left=4, right=6))
