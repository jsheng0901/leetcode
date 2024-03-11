from typing import List


class Solution1:
    def missingElement(self, nums: List[int], k: int) -> int:
        """
        Time O(n)
        Space O(1)
        找每个数直接的gap个数，如果小于k，就继续向前走，同时更新还剩下多少k。
        """
        n = len(nums)

        for i in range(1, n):
            missed_in_gap = nums[i] - nums[i - 1] - 1
            # 找到区间
            if missed_in_gap >= k:
                return nums[i - 1] + k
            # 更新k
            k -= missed_in_gap

        # 在最右边
        return nums[-1] + k


class Solution2:
    def missingElement(self, nums: List[int], k: int) -> int:
        """
        Time O(log(n))
        Space O(1)
        所有二分发一定要找到要对比中间点和target值的equation。这里我们找的是中间点到起始点缺失的元素个数对比target值k的大小。
        nums[mid] - nums[0] + 1 表示从起始点到当前中间点应该有多少个元素如果没有缺失，mid + 1 表示实际有多少个元素。相减就是缺失的个数。
        如果缺失的大于k，那说明结果在中间点的左边，如果小于k说明结果在右边，如果等于k，说明结果在左边，
        最终我们需要找到的index表示，nums[index]到起始点的缺失值大于k，nums[index + 1]到起始点的缺失值小于k，也就是说最终答案在
        nums[index] - nums[index + 1] 中间。我们可以构建方程 answer - nums[0] + 1 表示从answer到起始点应该有多少个数，
        index + 1 + k 表示同样 index + 1表示有多少个数在nums里面，+ k表示到answer总共多少个数。
        则有 answer - nums[0] + 1 = index + 1 + k，answer = nums[0] + index + k。
        之后就是找index。这里采用找左边界的二分法写法，区别在于我们要找的是左边界左边的第一个数，而不是左边界本身，
        所以 return 是 right 不是 left，因为出循环是left = right + 1，这里right是上面的index，left是index + 1
        """
        left = 0
        right = len(nums) - 1
        # 找左边界写法
        while left <= right:
            mid = left + (right - left) // 2
            # 计算从起始点到中间点的缺失数有多少
            gap = (nums[mid] - nums[0] + 1) - (mid + 1)
            if gap > k:
                right = mid - 1
            elif gap < k:
                left = mid + 1
            else:
                right = mid - 1

        # 这里出循环后用的是右指针，而不是左指针，表示的是小于左边界的第一个数
        return nums[0] + right + k


s = Solution2()
print(s.missingElement(nums=[4, 7, 9, 10], k=1))
print(s.missingElement(nums=[4, 7, 9, 10], k=3))
print(s.missingElement(nums=[1, 2, 4], k=3))
