from typing import List


class Solution1:
    def dp(self, jobDifficulty, index, d, memo):
        # 特殊情况，划分完了但是时间没结束，返回最大值
        if index >= len(jobDifficulty):
            return float('inf')

        # 最后一天
        if d == 1:
            # 取最后一个划分的最大值
            difficulty = max(jobDifficulty[index:])
            return difficulty

        # 备忘录里面出现过，直接返回
        if memo[index][d] != -1:
            return memo[index][d]

        # 记录当前节点返回的最小情况
        min_difficulty = float('inf')
        # 记录当前划分组的最大值
        cur_difficulty = 0
        for i in range(index, len(jobDifficulty)):
            # 用一个指针一直更新最大值，快速找到当前划分数组的最大值
            cur_difficulty = max(cur_difficulty, jobDifficulty[i])
            # 子结果最小值
            next_difficulty = self.dp(jobDifficulty, i + 1, d - 1, memo)
            # 当前总和最小值
            min_difficulty = min(min_difficulty, cur_difficulty + next_difficulty)

        # 更新进备忘录
        memo[index][d] = min_difficulty

        return min_difficulty

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """
        Time O(n * n * d)
        Space O(n * d)
        此题可以简单的转化成，把一个数组划分成d组，每组必须是连续的subarray，每一组取最大值，然后找到所有可以的划分组合中每组的总和最小的值。
        用DP带备忘录，记录所有状态，详细见注释。
        """
        # 构建备忘录
        memo = [[-1] * (d + 1) for _ in range(len(jobDifficulty))]

        min_difficulty_job_schedule = self.dp(jobDifficulty, 0, d, memo)
        # 特殊情况，返回-1
        return -1 if min_difficulty_job_schedule == float('inf') else min_difficulty_job_schedule


class Solution2:
    def dp(self, jobDifficulty, index, d, memo, max_job_remaining):
        if index >= len(jobDifficulty):
            return float('inf')

        if d == 1:
            # 直接获取最大值，这里是最重要的区别对比思路1，可以加速找到最大值
            difficulty = max_job_remaining[index]
            return difficulty

        if memo[index][d] != -1:
            return memo[index][d]

        min_difficulty = float('inf')
        cur_difficulty = 0
        for i in range(index, len(jobDifficulty)):
            cur_difficulty = max(cur_difficulty, jobDifficulty[i])
            next_difficulty = self.dp(jobDifficulty, i + 1, d - 1, memo, max_job_remaining)
            min_difficulty = min(min_difficulty, cur_difficulty + next_difficulty)

        memo[index][d] = min_difficulty

        return min_difficulty

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """
        Time O(n * n * d)
        Space O(n * d)
        同思路1，但是用一个数组提前记录所有最大值的情况，加速找最大值。
        """
        n = len(jobDifficulty)
        # 计算每一组的最大值的结果，方便后续直接O(1)的速度拿最大值，不需要重复遍历数组
        max_job_remaining = jobDifficulty[:]
        for i in range(n - 2, -1, -1):
            max_job_remaining[i] = max(max_job_remaining[i], max_job_remaining[i + 1])

        memo = [[-1] * (d + 1) for _ in range(len(jobDifficulty))]

        min_difficulty_job_schedule = self.dp(jobDifficulty, 0, d, memo, max_job_remaining)

        return -1 if min_difficulty_job_schedule == float('inf') else min_difficulty_job_schedule


class Solution3:
    def minDifficulty(self, jobDifficulty, d):
        """
        Time O(n * d)
        Space O(n)
        单调栈的思路，找到下一个更大的数，保证栈内是单调递减的栈。
        详细见解析 https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/description/
        """
        n = len(jobDifficulty)
        if n < d:
            return -1

        # min_diff_curr_day and min_diff_prev_day record the minimum total job difficulty
        # for the current day and previous day, respectively
        min_diff_prev_day, min_diff_curr_day = [float('inf')] * n, [float('inf')] * n

        for day in range(d):
            # Use a monotonically decreasing stack to record job difficulties
            stack = []

            # The number of jobs needs to be no less than number of days passed.
            for i in range(day, n):

                # We initialize min_diff_curr_day[i] as only performing 1 job at the i-th index.
                # At day 0, the minimum total job difficulty is to complete the 0th job only.
                if i == 0:
                    min_diff_curr_day[i] = jobDifficulty[0]
                # Otherwise, we increment min_diff_prev_day[i - 1] by the i-th job difficulty
                else:
                    min_diff_curr_day[i] = min_diff_prev_day[i - 1] + jobDifficulty[i]

                # When we find the last element in the stack is smaller than or equal to current job,
                # we need to pop out the element to maintain a monotonic decreasing stack.
                while stack and jobDifficulty[stack[-1]] <= jobDifficulty[i]:

                    # If we include all jobs with index j+1 to i to the current day,
                    # total job difficulty of the current day will be increased.
                    # by the amount of jobDifficulty[i] - jobDifficulty[j]
                    j = stack.pop()
                    diff_incr = jobDifficulty[i] - jobDifficulty[j]
                    min_diff_curr_day[i] = min(min_diff_curr_day[i], min_diff_curr_day[j] + diff_incr)

                # When the last element in the stack is larger than current element,
                # If we include all jobs with index j+1 to i to the current day,
                # the overall job difficulty will not change.
                if stack:
                    min_diff_curr_day[i] = min(min_diff_curr_day[i], min_diff_curr_day[stack[-1]])

                # Update the monotonic stack by adding in the current index
                stack.append(i)

            min_diff_prev_day, min_diff_curr_day = min_diff_curr_day, min_diff_prev_day

        return min_diff_prev_day[-1]


s = Solution3()
print(s.minDifficulty(jobDifficulty=[11, 111, 22, 222, 33, 333, 44, 444], d=6))
print(s.minDifficulty(jobDifficulty=[6, 5, 4, 3, 2, 1], d=2))
print(s.minDifficulty(jobDifficulty=[9, 9, 9], d=4))
print(s.minDifficulty(jobDifficulty=[1, 1, 1], d=3))
