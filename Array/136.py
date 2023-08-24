class Solution:
    def singleNumber(self, nums: [int]) -> int:
        """
        异或门^，任何数和自己异或都是0，任何数和0异或都是自己
        """
        single = 0
        for i in range(len(nums)):
            single ^= nums[i]

        return single
