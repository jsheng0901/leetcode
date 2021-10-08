class Solution:
    def numDecodings(self, s: str) -> int:
        #         count = 0

        #         def isValid(sub):
        #             if len(sub) > 2:
        #                 return False
        #             if sub[0] == '0':
        #                 return False
        #             if int(sub) > 26:
        #                 return False

        #             return True

        #         def backtracking(s, start_index, count):
        #             if start_index >= len(s):
        #                 count += 1
        #                 return count

        #             for i in range(start_index, len(s)):
        #                 sub = s[start_index: i+1]
        #                 if isValid(sub):
        #                     count = backtracking(s, i+1, count)
        #             return count

        #         count = backtracking(s, 0, 0)

        #         return count
        # 回溯的做法超时，dp的做法是，当前数字有前一个和前两数字的情况来决定，和爬楼梯一个道理
        if len(s) == 0 or (len(s) > 1 and s[0] == '0'):
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(dp)):
            dp[i] = 0 if s[i - 1] == '0' else dp[i - 1]
            two_digit = int(s[i - 2: i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]

