
class Solution1:
    def search_insert(self, nums: [int], target: int) -> int:
        """
        Time O(n) loop nums once
        Space O(1)
        """
        for i in range(len(nums)):
            if nums[i] >= target:
                return i

        return len(nums)


class Solution2:
    def search_insert(self, nums: [int], target: int) -> int:
        """
        Time O(logn) binary search time
        Space O(1)
        """
        left = 0
        right = len(nums) - 1   # 定义target在左闭右闭的区间里，[left, right]
        while left <= right:    # when left equal right, target value can same as middle
            middle = left + (right - left) // 2
            if nums[middle] < target:   # target on right side
                left = middle + 1
            elif nums[middle] > target:     # target on left side, right as middle - 1 because 区间是可以两边取到的
                right = middle - 1
            else:
                return middle

        return right + 1    # or just return left


s = Solution2()
print(s.search_insert([1, 2, 3, 4], 5))
