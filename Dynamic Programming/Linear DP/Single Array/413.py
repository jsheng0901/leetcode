from typing import List


class Solution1:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        dp[i]为以i结尾的数组可以构成等差数列的个数。当前如果数和前两个数构成等差数列，那么有dp[i] = dp[i - 1] + 1。
        我们记录的是当前结尾可以构成的个数，不包括前面所有的等差数列个数。
        最终叠加每个数结尾构成的等差数列的个数为整个数组可以构成等差数列的个数。
        """
        dp = [0] * len(nums)
        res = 0

        for i in range(2, len(nums)):
            # 核心思路在这里
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                # 递推公式
                dp[i] = dp[i - 1] + 1
                res += dp[i]

        return res


class Solution2:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(1)
        一模一样的思路，只是空间优化的版本，因为我们只需要知道前面一个数结尾的状态，用指针记录前一个的状态即可。
        """
        dp = 0
        res = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                # 指针状态更新
                dp += 1
                res += dp
            else:
                # 注意这里要初始化为0，因为前一个不成立，说明状态是0
                dp = 0

        return res


s = Solution2()
print(s.numberOfArithmeticSlices(nums=[1, 2, 3, 4]))
print(s.numberOfArithmeticSlices(nums=[1, 2, 3, 8, 9, 10]))
