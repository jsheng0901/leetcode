class Solution:
    def jump(self, nums: [int]) -> int:
        """
        「所以真正解题的时候，要从覆盖范围出发，不管怎么跳，覆盖范围内一定是可以跳到的，以最小的步数增加覆盖范围，
        覆盖范围一旦覆盖了终点，得到的就是最小步数！」
        此题不能以计算是否覆盖的方式每次计算次数，因为会多计算跳的步骤，一定要跳到当前最远覆盖范围的点的距离的时候再计算次数
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return 0

        cur = 0     # 当前覆盖最远距离下标
        next = 0    # 记录走的最大步数
        ans = 0     # 下一步覆盖最远距离下标

        for i in range(len(nums)):
            next = max(i + nums[i], next)           # 更新下一步覆盖最远距离下标
            if i == cur:                            # 遇到当前覆盖最远距离下标
                if cur != len(nums) - 1:            # 如果当前覆盖最远距离下标不是终点
                    ans += 1                        # 需要走下一步
                    cur = next                      # 更新当前覆盖最远距离下标（相当于加油了）
                    if next >= len(nums) - 1:       # 下一步的覆盖范围已经可以达到终点，结束循环
                        break
                else:
                    break                           # 当前覆盖最远距离下标是集合终点，不用做ans++操作了，直接结束

        return ans


s = Solution()
print(s.jump(nums=[2, 3, 1, 1, 4]))
print(s.jump(nums=[2, 3, 0, 1, 4]))