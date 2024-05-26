# 2024-05-01
# Amazon Care is a healthcare and well-being portal for its employees.
#
# To promote physical fitness, on the portal they launched a "GetFit" tournament consisting of n sprints. Each sprint
# lasts for a given number of days and includes several tasks such as push-ups, running, etc. Some tasks are
# scheduled for each day of the sprint. The ith sprint lasts for days[i] days, and each sprint starts just after the
# other. That is, if the sprint ends on day d, the (i + 1)th sprint starts on day (d + 1). During each sprint,
# completing the required tasks scheduled on the jth day of the sprint earns the participant j points.
#
# The tournaments are periodic, i.e., as soon as the last sprint of a tournament ends, the first sprint of the next
# tournament begins. Each tournament, however, has the same schedule of sprints. More formally, the tournament
# schedule can be considered cyclic in nature and after the last sprint, the first sprint starts again.
#
# An employee decides to participate. However, due to a tight schedule, the employee cannot complete all tasks every
# day. Instead, the employee will complete the tasks of exactly k consecutive days, hoping to achieve the maximum
# number of points.
#
# Given the sprint days of n sprints, and the number of days for which the employee competes for k, find the maximum
# points the employee can score. The training can start and end on any day of any sprint.
#
# Note:
#
# k is guaranteed to be less than the total number of days for which the sprints last.
# Also, it is not necessary to start and end the training in the same tournament.
# A sprint here denotes a set of activities performed in a particular time period
from typing import List


class Solution:
    def getMaxPointsFromSprints(self, days: List[int], k: int) -> int:
        """
        Time O(n)
        Space O(n)
        把每一天的point拉平进一个list，其实就是求滑动窗口k内最大的和。
        """
        # 把每一天的point装进一个数组
        points = []
        for day in days:
            for point in range(day):
                points.append(point + 1)

        total_days = len(points)
        cur_points = 0
        # 计算初始值前k个数的和
        for i in range(k):
            cur_points += points[i % total_days]

        max_points = cur_points
        # 开始滑动窗口，统计后面k个窗口内的和并且找到最大情况
        for i in range(1, total_days):
            # 出窗口的数
            cur_points -= points[(i - 1) % total_days]
            # 判断一下下一个进窗口的数是不是超过总长度
            if i + k - 1 < total_days:
                # 没有超出，直接加入
                cur_points += points[i + k - 1]
            else:
                # 超出，直接循环后的数
                cur_points += points[(i + k - 1) % total_days]
            # 更新最大值
            max_points = max(max_points, cur_points)

        return max_points


s = Solution()
print(s.getMaxPointsFromSprints(days=[2, 3, 2], k=4))
