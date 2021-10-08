class Solution:
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
        classic backtracking problem, just loop over all combination,
        but make sure substring is valid first before backtracking
        """
        self.backtrakcing(s, wordDict, 0)

        return self.result


s = Solution()
print(s.wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]))
