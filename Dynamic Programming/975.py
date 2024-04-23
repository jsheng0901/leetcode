from typing import List


class Solution:
    def get_next_index(self, sortedIdx):
        # find next index of current index that is the least large/small
        stack = []
        result = [None] * len(sortedIdx)

        for i in sortedIdx:
            # 如果当前index大于栈顶index，因为已经sort过了，所有说明我们找到了当前栈顶的index对应的下一个更大或者更小的index
            while stack and i > stack[-1]:
                # 给result赋值
                result[stack.pop()] = i
            # 入栈记录当前index
            stack.append(i)
        return result

    def oddEvenJumps(self, arr: List[int]) -> int:
        """
        Time O(n * log(n) + n)
        Space O(n)
        理解此题是核心要点，换句话来说，每个index可以跳偶数或者奇数步，奇数需要跳到的地方大于当前数并且是所有可以的index中最小的那个。
        偶数刚刚好相反。所以这里我们可以找到每个情况对应的index的下一个可以走到的index，对于计数，我们从小到大sort，然后找下一个更大的，
        对于偶数我们完全相反sort，找下一个更小的。存储下来后，用dp的思路，每个index都有两种状态到达，遍历所有index，计算每个状态可以
        到达的下一个index的个数，详细见注释。dp[i]表示到达当前i的时候总共有多少个可以起始的index，无论跳计数还是偶数步。
        """

        # 从小到大排序，对应的在原始arr里面的index
        sorted_idx = sorted(range(len(arr)), key=lambda x: arr[x])
        odd_indexes = self.get_next_index(sorted_idx)

        # 从大到小排序，对应的在原始arr里面的index
        sorted_idx.sort(key=lambda x: -arr[x])
        even_indexes = self.get_next_index(sorted_idx)

        # [odd, even], the 0th jump is even，偶数自动可以跳到初始index 0
        dp = [[0, 1] for _ in range(len(arr))]

        for i in range(len(arr)):
            # 如果当前有奇数步可以跳，记录
            if odd_indexes[i] is not None:
                dp[odd_indexes[i]][0] += dp[i][1]
            # 如果当前有偶数步可以跳，记录
            if even_indexes[i] is not None:
                dp[even_indexes[i]][1] += dp[i][0]
        # 返回两种状态到达最后的总和
        return dp[-1][0] + dp[-1][1]


s = Solution()
print(s.oddEvenJumps(arr=[2, 3, 1, 1, 4]))
