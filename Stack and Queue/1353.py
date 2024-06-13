import heapq


class Solution:
    def maxEvents(self, events: [[int]]) -> int:
        """
        Time O(n + k) n is number, k is length of events
        Space O(n)
        贪心 + 小顶堆的思路，每一次我们loop每一天，我们把等同于这一天开始的events加入小顶堆，记录结束的时间进栈，
        如果越早结束的时间，及栈顶小于当天，说明无法参加，如果大于等于当天，说明可以参加，并且弹出栈，然后继续下一天
        """
        events.sort(key=lambda x: x[0])
        heap = []
        attend = 0
        for curr_day in range(1, 100001):
            while events and events[0][0] == curr_day:  # 等于当天开始的events进入栈，进入的是结束的时间
                heapq.heappush(heap, events.pop(0)[1])

            while heap and heap[0] < curr_day:  # 如果结束的时候早于当天，则说明无法参加
                heapq.heappop(heap)

            if heap:  # 如果当天结束的时候还有时间在栈顶，说明可以参加
                heapq.heappop(heap)
                attend += 1

        return attend


s = Solution()
print(s.maxEvents(events=[[1, 2], [2, 3], [3, 4]]))
print(s.maxEvents(events=[[1, 2], [2, 3], [3, 4], [1, 2]]))
