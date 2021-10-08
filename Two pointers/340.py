from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """
        O(n) time, O(k) space
        双指针 + hahs_map 记录frequency， 如果超过两个key就开始移动左指针并同时删除frequency，如果frequency为0则删除key
        记录最长的substring
        """
        p1 = 0
        p2 = 0
        hash_map = defaultdict(int)
        length = float('-inf')

        while p2 < len(s):
            hash_map[s[p2]] += 1

            while len(hash_map.keys()) > k:
                hash_map[s[p1]] -= 1
                if hash_map[s[p1]] == 0:
                    del hash_map[s[p1]]
                p1 += 1

            length = max(length, p2 - p1 + 1)
            p2 += 1

        return length


