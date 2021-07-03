class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        """
        O(n) time, can use two pointers but may not improve efficient
        :param nums:
        :return:
        """
        result = 0
        tmp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                tmp += 1
                result = max(result, tmp)
            else:
                tmp = 0

        return result