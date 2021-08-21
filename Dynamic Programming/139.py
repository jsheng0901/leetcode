class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        """
        单词就是物品，字符串s就是背包，单词能否组成字符串s，就是问物品能不能把背包装满。
        完全背包问题， 重复使用单词可以
        递推公式是 if([j, i] 这个区间的子串出现在字典里 && dp[j]是true) 那么 dp[i] = true。
        :param s:
        :param wordDict:
        :return:
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                string_word = s[j: i]  # substr j 是起始截取点，截取j到i的部分进行判断这个单词在不在dict里面
                if string_word in wordDict and dp[j]:
                    dp[i] = True

        return dp[len(s)]

s = Solution()
print(s.wordBreak(s="leetcode", wordDict=["leet", "code"]))
