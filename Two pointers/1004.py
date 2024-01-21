from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Time O(n)
        Space O(1)
        滑动窗口，因为是找连续的1所以在窗口内的符合规则的一定是最长的。右指针一直扩大，直到0的个数超过k，此时可以缩短左指针直到0的个数从新回到
        k内，也可以保证窗口的大小，只移动一次左指针，然后继续右指针。
        """
        window = 0
        left = 0
        right = 0
        result = 0

        while right < len(nums):
            # 需要被加进来的元素
            c = nums[right]
            # 下一个右指针位置
            right += 1
            # 更新窗口内0的出现次数
            if c == 0:
                window += 1

            # 判断窗口是否需要收缩
            while window > k:
                # 需要踢出去的元素
                d = nums[left]
                # 下一个左指针位置
                left += 1
                # 更新窗口内0的出现次数
                if d == 0:
                    window -= 1
            # 更新当前最长距离，这里不用 +1，因为右指针已经往前跳了一步
            result = max(result, right - left)

        return result


s = Solution()
print(s.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
