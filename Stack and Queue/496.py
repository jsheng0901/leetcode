class Solution:
    def nextGreaterElement(self, nums1: [int], nums2: [int]) -> [int]:
        """
        O(n) time, O(n) space
        单调递增(stack top -> stack bottom)栈, 当当前数字大于栈顶数字的时候，判断栈顶数字是否是nums1里面的数字，如果是
        则说明找到了第一个比它大的数字，此时找到nums1的index并且记录当前数字到这个index去，弹出栈顶数字，继续loop nums2
        """
        result = [-1] * len(nums1)
        hash_map = {}
        for i, v in enumerate(nums1):
            hash_map[v] = i

        stack = [0]
        for i in range(1, len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                if nums2[stack[-1]] in hash_map:
                    idx = hash_map[nums2[stack[-1]]]
                    result[idx] = nums2[i]
                stack.pop()

            stack.append(i)

        return result


s = Solution()
print(s.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
