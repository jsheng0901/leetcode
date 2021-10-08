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
        O(n) time, 不 import defaultdict 更快一点
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


s = Solution()
print(s.groupStrings(strings=["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
