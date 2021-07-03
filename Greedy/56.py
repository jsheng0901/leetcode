class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        """
        那么我按照左边界排序，排序之后局部最优：每次合并都取最大的右边界，这样就可以合并更多的区间了，整体最优：合并所有重叠的区间。
        :param intervals:
        :return:
        """
        if len(intervals) == 0:
            return 0

        # 先排序，按照第一个大小排序，然后从左向右遍历, 更新右边界
        intervals.sort(key=lambda x: x[0])

        flag = False  # 标记最后一个区间有没有合并
        result = []
        i = 1         # python 要设置其实点，并用while loop，不然没办法更新i的值用for loop只会 1,2,3,4往前走

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
        time： O（nlogn), space: O(1)
        那么我按照左边界排序，排序之后局部最优：每次合并都取最大的右边界，这样就可以合并更多的区间了，整体最优：合并所有重叠的区间。
        :param intervals:
        :return:
        """
        if len(intervals) == 0:
            return 0

        # 先排序，按照第一个大小排序，然后从左向右遍历, 更新右边界
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]             # 次写法更简洁，每次更新result里面的最右边的节点就行，不用while loop

        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])

        return result


s = Solution2()
print(s.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
