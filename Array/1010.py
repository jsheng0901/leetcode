from collections import defaultdict


class Solution:

    def numPairsDivisibleBy60(self, time: [int]) -> int:
        """two sum的改编版本，需要想清楚hash map里面要存什么东西"""
        count = 0
        hash_map = defaultdict(int)

        for i in range(len(time)):
            if 60 - (time[i] % 60) in hash_map:
                count += hash_map[60 - (time[i] % 60)]
            if time[i] % 60 == 0:
                count += hash_map[0]

            hash_map[time[i] % 60] += 1     # store modulo

        return count
