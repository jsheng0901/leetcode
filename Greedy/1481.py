from collections import defaultdict


class Solution:
    def findLeastNumOfUniqueInts(self, arr: [int], k: int) -> int:
        """
        O(n log(n)) time, O(n) space
        贪心的思路，把出现频率最小的先移除掉
        """
        mapping = defaultdict(int)
        for i in arr:
            mapping[i] += 1

        mapping = sorted(mapping.values())

        number_to_remove = 0
        for i in range(len(mapping)):
            number_to_remove += mapping[i]
            if number_to_remove > k:
                return len(mapping) - i

        return 0




