class Solution:
    def pivotIndex(self, nums: [int]) -> int:
        """
        前缀和应用，找到一个点左右和相等
        :param nums:
        :return:
        """
        total = sum(nums)

        left_sum = 0

        for i in range(len(nums)):
            if left_sum == total - nums[i] - left_sum:
                return i
            left_sum += nums[i]

        return -1
