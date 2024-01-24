from typing import List


class Solution:
    def dp(self, stickers, target, index, memo):
        # 走到底了，此时target已经全部移除完，说明我们找到了一条合理的path，返回0
        if target == "":
            return 0
        # sticker已经用完了，但是没有移除完target，说明这条path不合理，返回一恶搞最大值，注意这里一定要返回最大值，
        # 因为我们后面要用min取最小值，如果这里返回-1，则最终只要出现有不合理的path返回值永远是-1
        if index == len(stickers):
            return float('inf')

        # 构建备忘录的key
        key = (index, target)
        # 如果之前出现过直接返回结果
        if key in memo:
            return memo[key]

        # 第一种情况，不用这个sticker，直接跳入下一个sticker
        res = self.dp(stickers, target, index + 1, memo)

        # 第二种情况，用这个sticker，开始移除target词里面存在sticker里面的字符
        cur_sticker = stickers[index]
        new_target = target
        # 用一个flag标记是否有字符需要被移除
        cur_sticker_used = False
        for c in cur_sticker:
            # 找到移除的index
            ind_to_remove = new_target.find(c)
            # 开始移除，合并新的string
            if ind_to_remove != -1:
                new_target = new_target[:ind_to_remove] + new_target[ind_to_remove + 1:]
                # 更新flag
                cur_sticker_used = True

        # 如果有移除的字符说明我们有用到这个sticker，此时当前节点的返回值要 +1，同时取当前节点返回值的最小值
        if cur_sticker_used:
            res = min(res, 1 + self.dp(stickers, new_target, index, memo))

        # 更新备忘录
        memo[key] = res

        return res

    def minStickers(self, stickers: List[str], target: str) -> int:
        """
        Time O(len(stickers) * len(target))
        Space O(len(stickers) * len(target))
        核心思路，对于当前的sticker我们有两种状态，选择此sticker或者不选择此sticker。
        1. 选择此sticker，那么我们就把target里面所有和此sticker里面相同的字符都过滤掉，然后继续遍历
        2. 不选择此sticker，那么我们就直接跳过这个sticker，进入下一个sticker。
        每个状态分别由此sticker的index和此时的target值决定，所以我们的备忘录要记录这两种状态的组合情况，分别对应我们用了多少sticker。
        """
        # 这里备忘录用字典来记录，因为index和target的组合不好构建成数组，变成一个tuple作为字典的key
        res = self.dp(stickers, target, 0, {})

        return res if res != float('inf') else -1


s = Solution()
print(s.minStickers(stickers=["with", "example", "science"], target="thehat"))
