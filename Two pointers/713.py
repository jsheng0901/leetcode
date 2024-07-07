from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        Time O(n)
        Space O(1)
        持续记录窗口内的乘积，因为都是保证为正数所以窗口内的乘积一定是递增的。所以如果大于等于k说明需要开始收缩窗口。
        最后在最后一步判断满足情况的条件，叠加subarray个数。
        """
        # 记录窗口内的乘积
        window = 1
        count = 0

        left = 0
        right = 0

        while right < len(nums):
            # 进入窗口的字符
            d = nums[right]
            right += 1
            # 更新窗口
            window *= d

            # 如果左指针小于右指针并且窗口内乘积大于等于k，说明可以开始收缩，这里一定要判断左指针的位置先，不然会出现一直为1的情况，
            # 左指针会一直递增则超过右指针。
            while left < right and window >= k:
                c = nums[left]
                left += 1
                # 更新窗口，用取乘数的方式，因为前面连成过所以一定可以整除
                window //= c

            # 计算subarray的个数
            if window < k:
                count += right - left

        return count


s = Solution()
print(s.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
print(s.numSubarrayProductLessThanK(nums=[1, 2, 3, 4, 5], k=1))
print(s.numSubarrayProductLessThanK(nums=[1, 2, 3], k=0))
