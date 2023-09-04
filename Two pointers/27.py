class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        """
        Time O(n)
        Space O(1)
        当慢指针和快指针指向同一个不等于value的元素时候，一起向前进一步，
        当快指针指向等于value的元素时候，慢指针不动，快指针继续，直到找到下一个不一样的，然后与慢指针相互交换位置，同时慢指针向前走一步
        """
        slow_index = 0
        for fast_index in range(len(nums)):
            if nums[fast_index] != val:
                nums[slow_index], nums[fast_index] = nums[fast_index], nums[slow_index]
                slow_index += 1

        return slow_index


s = Solution()
print(s.removeElement([1, 2, 3, 4, 5, 3, 3], 5))
