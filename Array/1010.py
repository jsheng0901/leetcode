from collections import defaultdict
from typing import List


class Solution:

    def numPairsDivisibleBy60(self, time: [int]) -> int:
        """
        Time O(n)
        Space O(n)
        two sum的改编版本，需要想清楚hash map里面要存什么东西。我们每次需要找的是如果 a % 60 == 0，则需要 b % 60 == 0 或者
        ((a % 60) + (b % 60)) % 60 == 0。
        """
        count = 0
        hash_map = defaultdict(int)

        for i in range(len(time)):
            if 60 - (time[i] % 60) in hash_map:
                count += hash_map[60 - (time[i] % 60)]
            if time[i] % 60 == 0:
                count += hash_map[0]

            hash_map[time[i] % 60] += 1  # store modulo

        return count


class Solution2:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        同第一个一模一样的思路，换一个写法
        """
        count = 0
        remainders = defaultdict(int)

        for t in time:
            if t % 60 == 0:
                count += remainders[0]
            else:
                count += remainders[60 - t % 60]

            remainders[t % 60] += 1

        return count


class Solution3:
    def __init__(self):
        self.res = 0

    def backtracking(self, time, path, start):
        if len(path) == 2:
            if sum(path) % 60 == 0:
                self.res += 1
            return

        for i in range(start, len(time)):
            path.append(time[i])
            self.backtracking(time, path, i + 1)
            path.pop()

        return

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        Time O(n!)
        Space O(n)
        回溯写法，找到所有组合，然后再找到所有符合要求的组合，超时。
        """
        self.backtracking(time, [], 0)

        return self.res


s = Solution2()
print(s.numPairsDivisibleBy60(time=[30, 20, 150, 100, 40]))
