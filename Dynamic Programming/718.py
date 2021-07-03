class Solution:
    def findLength(self, nums1: [int], nums2: [int]) -> int:
        """
        dp类型，记录两个数组的变化，用双loop
        time O(n * m), space O(n * m)
        :param nums1:
        :param nums2:
        :return:
        """

        dp = [[0] * (len(nums2) + 1) for i in range(len(nums1) + 1)]
        result = 0

        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > result:
                        result = dp[i][j]

        return result


s = Solution()
print(s.findLength(nums1=[1, 2, 3, 2, 1], nums2=[3, 2, 1, 4, 7]))
