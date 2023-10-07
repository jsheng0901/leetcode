from typing import List


class Solution1:
    def merge(self, intervals: [[int]]) -> [[int]]:
        """
        Time O(n + log(n))
        Space: O(n)
        那么我按照左边界排序，排序之后局部最优：每次合并都取最大的右边界，这样就可以合并更多的区间了，整体最优：合并所有重叠的区间。
        """
        if len(intervals) == 0:
            return 0

        # 先排序，按照第一个大小排序，然后从左向右遍历, 更新右边界
        intervals.sort(key=lambda x: x[0])

        flag = False  # 标记最后一个区间有没有合并
        result = []
        i = 1  # python 要设置起始点，并用while loop，不然没办法更新i的值，用for loop只会 1,2,3,4往前走

        while i < len(intervals):
            start = intervals[i - 1][0]  # 初始为i - 1 区间的左边界
            end = intervals[i - 1][1]  # 初始i - 1 区间的右边界
            while i < len(intervals) and intervals[i][0] <= end:  # 合并区间
                end = max(end, intervals[i][1])  # 不断更新右区间
                if i == len(intervals) - 1:
                    flag = True  # 最后一个区间也合并了
                i += 1  # 继续合并下一个区间
            i += 1

            # start和end是表示intervals[i - 1] 的左边界右边界，所以最优intervals[i] 区间是否合并了要标记一下
            result.append([start, end])

        # 如果最后一个区间没有合并，将其加入result
        if not flag:
            result.append([intervals[len(intervals) - 1][0], intervals[len(intervals) - 1][1]])

        return result


class Solution2:
    def merge(self, intervals: [[int]]) -> [[int]]:
        """
        Time O(n + log(n))
        Space: O(n)
        那么我按照左边界排序，排序之后局部最优：每次合并都取最大的右边界，这样就可以合并更多的区间了，整体最优：合并所有重叠的区间。
        """
        if len(intervals) == 0:
            return 0

        # 先排序，按照第一个大小排序，然后从左向右遍历, 更新右边界
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]  # 写法更简洁，每次更新result里面的最右边的节点就行，不用while loop

        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])

        return result


class Solution3:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Time O(n + log(n))
        Space: O(n)
        逻辑同解法2
        """

        intervals.sort(key=lambda x: x[0])
        #  写法思路和第二种一样，只是这里要一直维护一个最右端的指针
        right = intervals[0][1]
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= right:
                # 更新最右端指针
                right = max(intervals[i][1], right)
                result[-1][1] = right
            else:
                result.append(intervals[i])
                # 更新最右端指针
                right = result[-1][1]

        return result


s = Solution3()
print(s.merge(intervals=[[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]]))
