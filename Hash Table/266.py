from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """
        Time O(n)
        Space O(n -> 26 -> 1)
        统计出现的数字频率，统计奇数和偶数的个数，如果s是奇数则最多一个奇数频率可以出现，如果s是偶数则不能有奇数频率出现。
        """
        freq = Counter(s)

        num_even = 0
        num_odd = 0
        # 统计奇数偶数频率
        for k, v in freq.items():
            if v % 2 == 1:
                num_odd += 1
            else:
                num_even += 1

        # 如果是奇数长度
        if len(s) % 2 == 1:
            # 最多一个奇数
            if num_odd > 1:
                return False
        # 如果是偶数长度
        else:
            # 不能有奇数
            if num_odd > 0:
                return False

        return True


class Solution2:
    def canPermutePalindrome(self, s: str) -> bool:
        """
        Time O(n)
        Space O(1)
        判断方式更简单，因为偶数的余数一个一定是0，奇数最多一个也就是余数是1，则说明所有余数和最多等于1无论长度是奇数还是偶数。
        """
        freq = Counter(s)

        # 统计所有频率的余数
        r = [v % 2 for k, v in freq.items()]

        # 判断是否小于等于1
        return sum(r) <= 1


class Solution3:
    def canPermutePalindrome(self, s):
        """
        Time O(n)
        Space O(1)
        判断方式同上，这里用set来找配对的数，因为形成回文一定要配对，所有用set来计算配对的情况。
        """
        unpaired_chars = set()

        for char in s:
            # 如果没有出现过，加入set
            if char not in unpaired_chars:
                unpaired_chars.add(char)
            # 如果出现过，说明有一对配对出现，弹出set
            else:
                unpaired_chars.remove(char)

        return len(unpaired_chars) <= 1


s = Solution3()
print(s.canPermutePalindrome(s="carerac"))
print(s.canPermutePalindrome(s="code"))
