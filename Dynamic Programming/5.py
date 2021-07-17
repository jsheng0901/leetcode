class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        """
        回溯，当左括号的数量小的时候就一直叠加，树的深度及，保证右括号永远小雨等于左括号
        :param n:
        :return:
        """
        ans = []

        def backtrack(S=[], left=0, right=0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right + 1)
                S.pop()

        backtrack()
        return ans

