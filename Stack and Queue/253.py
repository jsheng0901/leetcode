import heapq
from typing import List


class Solution1:
    def minMeetingRooms(self, intervals: [[int]]) -> int:
        """
        Time O(n * log(n))
        Space O(n)
        先排序，然后维护一个优先列队，保证最快完成的meeting时间在列队头，如果有重复的交集的meeting，说明我们要新的room，此时把新的room
        对应的结束时间放进列队，如果没有交集说明我们可以用之前完成的room，列队头弹出表示完成meeting。
        """
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key=lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)


class Solution2:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Time O(n * log(n))
        Space O(n)
        同思路1，换一种写法。把第一个元素的添加顺序加入loop里面写
        """
        pq = []
        intervals_sorted = sorted(intervals, key=lambda x: x[0])

        for i in range(len(intervals_sorted)):
            start = intervals_sorted[i][0]
            end = intervals_sorted[i][1]
            # 如果列队存在并且开始时间大于最早结束时间，则解放一个room
            if pq and start >= pq[0]:
                heapq.heappop(pq)

            heapq.heappush(pq, end)

        return len(pq)


class Solution3:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Time O(n * log(n))
        Space O(n)
        本质上应该更快，因为只需要sort之后loop一次所有meeting。思路是，当起始时间小于结束时间时候，说明我们需要一个新的房间，当相反的时候，
        我们可以解放一个房间，同时结束时间指针向前走一步。
        """
        # 记录结果
        used_room = 0
        # 首先对结束和开始时间单独排序，贪心的思路，先完成最快结束的meeting
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)

        # 双指针遍历开始结束时间
        start_pointer = 0
        end_pointer = 0

        while start_pointer < len(intervals):
            # 如果开始时间大于结束时候，说明我们可以解放一个room，及used room -1，同时下一步结束时间meeting
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                used_room -= 1
                end_pointer += 1
            # 开始时间小于结束时间，此时我们需要新的room，同时开始时间前进一步
            used_room += 1
            start_pointer += 1

        return used_room


s = Solution2()
print(s.minMeetingRooms(intervals=[[0, 30], [5, 10], [15, 20]]))
