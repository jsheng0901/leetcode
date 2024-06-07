class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Time O(n)
        Space O(1)
        双指针基础题，同时移动指针并且放进结果，然后再判断是否有剩下没有走完的部分，直接加入结果。
        """
        p1 = 0
        p2 = 0
        res = ""
        # 双指针走完最短的单词
        while p1 < len(word1) and p2 < len(word2):
            # 依次加入结果
            res += word1[p1]
            res += word2[p2]
            # 移动指针
            p1 += 1
            p2 += 1

        # 判断是否还有剩下的部分，有的话，直接加入结果
        if p1 < len(word1):
            res += word1[p1:]
        if p2 < len(word2):
            res += word2[p2:]

        return res


class Solution2:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Time O(n)
        Space O(1)
        一样的思路，但是单指针。
        """
        result = []
        # 遍历最长的单词
        n = max(len(word1), len(word2))
        for i in range(n):
            # 如果单词还有没用完的，加入结果，这里一定要判断一下先，不然会出现短的单词先走完的情况
            if i < len(word1):
                result += word1[i]
            # 同上
            if i < len(word2):
                result += word2[i]

        return "".join(result)


s = Solution2()
print(s.mergeAlternately(word1="abc", word2="pqr"))
print(s.mergeAlternately(word1="abcd", word2="pq"))
