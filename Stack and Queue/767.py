from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        Time O(n * log(k) --> n)       k bounded by 26
        Space O(k --> 1)
        有很多种重新组合的方式，我们可以先从频率出现最高地开始排，每次交叉排序频率最高的字符，如果最终重新排完的和之前的一样，
        说明找到合理的排序方式，如果不一样，说明无法排出合理的string。
        """
        # 记录每个字符出现的频率
        freq = Counter(s)
        pq = []
        # 把频率从大到小放进优先列队，注意Python是小顶堆，所以要放负数进去
        for key, value in freq.items():
            heapq.heappush(pq, (-value, key))

        # 开始遍历整个优先列队
        res = ""
        # 用一个指针记录上一个弹出的频率最大值元素，不能弹出后立即加入列队，因为可能会出现加入后依旧是最高频率的元素，所有需要一个指针来记录，
        # 等到下一个最高频率的元素使用完再重新加入列队
        tmp = None
        while pq:
            # 列队头
            value, key = heapq.heappop(pq)
            # 加入结果
            res += key
            # 如果上一个指针存在并且使用完后频率没有变成0，则从新加入列队
            if tmp and tmp[0] != 0:
                heapq.heappush(pq, tmp)
            # tmp指针记录当前弹出的元素，value + 1 是因为已经使用过一次，这里是负数所有是 +1
            tmp = (value + 1, key)

        # check是否等长，如果相等说明重新排列成功，不相等说明不成功，返回空string
        return "" if len(res) != len(s) else res


s = Solution()
print(s.reorganizeString(s="aab"))
print(s.reorganizeString(s="aaabb"))
