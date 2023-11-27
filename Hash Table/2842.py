from collections import Counter
from math import comb


class Solution:
    def __init__(self):
        self.beatuy = float('-inf')
        self.count = 0

    def backtracking(self, s, start, k, chr_to_freq, cur_sum, cur_path):
        # 当前组合里面已经有k个数字，可以结束遍历，开始判断
        if len(cur_path) == k:
            # 如果当前乘积更大，更新结果
            if cur_sum > self.beatuy:
                self.beatuy = cur_sum
                self.count = 1
            # 如果相等，次数累加
            elif cur_sum == self.beatuy:
                self.count += 1
            # 结束遍历
            return

        # 遍历下一个字符
        for i in range(start, len(s)):
            # 保证没有重复的字符出现在子序列里面
            if s[i] not in cur_path:
                # 当前path
                cur_path.add(s[i])
                # 当前总数
                cur_sum += chr_to_freq[s[i]]
                self.backtracking(s, i + 1, k, chr_to_freq, cur_sum, cur_path)
                # 离开时候记得回溯
                cur_sum -= chr_to_freq[s[i]]
                cur_path.remove(s[i])

        return

    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        """
        Time O(n + C(n,k))
        Space O(n)
        找到单词对应的频率，之后找出所有可能的k个情况下的不重复的组合，算出最大乘积的情况，并统计出现的次数。
        此方法非常非常费时，因为回溯需要走遍所有情况。测试数据超时。
        """
        chr_to_freq = Counter(s)
        self.backtracking(s, 0, k, chr_to_freq, 0, set())
        return self.count


class Solution2:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        """
        Time O(n)
        Space O(n)
        此题贪心思路 + 数学思路，我们需要的是计算最大的k长度的子序列的乘积，那么我们可以先把frequency算出来，然后一个一个放进子序列，
        直到放满k个为止，并且我们需要知道有多少个这个子序列，只需要一直累乘unique字符出现的frequency就行。
        注意要一直除以mod，不然很容易超memory。
        """
        # 定义mod
        mod = 10 ** 9 + 7
        # 计算出每个字符出现的频率
        chr_to_freq = Counter(s)
        # 如果unique字符的个数小于k说明我们构不成合理的子序列，返回0
        if len(chr_to_freq) < k:
            return 0
        # 计算出每个频率出现的次数，这个才是我们需要放进结果的字符的顺序，次数多的先放，保证最后乘积最大
        freq_to_chr = Counter(chr_to_freq.values())

        res = 1
        # 遍历频率到次数的字典，这里需要sort一下写
        for key, val in dict(sorted(freq_to_chr.items(), reverse=True)).items():
            # 如果我们有的次数少于等于k，说明还需要继续添加字符，此频率下的字符先全部加进去
            if val <= k:
                # 结果是组合的效果，所以是累乘
                res = res * ((pow(key, val, mod)) % mod)
                # 更新剩下的k
                k -= val
            else:
                # 此时我们需要的k小于我们有的次数，说明要从次数里面选出k个，然后再乘以次数
                res = (res * comb(val, k) * pow(key, k, mod)) % mod
                # 可更新可不更新，因为走到这里一定所有k都已经用完了
                k -= val
                # 用完所有k，结束循环
                break

        # 记得最终结果也要除以mod
        return res % mod


s1 = Solution2()
print(s1.countKSubsequencesWithMaxBeauty(s="bcca", k=2))
s2 = Solution2()
print(s2.countKSubsequencesWithMaxBeauty(s="abbcd", k=4))
s3 = Solution2()
print(s3.countKSubsequencesWithMaxBeauty(s="elex", k=4))
s4 = Solution2()
print(s4.countKSubsequencesWithMaxBeauty(s="sdsidx", k=3))
s5 = Solution2()
print(s5.countKSubsequencesWithMaxBeauty(s="lelxul", k=1))
s6 = Solution2()
print(s6.countKSubsequencesWithMaxBeauty(s="qqwweerrttyyuuiiooppaassddffgghhjjkkllzzxxccvvbbnnmm", k=10))
