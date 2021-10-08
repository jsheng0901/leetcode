class Solution:
    def summaryRanges(self, nums: [int]) -> [str]:
        """双指针，找连续的子序列，找到不是连续的时候，加入result，然后慢指针调到快指针位置继续找"""
        if len(nums) == 0:
            return []

        slow = 0

        result = []

        for fast in range(1, len(nums)):
            if nums[fast] - nums[fast - 1] == 1:
                continue
            else:
                if fast - slow == 1:
                    result.append(str(nums[slow]))
                else:
                    result.append(str(nums[slow]) + '->' + str(nums[fast - 1]))
                slow = fast

        if slow == len(nums) - 1:
            result.append(str(nums[slow]))
        else:
            result.append(str(nums[slow]) + '->' + str(nums[-1]))

        return result