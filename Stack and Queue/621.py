from collections import Counter
import heapq
from typing import List


class Solution1:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Time O(n * log(n))
        Space O(n * log(n)) -> O(1) 因为最多就26个字母
        此题有一定的数学知识包含，从贪心的角度来说，把频率最高的拍好后，每个频率最高的间隔是n时间，然后从高频到低频一次插入进空隙。
        直到全部插入结束，此时最终的完成时间为原本的task的数量 + idle的休息时间。这里用优先列队大顶堆实现从高到低频率遍历task。
        """
        # 统计所有频率
        freq = Counter(tasks)
        pq = []
        # 放进大顶堆
        for k, v in freq.items():
            heapq.heappush(pq, -v)

        # 最高频率
        freq_max = -heapq.heappop(pq)
        # 最高的休息时间
        idle_time = (freq_max - 1) * n

        # 依次遍历所有task
        while pq and idle_time > 0:
            # 休息时间会被其它task填充导致减少，减少的休息时间有两种情况
            # 1. 本身空闲的时间大于此时task的频率，此时减少的是task的频率及所有空隙都可以插入一个task
            # 2. 本身空闲的时间小于此时task的频率，此时最多每个freq_max的空隙插入一个task，所以此时是 freq_max - 1
            idle_time -= min(-heapq.heappop(pq), freq_max - 1)
        # 最后需要注意的是空闲时间要大于等于0
        idle_time = max(0, idle_time)
        # 返回最终总时间
        return len(tasks) + idle_time


class Solution2:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Time O(n)
        Space O(1)
        逻辑一模一样同上，区别在于用数组来存储所有task的频率，并且直接sort，此时可以降低时间复杂度到O(n)。
        """
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1

        frequencies.sort()

        # max frequency
        f_max = frequencies.pop()
        idle_time = (f_max - 1) * n

        while frequencies and idle_time > 0:
            idle_time -= min(f_max - 1, frequencies.pop())
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)


s = Solution2()
print(s.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2))
