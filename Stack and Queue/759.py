import heapq
import operator


# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution1:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        """
        Time O(n * log(n))     --> n is the number of intervals across all employees
        Space O(n)
        先把interval所有区间转换成一个list里面，再sort每个区间的起始点，找到每个区间空白的部分即可。
        """
        work_time = []
        # 把所有时间区间变成一个list
        for i in range(len(schedule)):
            for j in range(len(schedule[i])):
                start = schedule[i][j].start
                end = schedule[i][j].end
                work_time.append([start, end])

        # sort从小到大根据start time
        work_time.sort(key=lambda x: x[0])

        # 记录当前最大的右边点
        res = []
        right_most = work_time[0][1]
        for i in range(1, len(work_time)):
            # 如果没有交集说明有空白时间
            if work_time[i][0] > right_most:
                # 注意这里要把start和end转化成题目定义的object
                free_time = Interval(right_most, work_time[i][0])
                # 加入结果
                res.append(free_time)

            # 同时更新最右边的点
            right_most = max(right_most, work_time[i][1])

        return res


class Solution2:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        """
        Time O(n * log(k))      --> k is the number of employees
        Space O(k)
        其实我们可以优化空间，和23题一样，我们其实在merge k 个有序数组。首先收集每个员工的第一个event，因为每个人是有序的，所以第一个event
        一定是每个人最早的时间，之后一直往heapq里面添加这个人下一个event，如果这个人没有下一个event，意味着这个人merge完了。同时维护最右点。
        """
        # collect first events of all employees
        heap = []
        for i, employee in enumerate(schedule):
            # (event.start, employee index, event index)
            heapq.heappush(heap, (employee[0].start, i, 0))

        res = []
        _, i, j = heap[0]
        # 第一个最早开始的event
        prev_end = schedule[i][j].end
        while heap:
            _, i, j = heapq.heappop(heap)
            # check for next employee event and push it
            # 如果这个人还有下一个event，先push进来，可能这个event比其它所有人的第一个event都早
            if j + 1 < len(schedule[i]):
                heapq.heappush(heap, (schedule[i][j + 1].start, i, j + 1))

            # 当前event
            event = schedule[i][j]
            # 同思路1，如果没有交集，说明有空白时间，加入结果
            if event.start > prev_end:
                res.append(Interval(prev_end, event.start))
            # 同时更新当前最右点
            prev_end = max(prev_end, event.end)

        return res


class Solution3:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        """
        Time O(n * log(k))      --> k is the number of employees
        Space O(k)
        同思路2，只是换成heapq.merge的写法。
        """
        iterator = heapq.merge(*schedule, key=operator.attrgetter('start'))
        res, prev_end = [], next(iterator).end
        for event in iterator:
            if event.start > prev_end:
                res.append(Interval(prev_end, event.start))
            prev_end = max(prev_end, event.end)
        return res


event1 = Interval(1, 2)
event2 = Interval(5, 6)
event3 = Interval(1, 3)
event4 = Interval(4, 10)
employee1 = [event1, event2]
employee2 = [event3]
employee3 = [event4]
s = Solution2()
print(s.employeeFreeTime(schedule=[employee1, employee2, employee3]))
