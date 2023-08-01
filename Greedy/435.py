from typing import List


class Solution1:
    def eraseOverlapIntervals(self, intervals: [[int]]) -> int:
        """
        Time: O(nlogn)
        Space: O(1)
        按照右边界排序，从左向右记录非交叉区间的个数。最后用区间总数减去非交叉区间的个数就是需要移除的区间个数了
        右边界排序之后，局部最优：优先选右边界小的区间，所以从左向右遍历，留给下一个区间的空间大一些，
        从而尽量避免交叉。全局最优：选取最多的非交叉区间
        """
        if len(intervals) == 0:
            return 0
        # 先排序，按照第二个(右边界)大小排序，然后从左向右遍历
        intervals.sort(key=lambda x: x[1])

        count = 1  # 记录非交叉区间的个数
        end = intervals[0][1]  # 记录区间分割点

        for i in range(1, len(intervals)):
            if end <= intervals[i][0]:  # 如果上一个的右边界的点小于等于此时区间的左边界，意味着没有交叉空间此时
                end = intervals[i][1]
                count += 1

        return len(intervals) - count


class Solution2:
    def eraseOverlapIntervals(self, intervals: [[int]]) -> int:
        """
        按照右边界排序，从左向右记录非交叉区间的个数。最后用区间总数减去非交叉区间的个数就是需要移除的区间个数了
        右边界排序之后，局部最优：优先选右边界小的区间，所以从左向右遍历，留给下一个区间的空间大一些，
        从而尽量避免交叉。全局最优：选取最多的非交叉区间
        """
        if len(intervals) == 0:
            return 0
        # 先排序，按照第二个(右边界)大小排序，然后从左向右遍历
        intervals.sort(key=lambda x: x[1])

        count = 0  # 记录交叉区间的个数
        end = intervals[0][1]  # 记录区间分割点最远的点

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:  # 如果小于最远的点，则说明有交集，取最小的新的最远的点，这样可以让移除的数组尽量少一点
                count += 1
                end = min(end, intervals[i][1])
            else:
                end = intervals[i][1]

        return count


class Solution3:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        从左边界排序，和452一模一样，区别在于记录重叠区间的个数就是记录452里面需要射箭的个数
        """
        intervals.sort(key=lambda x: x[0])
        result = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:  # 存在交际，则此时需要记录
                result += 1
                intervals[i][1] = min(intervals[i][1], intervals[i - 1][1])  # 更新最小右边界

        return result


s = Solution1()
print(s.eraseOverlapIntervals(intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]))
