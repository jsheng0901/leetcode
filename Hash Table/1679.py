from collections import defaultdict


class Solution:
    def maxOperations(self, nums: [int], k: int) -> int:
        """
        O(n) time, O(n) space
        记录rest的词频，每次check到存在的时候要减1，然后如果为0了就删除这个key
        """
        hash_map = defaultdict(int)
        count = 0

        for i in range(len(nums)):
            if k - nums[i] not in hash_map:
                hash_map[nums[i]] += 1
            else:
                count += 1
                hash_map[k - nums[i]] -= 1
                if hash_map[k - nums[i]] == 0:
                    del hash_map[k - nums[i]]

        return count
