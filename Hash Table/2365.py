from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        """
        Time O(n)
        Space O(n)
        记录下一个available的时间点是多少对于同一个task type。同时休息的时候也是算在space里面的。
        """

        next_available_day, days = {}, 0

        for t in tasks:
            # 第一个是下一个available的时间，第二个是如果不存在的话直接 +1 表示complete这个task
            days = max(next_available_day.get(t, 0), days + 1)
            # 更新下一个完成的时间点
            next_available_day[t] = days + 1 + space

        return days


s = Solution()
print(s.taskSchedulerII(tasks=[1, 2, 1, 2, 3, 1], space=3))
