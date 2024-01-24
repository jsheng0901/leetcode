from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Time O(n^2)
        Space O(1)
        把每个string和每个string里面字符当前二维数组来遍历，check每个是否相等。
        """
        m = len(strs)
        # 以第一行的列数为基准
        n = len(strs[0])
        for col in range(n):
            for row in range(1, m):
                this_str, prev_str = strs[row], strs[row - 1]
                # 判断每个字符串的 col 索引是否都相同
                if col >= len(this_str) or col >= len(prev_str) or this_str[col] != prev_str[col]:
                    # 发现不匹配的字符，只有 strs[row][0..col-1] 是公共前缀
                    return strs[row][:col]
        return strs[0]


s = Solution()
print(s.longestCommonPrefix(strs=["flower", "flow", "flight"]))
