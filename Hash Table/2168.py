from collections import defaultdict


class Solution1:
    def check_valid(self, substring_encode):
        # check子串的每个字符的频率是否是一样的
        values = list(substring_encode.values())
        for i in range(1, len(values)):
            if values[i] != values[i - 1]:
                return False

        return True

    def equalDigitFrequency(self, s: str) -> int:
        """
        Time O(n^2 * m)
        Space O(n)
        找到所有的子串，然后每个检查一下是否是valid的条件，如果是则加入记录，同时计数 +1。这里有个小trick是，我们记录子串的频率的时候用hash，
        此时可以滚动hash，也就是后一个子串的hash可以由前一个得出，而不需要每次都重头hash整个子串，否则这样很费时间。
        """
        # 记录合理的substring
        valid_substring = set()
        count = 0
        for i in range(len(s)):
            # 对每个子串进行hash
            substring_encode = defaultdict(int)
            for j in range(i, len(s)):
                # 当前子串
                substring = s[i: j + 1]
                # 子串的频率 +1
                substring_encode[s[j]] += 1
                # 如果没有出现过才继续判断
                if substring not in valid_substring:
                    # 判断是否是符合条件的子串
                    is_valided = self.check_valid(substring_encode)
                    # 如果是，则加入记录，并计数 +1
                    if is_valided:
                        count += 1
                        valid_substring.add(substring)

        return count


class Solution2:
    def check_valid(self, substring_encode):
        # 拿到所有出现过的频率的set
        values = set(substring_encode.values())
        # 只有长度是1说明频率都一样
        return True if len(values) == 1 else False

    def equalDigitFrequency(self, s: str) -> int:
        """
        Time O(n^2 * m)
        Space O(n)
        和思路1一模一样的思路，就是检查是否符合条件的子串的时候，用set来检查。
        """
        # 同思路1
        valid_substring = set()
        count = 0
        for i in range(len(s)):
            substring_encode = defaultdict(int)
            for j in range(i, len(s)):
                substring = s[i: j + 1]
                substring_encode[s[j]] += 1
                if substring not in valid_substring:
                    is_valided = self.check_valid(substring_encode)
                    if is_valided:
                        count += 1
                        valid_substring.add(substring)

        return count


class Solution3:
    def equalDigitFrequency(self, s: str) -> int:
        """
        Time O(n^2)
        Space O(n)
        整体思路还是一样的，但是检查是否是合理的子串的时候，我们可以并不需要遍历每个频率，可以用一点数学的trick思路，一个数组里面所有数出现的
        频率一样，一定满足 独特数子的个数 * 最大的频率 = 数组的长度 --> max_freq * unique == j - i + 1。
        """
        # 其它整体思路都一样
        valid_substring = set()
        count = 0
        for i in range(len(s)):
            substring_encode = defaultdict(int)
            # 记录有多少个数值不一样的数
            unique_digit = 0
            # 记录最大频率
            max_freq = 0
            for j in range(i, len(s)):
                substring = s[i: j + 1]
                # 如果没有出现过，计数 +1
                if s[j] not in substring_encode:
                    unique_digit += 1
                substring_encode[s[j]] += 1
                # 更新子串里面最大频率
                max_freq = max(max_freq, substring_encode[s[j]])
                if substring not in valid_substring:
                    # 如果满足每个子串里面的数出现的频率都一样，则一定符合一下数学公式
                    if max_freq * unique_digit == j - i + 1:
                        count += 1
                        valid_substring.add(substring)

        return count


s = Solution3()
print(s.equalDigitFrequency(s="1212"))
