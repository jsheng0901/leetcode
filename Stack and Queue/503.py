class Solution:
    def nextGreaterElements(self, nums: [int]) -> [int]:
        """
        Time O(n)
        Space O(n)
        单调递增(stack top -> stack bottom)栈, 当当前数字大于栈顶数字的时候，判断栈顶数字是否是nums1里面的数字，如果是
        则说明找到了第一个比它大的数字，此时找到nums1的index并且记录当前数字到这个index去，弹出栈顶数字，继续loop nums2
        此题和496几乎一摸一样，不同的是需要loop两次数组，用余数来找index，比如数组长度3，i=5的时候余数是2，刚好是index=2的下标。
        """
        result = [-1] * len(nums)
        stack = []
        length = len(nums)
        for i in range(length * 2):
            while len(stack) > 0 and nums[i % length] > nums[stack[-1]]:    # 注意这里的index如何标记
                result[stack[-1]] = nums[i % length]
                stack.pop()
            stack.append(i % length)

        return result
