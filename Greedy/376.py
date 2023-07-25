class Solution:
    def wiggleMaxLength(self, nums: [int]) -> int:
        """
        time: O(n), space: O(1)
        局部最优：删除单调坡度上的节点（不包括单调坡度两端的节点），那么这个坡度就可以有两个局部峰值
        整体最优：整个序列有最多的局部峰值，从而达到最长摆动序列
        """
        if len(nums) <= 1:
            return len(nums)

        cur_diff = 0  # 当前一对差值

        pre_diff = 0  # 前一对差值, 给定一个初始差值，这样当长度为2的时候也会自动比较初始值

        result = 1  # 记录峰值个数，序列默认序列最右边有一个峰值

        # for i in range(len(nums) - 1):    # 或者可以从第一个开始loop，但是ending是倒数第二个
        #     cur_diff = nums[i + 1] - nums[i]
        for i in range(1, len(nums)):
            cur_diff = nums[i] - nums[i - 1]
            # 出现峰值
            if cur_diff > 0 >= pre_diff or cur_diff < 0 <= pre_diff:
                result += 1
                pre_diff = cur_diff

        return result


s = Solution()
print(s.wiggleMaxLength(nums=[1, 2, 3]))
