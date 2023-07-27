class Solution:
    def canJump(self, nums: [int]) -> bool:
        """
        Time O(n)
        Space O(1)
        这个问题就转化为跳跃覆盖范围究竟可不可以覆盖到终点！
        贪心算法局部最优解：每次取最大跳跃步数（取最大覆盖范围），整体最优解：最后得到整体最大覆盖范围，看是否能到终点
        """
        cover = 0
        if len(nums) == 1:
            return True

        for i in range(len(nums)):      # python 不能写动态范围，不能写range(cover)，python并不会更新cover变化后的loop范围
            # python 要改成全局loop，每一次记录可到的最远范围并且对比此时loop的点是不是还在范围内，如果超出在说明到不了，否则继续更新范围
            if i > cover:
                return False
            else:
                cover = max(i + nums[i], cover)     # 取最大覆盖范围
                if cover >= len(nums) - 1:
                    return True

        return False


s = Solution()
print(s.canJump(nums=[3, 2, 1, 0, 4]))
print(s.canJump(nums=[1, 1, 1, 0]))
