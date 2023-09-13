from collections import defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Time O(n)
        Space O(n)
        同567，区别在于这里找到一个符合substring排列情况，则加入起始index进结果。
        """
        window = defaultdict(int)
        need = defaultdict(int)

        for c in p:
            need[c] += 1

        left, right = 0, 0
        valid = 0

        result = []

        while right < len(s):
            # 加入窗口的字符
            c = s[right]
            right += 1

            # 进行窗口内数据的一系列更新
            if c in need:
                # 注意此处一定要先加入window再判断，因为c是加进来的字符
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否要收缩
            while right - left >= len(p):
                # 当窗口符合条件时，把起始索引加入 result
                if valid == len(need):
                    result.append(left)

                d = s[left]
                left += 1
                # 进行窗口内数据的一系列更新
                if d in need:
                    # 注意此处和前面加入不一样，先判断再删减，因为此时d已经在窗口里面，所以先判断是否符合的情况
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return result


s = Solution()
print(s.findAnagrams(s="cbaebabacd", p="abc"))
