from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        Time O(n)
        Space O(n)
        先loop一遍统计出现频率，再loop一次所有频率，check是否有重复的频率
        """
        hash_map = {}
        for i in arr:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1

        check_occ = set()
        for k, v in hash_map.items():
            if v not in check_occ:
                check_occ.add(v)
            else:
                return False

        return True
