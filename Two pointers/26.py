class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        """
        Time O(n)
        Space O(1)  in-place变化，没有额外空间开销。
        双指针的应用，当遇到相等的时候，fast向前走，遇到不相等的时候，慢指针网跳一个并swap。
        """
        slow = 0

        for fast in range(1, len(nums)):
            if nums[fast] == nums[slow]:
                continue
            else:
                slow += 1
                nums[slow], nums[fast] = nums[fast], nums[slow]

        return slow + 1  # return长度所以index上+1
