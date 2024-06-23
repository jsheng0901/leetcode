from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Time O(n * log(n))
        Space O(n)
        贪心思想为主，如果我们想船用的最少，只需要找到所有两两配对最接近limit值的个数，所以我们用左右指针最胖和最瘦的开始配对，如果配对成功
        则上一条船，如果失败，说明最胖的一定需要一个人一条船，相对应的移动指针。
        """
        # 先sort一下，保证从小到大排序
        people.sort()

        res = 0
        # 左右指针
        left = 0
        right = len(people) - 1

        # 记得当左右指针相等的时候也要进一次loop，因为最中间那个人也需要一条船
        while left <= right:
            # 船数量 +1
            res += 1
            # 如果配对成功小于limit
            if people[left] + people[right] <= limit:
                # 左右指针都移动到下一个人
                left += 1
                right -= 1
            # 如果失败
            else:
                # 则说明最胖的那个需要一条船，移动右指针
                right -= 1

        return res


# 延伸问题，如果每艘船人数不受限制
# class Solution:
#     def numRescueBoats(self, people: List[int], limit: int) -> int:
#         """
#         Obviously n boats can save everyone.
#         We then want to group people so that the sum of their weights comes as close to limit as possible.
#
#         1. You can remove everyone with weight = limit
#         2. You want to pair the heaviest people remaining with the lightest
#         """
#         ans = 0
#
#         # Copy people, sorted it, then reverse it
#         weights = sorted(people[:])[::-1]
#
#         # Two pointers, put the fat person (i) in the boat first.
#         i, j = (0, len(weights) - 1)
#         while i <= j:
#             boat = weights[i]
#             i += 1
#
#             # Boat holds only two people
#             # if i <= j and boat + weights[j] <= limit:
#             #     boat += weights[j]
#             #     j -= 1
#
#             # No limit to the number of people
#             while i <= j and boat + weights[j] <= limit:
#                 boat += weights[j]
#                 j -= 1
#             ans += 1
#
#         return ans


s = Solution()
print(s.numRescueBoats(people=[1, 2], limit=3))
print(s.numRescueBoats(people=[3, 2, 2, 1], limit=3))
print(s.numRescueBoats(people=[3, 5, 3, 4], limit=5))
