from typing import List


class Solution1:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        Time O(n)
        Space O(n)
        每次记录前缀和，check pre_sum - goal 是否出现过，如果出现过，意味着之前有前缀和等于rest，
        因为pre_sum1 - pre_sum2 = goal 及为我们要找的区间subarray。同560思路一模一样，只需要把code里面的k换成goal即可。
        """
        # 同560一模一样
        count = 0
        pre_sum = 0
        pre_sum_to_freq = {0: 1}

        for i in nums:
            pre_sum += i
            if pre_sum - goal in pre_sum_to_freq:
                count += pre_sum_to_freq[pre_sum - goal]

            if pre_sum in pre_sum_to_freq:
                pre_sum_to_freq[pre_sum] += 1
            else:
                pre_sum_to_freq[pre_sum] = 1

        return count


class Solution2:
    def sliding_window_at_most(self, nums, goal):
        # 滑动窗口模版
        left = 0
        right = 0
        window = 0
        count = 0

        while right < len(nums):
            d = nums[right]
            window += d
            right += 1
            # 当窗口总和大于goal的时候收缩
            while left < right and window > goal:
                d = nums[left]
                window -= d
                left += 1

            # 这里直接记录了当前合理subarray里面所有小于等于goal的情况的个数
            count += right - left + 1

        return count

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        Time O(2n)
        Space O(1)
        滑动窗口计算subarray总和最多是goal的次数 - subarray总和最多是goal - 1的次数，刚好等于subarray总和等于goal的次数。
        需要两次滑动窗口遍历。
        """
        # subarray总和最多是goal的次数
        at_most_goal = self.sliding_window_at_most(nums, goal)
        # subarray总和最多是goal - 1的次数
        at_most_goal_minus_1 = self.sliding_window_at_most(nums, goal - 1)

        # 相减得到结果
        return at_most_goal - at_most_goal_minus_1


class Solution3:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        Time O(n)
        Space O(1)
        还是滑动窗口，其实我们每次找到合理的subarray后，有多少个等于goal的个数在这个subarray里面，为 1 + prefix_zeros，
        也就是第一个1前面有多少个0的个数。
        """
        left = 0
        right = 0
        # 计算有多少个0
        prefix_zero = 0
        window = 0
        count = 0

        while right < len(nums):
            d = nums[right]
            window += d
            # 如果subarray总和大于goal或者第一个是0的时候
            while left < right and (nums[left] == 0 or window > goal):
                d = nums[left]
                # 记录前缀是0的个数，如果遇到1，说明前缀直接初始化
                if d == 1:
                    prefix_zero = 0
                else:
                    prefix_zero += 1

                window -= d
                left += 1

            # 当等于goal的时候，计算有多少个subarray
            if window == goal:
                count += 1 + prefix_zero

            right += 1

        return count


s = Solution3()
print(s.numSubarraysWithSum(nums=[1, 0, 1, 0, 1], goal=2))
print(s.numSubarraysWithSum(nums=[0, 0, 0, 0, 0], goal=0))
