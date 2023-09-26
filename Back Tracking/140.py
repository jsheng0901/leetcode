from typing import List, Dict


class Solution1:
    def __init__(self):
        self.result = []
        self.path = []

    def backtrakcing(self, s, wordDict, start_index):
        if start_index == len(s):
            self.result.append(" ".join(self.path))
            return

        for i in range(start_index, len(s)):
            sub = s[start_index: i + 1]
            if sub in wordDict:
                self.path.append(sub)
                self.backtrakcing(s, wordDict, i + 1)
                self.path = self.path[:-1]

        return

    def wordBreak(self, s: str, wordDict: [str]) -> [str]:
        """
        Time O(2^n)
        Space O(n)
        回溯经典模板题，遍历所有切割情况，然后找到合规的加入result。
        """
        self.backtrakcing(s, wordDict, 0)

        return self.result


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        word_set = set(wordDict)
        memo = [None] * len(s)
        return self.dp(s, 0, word_set, memo)

    # 定义：返回用 wordDict 构成 s[i..] 的所有可能
    def dp(self, s: str, i: int, wordDict: set, memo: List[Dict[int, List[str]]]) -> List[str]:

        res = []
        if i == len(s):
            res.append("")
            return res
        # 防止冗余计算
        if memo[i] is not None:
            return memo[i]

        # 遍历 s[i..] 的所有前缀
        for j in range(i + 1, len(s) + 1):
            # 看看哪些前缀存在 wordDict 中
            prefix = s[i:j]
            if prefix in wordDict:
                # 找到一个单词匹配 s[i..i+j)
                sub_problem = self.dp(s, j, wordDict, memo)
                # 构成 s[i+j..] 的所有组合加上 prefix
                # 就是构成构成 s[i] 的所有组合
                for sub in sub_problem:
                    if sub == "":
                        # 防止多余的空格
                        res.append(prefix)
                    else:
                        res.append(prefix + " " + sub)

        # 存入备忘录
        memo[i] = res

        return res


class Solution3:
    def backtracking(self, s, word_set, start_index, memo):
        res = []
        if start_index == len(s):
            res.append("")
            return res

        # 防止冗余计算
        if memo[start_index]:
            return memo[start_index]

        # 遍历同一层所有切割情况
        for i in range(start_index, len(s)):
            word = s[start_index: i + 1]
            # 合理的切割词才进入下一层
            if word in word_set:
                # 找到一个单词匹配 s[start..start+i)
                sub_problem = self.backtracking(s, word_set, i + 1, memo)
                # 构成 s[start+i..] 的所有组合加上 prefix
                # 就是构成构成 s[start..] 的所有组合
                for sub in sub_problem:
                    if sub == "":
                        # 防止多余的空格
                        res.append(word)
                    else:
                        # 加入所有合理的s[start+i..]组合和prefix的组合进此层的结果
                        res.append(word + " " + sub)

        # 加入备忘录
        memo[start_index] = res

        return res

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        Time O(n * len(result)) 每次子问题的长度是len(result) 可能更快也可能没有不带memo的情况。
        Space O(n)
        带备忘录的回溯，和solution2是一个逻辑，每次我们找到合理的path的时候不要理解结束同层的遍历，而是把合理的组合加入进同一层的数组。
        并存入memo对应的index记录此分割点下所有合理的组合情况，之后继续遍历整个回溯树。
        """

        word_set = set(wordDict)
        memo = [None] * len(s)

        return self.backtracking(s, word_set, 0, memo)


s = Solution3()
print(s.wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]))
