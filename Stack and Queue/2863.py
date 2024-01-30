from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        利用栈来存储单调递增，从栈头到栈底。这些index对应的数字才是可能实现最长距离的index，因为如果中间右更小的在站内，那么最长距离
        一定就会是更小的那个index对应的数字。详细见注释
        """
        stack = []
        n = len(nums)
        # 单调递增栈，从后向前
        for i in range(n - 1, -1, -1):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        # 记录最长距离
        max_length = 0
        # 记录当前最大值
        cur_min = float('-inf')

        for i in range(n):
            # 如果当前栈顶的index小于当前index，说明subarray不存储在，直接弹出栈顶
            while stack and stack[-1] <= i:
                stack.pop()
            # 如果当前数字大于当前最大值才说明会有更长的subarray，如果小于此时一定不会比之前的最大值对应找到的更长
            if nums[i] > cur_min:
                # 更新当前最大值
                cur_min = nums[i]
                # 开始尝试所有可能构成的单调栈里面index，同时更新最长距离
                while stack and nums[stack[-1]] < cur_min:
                    max_length = max(max_length, stack[-1] - i + 1)
                    stack.pop()

        return max_length


s = Solution()
print(s.maxSubarrayLength(nums=[57, 55, 50, 60, 61, 58, 63, 59, 64, 60, 63]))
