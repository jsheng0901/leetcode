from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """
        Time O(n * k)
        Space O(1)   --> only 26 characters
        找到每个word的交集对应的最小频率，这里注意，其实没有出现在交际里面的character并不需要移除，因为我们会计算最小值，没出现的会变成0。
        之后只需要按照所有交集出现的character的频次放进结果即可。
        """
        res = []
        # 计算第一个词每个character出现的频率
        common = Counter(words[0])

        for word in words[1:]:
            # 当前词每个character出现的频率
            cur_freq = Counter(word)
            # 对于出现过的或者没出现的character计算出现的最小频率，没出现就会变成0，出现过去最小频率
            for c in common:
                common[c] = min(common[c], cur_freq[c])

        # 按照所有交集出现的character的频次放进结果
        for k, v in common.items():
            for i in range(v):
                res.append(k)

        return res


s = Solution()
print(s.commonChars(
    words=["bbddabab", "cbcddbdd", "bbcadcab", "dabcacad", "cddcacbc", "ccbdbcba", "cbddaccc", "accdcdbb"]))
