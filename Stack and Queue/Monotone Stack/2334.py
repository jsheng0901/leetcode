from typing import List


class Solution:
    def get_next_smaller_index(self, nums):
        # 单调递增栈找下一个更小的数模版，如果没有则为本身index
        res = [i for i in range(len(nums))]
        stack = []

        for i, val in enumerate(nums):
            # 遇到当前数小于栈顶数的时候，找到下一个更小的数的index
            while stack and nums[stack[-1]] > val:
                # 记录进数组
                res[stack.pop()] = i
            # 当前数index入栈
            stack.append(i)

        return res

    def get_previous_smaller_index(self, nums):
        # 单调递增栈找前一个更小的数，同下一个更小的数，只是反过来遍历
        res = [i for i in range(len(nums))]
        stack = []

        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                res[stack.pop()] = i
            stack.append(i)

        return res

    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        """
        Time O(n)
        Space O(n)
        单调栈的运用，换个角度思考，如果我们知道一个subarray里面最小的数满足题目条件的话，那么这个subarray里面所有的数都会满足要求。所以
        我们需要的是知道每个数作为subarray里面最小的数的时候，最长的的subarray是什么，也就是需要知道左右boundary。单调栈找下一个更小的数，
        同理反过来单调栈找前一个更小的数。然后找到最长合理subarray区间，计算是否满足条件，满足返回结果，不满足继续遍历，如果都没有，返回 -1。
        """
        # 每一个数的下一个更小的数，如果不存在则为自己本身的index
        next_smaller_index = self.get_next_smaller_index(nums)
        # 前一个更小的数
        previous_smaller_index = self.get_previous_smaller_index(nums)

        for i in range(len(nums)):
            # 注意这里特殊情况，如果下一个是自己本身，说明后面所有数都比它大，则说明右端点可以到最后
            next_index = len(nums) if next_smaller_index[i] == i else next_smaller_index[i]
            # 同上，注意这里特殊情况，如果前一个是自己本身，说明前面所有数都比它大，则说明左端点可以到最开始
            previous_index = -1 if previous_smaller_index[i] == i else previous_smaller_index[i]
            # 计算subarray长度
            length = next_index - previous_index - 1
            # 判断是否符合要求
            if nums[i] > threshold // length:
                return length

        return -1


s = Solution()
print(s.validSubarraySize(nums=[6, 5, 6, 5, 8], threshold=7))
print(s.validSubarraySize(nums=[1, 3, 4, 3, 1], threshold=6))
