from typing import List
from collections import defaultdict


class Solution:
    def get_difference(self, s):
        res = []

        for i in range(1, len(s)):
            difference = ord(s[i]) - ord(s[i - 1])
            if difference < 0:
                difference += 26
            res.append(str(difference))

        return str(0) if len(res) == 0 else "".join(res)

    def groupStrings(self, strings: [str]) -> [[str]]:
        """
        Time O(n) 不 import defaultdict 更快一点
        Space O(n)
        构建一个ex: {'string difference': {'length of string[i]': index}), 再loop出结果
        """
        # length_to_index = defaultdict(list)
        # difference_to_index = defaultdict(lambda: defaultdict(list))
        difference_to_index = {}
        for i in range(len(strings)):
            difference = self.get_difference(strings[i])
            if difference in difference_to_index:
                if str(len(strings[i])) in difference_to_index[difference]:
                    difference_to_index[difference][str(len(strings[i]))].append(i)
                else:
                    difference_to_index[difference][str(len(strings[i]))] = [i]
            else:
                difference_to_index[difference] = {str(len(strings[i])): [i]}
            # difference_to_index[difference][len(strings[i])].append(i)

        ans = []
        for k, v in difference_to_index.items():
            for value in v.values():
                ans.append([strings[i] for i in value])

        return ans


class Solution2:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """
        Time O(n)
        Space O(n)
        同上思路，区别在于我们只需要记录所有 {difference: [string1, string2]} 的pairs。最后输出所有values即可。
        这题难点在于如何记录 'z' 的情况，我们采取如果是负数就 +26，round到下一轮，如果是正数就直接记录。
        """
        # 构建 difference to string 的字典
        string_to_index = defaultdict(list)
        for index, string in enumerate(strings):
            # 特殊情况长度为1，直接记录string
            if len(string) == 1:
                string_to_index['1'].append(string)
                continue
            tmp = ''
            # 对于所有其它情况，计算difference
            for i in range(1, len(string)):
                diff = ord(string[i]) - ord(string[i - 1])
                # 负数则直接 +26
                if diff < 0:
                    tmp += str(diff + 26)
                else:
                    tmp += str(diff)
                tmp += ','
            string_to_index[tmp].append(string)

        # 返回所有values
        return string_to_index.values()


s = Solution2()
print(s.groupStrings(strings=["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
