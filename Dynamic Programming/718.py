class Solution:
    def findLength(self, nums1: [int], nums2: [int]) -> int:
        """
        Time O(n * m) 两个数组长度乘积
        Space O(n * m)
        dp[i][j] ：以下标i - 1为结尾的A，和以下标j - 1为结尾的B，最长重复子数组长度为dp[i][j]。
        """

        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        result = 0
        # 遍历数组 nums1
        for i in range(1, len(nums1)+1):        # 注意此处要取到等于数组的index，因为判断的时候要-1
            # 遍历数组 nums2
            for j in range(1, len(nums2)+1):
                # 如果 nums1[i-1] 和 nums2[j-1] 相等
                if nums1[i-1] == nums2[j-1]:    # 注意此处要-1判断，因为dp数组比实际nums数组index快一步
                    # 在当前位置上的最长公共子数组长度为前一个位置上的长度加一
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    # 更新最长公共子数组的长度
                    if dp[i][j] > result:
                        result = dp[i][j]
        # 返回最长公共子数组的长度
        return result


s = Solution()
print(s.findLength(nums1=[1, 2, 3, 2, 1], nums2=[3, 2, 1, 4, 7]))
