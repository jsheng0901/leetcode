from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        """
        Time O(n)
        Space O(n)
        用两个hash table：
            freq 记录数字出现的频率，一个元素判断自己是否能够作为开头，
            need 记录需要的次数，记录哪些元素可以被接到其他子序列后面，帮助一个元素判断自己是否可以被接到其他序列后面。
        每个数字当前元素n两种情况加入子序列分配。
            第一种：当前元素 n 自成一派，「以自己开头」构成一个长度至少为 3 的序列。
            第二种：当前元素 n 接到已经存在的子序列后面。
        优先判断自己是否能够接到其他序列后面，如果不行，再判断是否可以作为新的子序列开头。
        """

        freq = {}
        need = {}
        # 使用字典统计 nums 中元素的频率
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for n in nums:
            # 已经被用到其他子序列中
            if freq[n] == 0:
                continue
            # n 可以接到之前的某个序列后面，优先判断这种情况
            elif n in need and need[n] > 0:
                freq[n] -= 1
                need[n] -= 1
                # 这个数字的下一个数字需要加入need来判断下一个数字是否能加到此序列后面
                need[n + 1] = need.get(n + 1, 0) + 1
            # 将 n 作为开头，新建一个长度为 3 的子序列 [n, n + 1, n + 2]
            elif freq[n] > 0 and freq.get(n + 1, 0) > 0 and freq.get(n + 2, 0) > 0:
                # 这里需要直接使用三个连续的数字，所以需要直接连续三个数字 -1
                freq[n] -= 1
                freq[n + 1] -= 1
                freq[n + 2] -= 1
                # 第四个数字需要加入need来判断这个数字是否能加到此新建的序列后面
                need[n + 3] = need.get(n + 3, 0) + 1
            else:
                # 两种情况都不符合，则无法分配
                return False

        return True


s = Solution()
print(s.isPossible(nums=[1, 2, 3, 3, 4, 4, 5, 5]))
