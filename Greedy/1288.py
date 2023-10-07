from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """
        Time O(n + log(n))
        Space O(n)
        本质上是先merge可以重叠的区间，然后最后算重合之后的长度。先sort一下按照第一个元素，然后找到每次是否需要merge的区间条件，
        同时维护一个merge后的区间，加入进result数组，下一个区间永远和上一个merge过后的或者不需要merge的区间比较，及result里面最后一个元素。
        """
        # sort区间按照第一个元素，升序
        intervals.sort(key=lambda x: x[0])
        # 初始化加入第一个元素
        result = [intervals[0]]

        # 开始遍历
        for i in range(1, len(intervals)):
            # 需要merge，并且数组最后一个大于当前区间，ex: [1, 5]和[2, 3]，当前区间被并入数组最后一个区间，数组不需要变化
            if result[-1][1] >= intervals[i][1] and result[-1][0] <= intervals[i][0]:
                continue
            # 需要merge，并且数组最后一个小于当前区间，ex: [1, 3]和[1, 5] -> [1, 5]，此时更新数组最后一个区间最右端即可
            elif result[-1][1] <= intervals[i][1] and result[-1][0] == intervals[i][0]:
                result[-1][1] = intervals[i][1]
            # 不需要merge，直接加入区间进数组
            else:
                result.append(intervals[i])

        # 最终数组长度及merge需要整合的区间后的结果
        return len(result)


s = Solution()
print(s.removeCoveredIntervals(intervals=[[1, 4], [3, 6], [2, 8]]))
print(s.removeCoveredIntervals(intervals=[[1, 2], [1, 4], [3, 4]]))
print(s.removeCoveredIntervals(
    intervals=[[66672, 75156], [59890, 65654], [92950, 95965], [9103, 31953], [54869, 69855], [33272, 92693],
               [52631, 65356], [43332, 89722], [4218, 57729], [20993, 92876]]))
