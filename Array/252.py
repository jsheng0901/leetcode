from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        Time O(n * log(n))
        Space O(1)
        先sort一下intervals，判断是否有交集，有交集则返回false，否则继续check每一个intervals。
        """
        # 先排序一下，从小到大对于开始时间
        intervals.sort(key=lambda x: x[0])
        # check是否有交集
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True


s = Solution()
print(s.canAttendMeetings(intervals=[[0, 30], [5, 10], [15, 20]]))
