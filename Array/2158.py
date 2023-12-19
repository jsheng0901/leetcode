from typing import List


class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        """
        Time O(n)
        Space O(n)
        遍历一次所有paint，用一个数组记录每一个index是否有被paint过，如果没有就paint并且记录进当前的距离，
        如果有，记录当前index能覆盖到的最远距离。用来表示下一步需要跳到的index。此题的核心思想是一个index by index的遍历是否被paint过。
        """
        # to paint of length K (here 6000) only once. If it was painted before, then it will get skipped.
        # 初始化数组
        dp = [0] * 60000

        ans = []
        for (start, end) in paint:
            # 当前可以paint的长度
            ans.append(0)
            ind = start
            # 遍历此区间所有可以paint到的点
            while ind < end:
                # this cell not painted so paint it
                # paint此index， 并且更新最远覆盖距离
                if dp[ind] == 0:
                    dp[ind] = end
                    ans[-1] += 1
                    ind += 1
                else:
                    # always update ind to max possible end,
                    # so we skip maximum iterations,
                    # but we don't want to accidentally update the wrong index
                    # so save next and then do updates
                    # if we update dp[ind] first, we get wrong next ind, if we do ind = dp[ind],
                    # we update wrong dp[ind], since end maybe larger than dp[ind]
                    # and then we will miss dp[ind] - end interval.
                    next_index = dp[ind]
                    dp[ind] = max(end, dp[ind])
                    ind = next_index
        return ans


s = Solution()
print(s.amountPainted(paint=[[1, 4], [5, 8], [4, 7]]))
