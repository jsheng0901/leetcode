class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        """快慢指针，快一步一步走，慢走到slow-2相等的时候则停止，直到fast找到一个不相等的，swap交换后，slow继续走"""
        slow = 0
        k = 2

        for fast in range(len(nums)):
            if slow < k or nums[fast] != nums[slow - k]:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

        return slow
