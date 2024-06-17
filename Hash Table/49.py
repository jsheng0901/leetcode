from collections import defaultdict
from typing import List


class Solution1:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        """
        Time O(n * k * log(k)) n is length of list, k is length of element in list
        Space O(nk)
        use sorted string as key to store match str
        """
        hash_map = defaultdict(list)

        for i in strs:
            hash_map[str(sorted(i))].append(i)

        return hash_map.values()


class Solution2:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        """
        Time O(n * k) n is length of list, k is length of element in list
        Space O(nk)
        use tuple of count as key to store match str，这种方法对string的编码不需要排序，会更快，如果string本身很长的话。
        """
        hash_map = defaultdict(list)

        for i in strs:
            count = [0] * 26
            for c in i:
                count[ord(c) - ord('a')] += 1

            hash_map[tuple(count)].append(i)

        return hash_map.values()


class Solution3:
    def encode_count(self, s):
        count = [0] * 26
        for c in s:
            delta = ord(c) - ord('a')
            count[delta] += 1

        return str(count)

    def encode_sort(self, s):
        return str(sorted(s))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time O(n * k or n * k * log(k))
        Space O(n * k)
        同思路1和2，只是把两个方法换了一个方式写
        """
        string_to_group = defaultdict(list)
        for s in strs:
            code = self.encode_count(s)
            string_to_group[code].append(s)

        return list(string_to_group.values())


s = Solution3()
print(s.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
