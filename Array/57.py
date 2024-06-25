from typing import List


class Solution1:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Time O(n)
        Space O(n)
        此题最重要的是弄清楚三种情况，分别对应没有交集前，有交集的时候，和交集后。详细见注释。
        """
        n = len(intervals)
        i = 0
        res = []

        # Case 1: No overlapping before merging intervals
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Case 2: Overlapping and merging intervals
        while i < n and newInterval[1] >= intervals[i][0]:
            # 找到交集区间的起点和终点
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        # 加入交集进结果
        res.append(newInterval)

        # Case 3: No overlapping after merging newInterval
        while i < n:
            res.append(intervals[i])
            i += 1

        return res


class Solution2:
    def get_insert_index(self, intervals, newInterval):

        # 二分法标准模版找左边界，找到的index为第一个大于等于目标值的index
        left = 0
        right = len(intervals) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if intervals[mid][0] < newInterval[0]:
                left = mid + 1
            elif intervals[mid][0] == newInterval[0]:
                right = mid - 1
            elif intervals[mid][0] > newInterval[0]:
                right = mid - 1

        return left

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Time O(n + log(n))
        Space O(n)
        虽然都是一样的时间，但是实际上当数组很大的时候并且insert位置是最后或者前面的时候，二分法会更快。
        先用二分法找到需要insert的位置，插入后变成merged interval。
        """
        # 二分法找到需要插入的index，因为插入是向插入左边的index，所以刚好是二分法找到左边界的位置
        insert_index = self.get_insert_index(intervals, newInterval)
        # 插入到此位置
        intervals.insert(insert_index, newInterval)

        # 开始合并整个interval，同56题写法，一直维护一个最右值
        res = []
        for interval in intervals:
            # 如果是空结果，或者没有交集
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            # 有交集，更新最右点
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res


s = Solution2()
print(s.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
print(s.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))
