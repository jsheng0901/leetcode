class Solution:
    def largestSumAfterKNegations(self, nums: [int], k: int) -> int:
        """
        Time O(n)
        Space O(n) sorted会产生新的数组copy
        第一步：将数组按照绝对值大小从大到小排序，注意要按照绝对值的大小
        第二步：从前向后遍历，遇到负数将其变为正数，同时K--
        第三步：如果K还大于0，那么反复转变数值最小的元素，将K用完
        第四步：求和
        """
        nums = sorted(nums, key=abs, reverse=True)  # 第一步
        for i in range(len(nums)):
            if k > 0 > nums[i]:
                nums[i] *= -1
                k -= 1

        # while k > 0:
        #     nums[-1] *= -1
        #     k -= 1
        # 直接判断奇数或者偶数剩下的k
        if k % 2 == 1:
            nums[-1] *= -1

        result = sum(nums)

        return result


s = Solution()
print(s.largestSumAfterKNegations(nums=[4, 2, 3], k=1))
