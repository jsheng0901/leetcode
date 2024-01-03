from typing import List


class Solution:
    def dp(self, stones, index, prev, stone_to_index, memo):
        # 如果走到底了，说明找到一条合理的path，返回true
        if index == len(stones) - 1:
            return True
        # 如果之前此状态计算过，直接返回结果
        if memo[index][prev] != -1:
            return memo[index][prev]

        # 当前节点的返回结果，初始化为false
        sub = False
        # 遍历同一层所有可能的分支，也就是跳跃的步数
        for jump in [prev - 1, prev, prev + 1]:
            # 如果是负数说明往后跳，跳过
            if jump < 0:
                continue
            # 如果跳到的stone不存在stones的列表里，跳过
            if stones[index] + jump not in stone_to_index:
                continue
            # 下一个跳到的index
            next_index = stone_to_index[stones[index] + jump]
            # 如果下一个等于当前index，说明在原地，跳过
            if next_index == index:
                continue
            # 开始合理递归，返回子节点的所有结果，有一个为true则当前结果返回true
            sub = sub or self.dp(stones, next_index, jump, stone_to_index, memo)

        # 记录备忘录，注意是当前节点状态的备忘录
        memo[index][prev] = sub
        # 返回当前节点返回值
        return sub

    def canCross(self, stones: List[int]) -> bool:
        """
        Time O(n^2)
        Space O(n^2)
        把问题转化成树的递归结构，我们需要找到一条符合条件的从根节点到叶子结点的path。
        走到每个石头都有不同的step跳过来的走法，下一步总共有三种走法，我们遍历每一种走法之后只有有一种成功说明，子节点的返回值成功。从后向前，
        返回结果，递归带备忘录的写法。备忘录需要存储的参数为动态变化的参数，也就是stone的index和到达此处index的jump步数。
        """
        # 初始化备忘录，因为最大值是2000，所以直接初始化一个最大的二维数组
        memo = [[-1] * 2000 for _ in range(2000)]
        # 存储stone和index的关系
        stone_to_index = {}
        for i, v in enumerate(stones):
            stone_to_index[v] = i

        return self.dp(stones, 0, 0, stone_to_index, memo)


class Solution2:
    def canCross(self, stones: List[int]) -> bool:
        """
        Time O(n^2)
        Space O(n^2)
        一模一样的思路，只是换成了loop的写法。注意这里dp数组的初始化。
        """
        # 初始化为false先
        dp = [[False] * 2000 for _ in range(2000)]
        stone_to_index = {}
        for i, v in enumerate(stones):
            stone_to_index[v] = i
        # 第一个状态为true
        dp[0][0] = True

        for index in range(len(stones)):
            for jump in range(len(stones)):
                # 如果当前状态为true才能跳下一步
                if dp[index][jump]:
                    # 三种跳的情况
                    if stones[index] + jump in stone_to_index:
                        dp[stone_to_index[stones[index] + jump]][jump] = True
                    if stones[index] + jump + 1 in stone_to_index:
                        dp[stone_to_index[stones[index] + jump + 1]][jump + 1] = True
                    if stones[index] + jump - 1 in stone_to_index:
                        dp[stone_to_index[stones[index] + jump - 1]][jump - 1] = True

        # 如果最后一个index对应的状态有一个true则说明有一种走到最后的path，返回true
        for jump in range(len(stones)):
            if dp[len(stones) - 1][jump]:
                return True

        return False


s = Solution2()
print(s.canCross(stones=[0, 1, 3, 5, 6, 8, 12, 17]))
