class Solution:
    def shortestToChar(self, s: str, c: str) -> [int]:
        """数组的正反遍历，记录正向情况下离最新target的距离，在记录反向情况下的距离并比较哪个最短"""
        result = []
        pre = float('-inf')

        for i in range(len(s)):
            if s[i] == c:
                pre = i
            result.append(i - pre)

        pre = float('inf')
        for j in range(len(s) - 1, -1, -1):
            if s[j] == c:
                pre = j
            result[j] = min(result[j], pre - j)

        return result
