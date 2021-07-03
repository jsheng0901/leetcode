class Solution:
    def containsNearbyDuplicate1(self, nums: [int], k: int) -> bool:
        """
        用hash table记录出现的index, 然后有重复的就计算差值看是否符合小于等于k
        :param nums:
        :param k:
        :return:
        """
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
            else:
                index1 = d[nums[i]]
                diff = abs(index1 - i)
                if diff <= k:
                    return True
                else:
                    d[nums[i]] = i

        return False


s = Solution()
print(s.containsNearbyDuplicate1(nums=[1, 2, 3, 1], k=3))
