class Solution:
    def firstMissingPositive(self, nums: [int]) -> int:
        """
        use extra list to store
        first put all element in to new list according to their index, ex: 4 in index 4, then loop over new list from
        1 index, if element is not equal to index then which means this element not in original nums
        :param nums:
        :return:
        """
        l = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            if 0 < nums[i] < len(l):
                l[nums[i]] = nums[i]

        for j in range(1, len(l)):
            if l[j] != j:
                return j

        return len(l)


s = Solution()
print(s.firstMissingPositive(nums=[1, 2, 0]))