from typing import List


class Solution:
    def nextGreaterElement1(self, nums1: [int], nums2: [int]) -> [int]:
        """
        Time O(n)
        Space O(n)
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

    def nextGreaterElement2(self, nums1: [int], nums2: [int]) -> [int]:
        """
        另一种写法，不需要初始化stack
        """
        result = [-1] * len(nums1)
        stack = []
        nums1_map = {}
        for i in range(len(nums1)):
            nums1_map[nums1[i]] = i

        for i in range(len(nums2)):
            while len(stack) > 0 and nums2[stack[-1]] < nums2[i]:       # 判断是否当前数字大于stack top数字
                top_index = stack.pop()
                if nums2[top_index] in nums1_map:       # 判断此数字是否在nums1里面出现
                    nums1_top_index = nums1_map[nums2[top_index]]
                    result[nums1_top_index] = nums2[i]
            stack.append(i)

        return result


class Solution2:
    def next_greater(self, nums):
        # 计算 nums 中每个元素的下一个更大元素
        n = len(nums)
        # 存放答案的数组
        res = [-1] * n
        stack = []

        # 倒着往栈里放
        for i in range(n - 1, -1, -1):
            # 判定个子高矮
            while stack and stack[-1] <= nums[i]:
                # 矮个起开，反正也被挡着了
                stack.pop()
            # nums[i] 身后的下一个更大元素，一定是栈顶元素，如果栈内有元素
            if stack:
                res[i] = stack[-1]
            stack.append(nums[i])

        return res

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Time O(n)
        Space O(n)
        同样的逻辑，单调栈，只是此方法先找到所有nums2里面元素的下一个最大元素的值并存进数组。
        之后再遍历nums1然后找到存在nums2里面的元素并提取出。
        """
        # 记录 nums2 中每个元素的下一个更大元素
        greater = self.next_greater(nums2)
        # 转化成映射：元素 x -> x 的下一个最大元素
        greater_map = {}
        for i in range(len(nums2)):
            greater_map[nums2[i]] = greater[i]
        # nums1 是 nums2 的子集，所以根据 greater_map 可以得到结果
        res = []
        for num in nums1:
            res.append(greater_map[num])

        return res


s = Solution()
print(s.nextGreaterElement1(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
