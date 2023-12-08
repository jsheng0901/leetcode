import heapq
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Time O(n + k * log(k))
        Space O(n + k * log(k))
        把所有单词出现的频率按照从大到小加入优先列队，列队顶是最高频率字符，之后一个一个弹出并乘以频率加入新的string。
        注意Python里面是小顶堆，所以变成大顶堆要转为负数加入。
        构建hashmap + 每个unique字符加入一次heap，这里有个trick是unique字符最多可能就256个，则 k * log(k) -> O(1)
        """
        # 统计出现频率
        freq = Counter(s)
        pq = []
        # 按照频率从大到小加入列队
        for key, value in freq.items():
            heapq.heappush(pq, (-value, key))

        res = ""
        # 弹出所有字符并组成新字符
        while len(pq) > 0:
            value, key = heapq.heappop(pq)
            # 频率高地排前面
            res += key * -value

        return res


s = Solution()
print(s.frequencySort(s="tree"))
