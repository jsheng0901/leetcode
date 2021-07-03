class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        """
        time: O(n), space: O(1)
        贪心的原则是当局部总和是0的时候我们就取下一个作为连续区间起始位置, 然后更新记录最大总和
        :param nums:
        :return:
        """
        result = float('-inf')
        count = 0  # 临时记录总和
        for i in nums:
            count += i
            if count > result:  # 取区间累计的最大值（相当于不断确定最大子序终止位置）
                result = count

            if count <= 0:
                # 相当于重置最大子序起始位置，因为遇到负数一定是拉低总和, 此处不用担心为0的情况，因为如果下一个是负数
                # result结果并不会更新
                count = 0

        return result


s = Solution()
print(s.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
