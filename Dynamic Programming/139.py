from typing import List


class Solution1:
    def backtracking(self, s, word_set, start_index):
        # 边界情况：已经遍历到字符串末尾，返回True，能进入递归的都是合理的切割
        if start_index >= len(s):
            return True

        # 遍历所有可能的拆分位置
        for i in range(start_index, len(s)):
            # 截取子串
            word = s[start_index: i + 1]
            if word in word_set:
                # 如果截取的子串在字典中，并且后续部分也可以被拆分成单词，返回True
                if self.backtracking(s, word_set, i + 1):
                    return True

        # 无法进行有效拆分，返回False
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Time O(2^n) 对于长度为n的s，总共有n-1种切缝，每个字符有两种情况，切和不切，所以总共有2^n个节点，每个节点O(1)的时间check存在
        Space O(n)
        回溯的写法，找出所有可能的组合然后判断是否存在，此方法存在大量的重复切割，也就是N叉树上面的节点有多个重复切过的结果。会超时。
        这里有个小技巧就是list转化成set，能大量节约check存在的时间到O(1)。
        """

        word_set = set(wordDict)

        return self.backtracking(s, word_set, 0)


class Solution2:
    def backtracking(self, s, word_set, start_index, memo):
        if start_index >= len(s):
            return True

        # 防止冗余计算，如果已经切割过之前，直接返回之前的切割结果
        if memo[start_index] != -1:
            return memo[start_index]

        for i in range(start_index, len(s)):
            word = s[start_index: i + 1]
            if word in word_set:
                if self.backtracking(s, word_set, i + 1, memo):
                    # 切割合理，备忘录记录此时的切割垫start index为1
                    memo[start_index] = 1
                    return True

        # 切割不合理，备忘录记录此时的切割垫start index为0
        memo[start_index] = 0
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Time O(2^n) 对于长度为n的s，总共有n-1种切缝，每个字符有两种情况，切和不切，所以总共有2^n个节点，每个节点O(1)的时间check存在。
        Space O(n)
        回溯的带备忘录的写法，逻辑和上面原始写法一模一样。区别在于加入一个memo的备忘录，记录此start index是否被切分过并且切分结果是true
        还是false，这样回溯中重复切割的地方就不用切割了。这样能大大降低重复的递归计算。
        """

        word_set = set(wordDict)
        # 备忘录，-1 代表未计算，0 代表无法凑出，1 代表可以凑出，备忘录初始化为 -1
        memo = [-1 for _ in range(len(s))]

        return self.backtracking(s, word_set, 0, memo)


class Solution3:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        """
        Time O(n^2)
        Space O(n)
        单词就是物品，字符串s就是背包，单词能否组成字符串s，就是问物品能不能把背包装满。完全背包问题，可以重复使用单词。
        递推公式： if([j, i] 这个区间的子串出现在字典里 && dp[j]是true) 那么 dp[i] = true。
        动态规划方法和带memo的回溯方法是一模一样的，dp就是memo，记录的就是以i结尾的index对应的s，能不能切割后由word dict组成。
        """
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                string_word = s[j: i]  # sub str j 是起始截取点，截取j到i的部分进行判断这个单词在不在dict里面
                if string_word in word_set and dp[j]:
                    dp[i] = True

        return dp[len(s)]


s = Solution2()
print(s.wordBreak(s="leetcode", wordDict=["leet", "code"]))
