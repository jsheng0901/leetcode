from typing import List


class Solution1:
    def check_palindrome(self, number):
        left = 0
        right = len(number) - 1

        while left < right:
            if number[left] != number[right]:
                return False
            left += 1
            right -= 1

        return True

    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        """
        Time O(n^2)
        Space O(1)
        很直接的思路，从最小的base开始叠加，check每一个数是不是回文数字，如果是则记录找到的个数，对应query的话，加入结果，如果不对应，
        则继续叠加，此方法超时，因为比如100是base，则找到90 query时需要叠加到999，每个数还需要判断是不是回文，很费时。
        """
        # base起始点
        start = str(10 ** (intLength - 1))
        count = 0
        index = 0
        res = []

        # 直到所有query走完
        while index < len(queries):
            # check是否是回文
            if self.check_palindrome(start):
                # 记录找到一个回文
                count += 1
                # 当等于当前query的index的时候
                if count == index:
                    # 记录进结果
                    res.append(int(start))
                    # 下一个query
                    index += 1
            # 叠加
            start = str(int(start) + 1)

        return res


class Solution2:
    def get_palindrome(self, length, num):
        # index start from 0，比如 10 表示第一小的回文
        # 比如 num = 1 我们需要找到最小的回文，则 index 为 0
        # 比如 num = 2 我们需要找到第二最小的回文, 则 index 为 1
        index = num - 1
        # 如果是偶数
        if length % 2 == 0:
            # 当前base情况，比如1000应该是10
            cur = 10 ** ((length // 2) - 1)
            # 当前最长长度，比如10不能到100的长度，否则整体长度超过length限制
            max_length = len(str(cur))
            # 当前query对应的index数
            cur += index
            # 超过说明不存在，返回 -1
            if len(str(cur)) > max_length:
                return -1
            # 翻转base然后拼接起来
            else:
                cur = str(cur)
                # 记得翻转
                cur = cur + cur[::-1]
        # 如果是奇数，比如100，我们取10
        else:
            # 同偶数，只是base的情况我们不需要 -1
            cur = 10 ** (length // 2)
            max_length = len(str(cur))
            cur += index

            if len(str(cur)) > max_length:
                return -1
            else:
                # 当前base拼接base的前面到最后一位的数，比如 124 + 21 = 12421
                cur = str(cur)
                tmp = cur[:-1]
                # 记得翻转
                cur = cur + tmp[::-1]

        return int(cur)

    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        """
        Time O(n)
        Space O(1)
        只考虑一半的回文
        比如 len  = 4 我们只考虑前两位
            half: 10, 11, 12, 13, 14, ..., 19, 20,
            full: 1001, 1111, 1221, 1331, ...
        比如 len  = 5 我们只考虑前三位
            half: 100, 101, 102, ...
            full: 10001, 10101, 10201, ...
        数学思路，回文只需要前半段叠加即可。详细见注释。
        """
        res = []

        for i in queries:
            res.append(self.get_palindrome(intLength, i))

        return res


s = Solution2()
print(s.kthPalindrome(queries=[1, 2, 3, 4, 5, 90], intLength=3))
