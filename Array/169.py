class Solution:
    def majorityElement(self, nums: [int]) -> int:
        """majority vote算法"""
        count = 1
        majority = nums[0]

        for i in nums[1:]:
            if count == 0:
                majority = i

            if i == majority:
                count += 1
            else:
                count -= 1

        return majority