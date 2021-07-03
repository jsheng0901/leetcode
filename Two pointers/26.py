class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        """
        双指针的应用，当遇到相等的时候，fast向前走，遇到不相等的时候，慢指针网跳一个并swap
        :param nums:
        :return:
        """
        slow = 0

        for fast in range(1, len(nums)):
            if nums[fast] == nums[slow]:
                continue
            else:
                slow += 1
                nums[slow], nums[fast] = nums[fast], nums[slow]

        return slow + 1  # return长度所以index上+1
