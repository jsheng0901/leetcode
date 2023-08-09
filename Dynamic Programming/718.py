class Solution:
    def findLength(self, nums1: [int], nums2: [int]) -> int:
        """
        记录两个数组的变化，用双loop
        Time O(n * m) 两个数组长度乘积
        Space O(n * m)
        """

        dp = [[0] * (len(nums2) + 1) for i in range(len(nums1) + 1)]
        result = 0

        for i in range(1, len(nums1)+1):        # 注意此处要取到等于数组的index，因为判断的时候要-1
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:    # 注意此处要-1判断，因为dp数组比实际nums数组index快一步
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > result:
                        result = dp[i][j]

        return result


s = Solution()
print(s.findLength(nums1=[1, 2, 3, 2, 1], nums2=[3, 2, 1, 4, 7]))
