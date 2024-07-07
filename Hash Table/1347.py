from collections import Counter


class Solution1:
    def minSteps(self, s: str, t: str) -> int:
        """
        Time O(n)
        Space O(n --> 26) --> O(1)
        先分别计算出两个string的频率，因为要达到异位词效果必须出现频率是一样的并且出现的字符也是一样的。这里三种情况
        1. 出现的频率在s里面大于t
        2. 出现的频率在s里面小于t
        3. 出现的频率在s里面不存在t
        对于1，2两个case其实一个case，我们只需要增加t里面的频率等同于减少t里面多出部分的频率，对于没出现过的词其实也是1的情况。
        """
        # 统计出现的频率
        s_freq = Counter(s)
        t_freq = Counter(t)

        res = 0

        for k, v in s_freq.items():
            # case1，s里面的频率大于t里面的频率
            if k in t_freq and v > t_freq[k]:
                # 需要改动的次数为他们的差值
                res += v - t_freq[k]
            # case3，出现的频率在s里面不存在t
            elif k not in t_freq:
                # 需要改动的次数为s里面的频率
                res += v

        return res


class Solution2:
    def minSteps(self, s: str, t: str) -> int:
        """
        Time O(n)
        Space O(n --> 26) --> O(1)
        一模一样的思路，只是用数组代替字典达到映射，这里有个技巧，存储s出现的频率 +1，存储t出现的频率 -1，这样我们只需要统计所有大于0的数即可
        """

        hash_arr = [0] * 26

        for i in range(len(s)):
            # 构建出现频率差值的map
            hash_arr[ord(s[i]) - 97] += 1
            hash_arr[ord(t[i]) - 97] -= 1

        res = 0

        for freq in hash_arr:
            # 对于负数也就是case2，我们不需要管，直接去0，对于正数也就是1，3我们累计差值
            res += max(0, freq)

        return res


s = Solution2()
print(s.minSteps(s="bab", t="aba"))
print(s.minSteps(s="leetcode", t="practice"))
print(s.minSteps(s="anagram", t="mangaar"))
