class Solution:
    def get_variance(self, substring):
        freq_dict = defaultdict(int)
        for s in substring:
            freq_dict[s] += 1

        freq = freq_dict.values()
        return max(freq) - min(freq)

    def largestVariance(self, s: str) -> int:
        """
        Time O(n^2 * n)
        Space O(n)
        双指针遍历所有组合的substring，然后计算每个substring的最大variance，同时更新全局最大值。超时计算，太慢了特别是找variance的时候。
        """
        left, right = 0, 0
        max_variance = 0
        memo = {}
        while right <= len(s):
            left = 0
            while left < right:
                substring = s[left: right]
                if substring in memo:
                    variance = memo[substring]
                else:
                    variance = self.get_variance(substring)
                    memo[substring] = variance
                max_variance = max(max_variance, variance)
                left += 1
            right += 1

        return max_variance


from collections import defaultdict


class Solution2:
    def largestVariance(self, s: str) -> int:
        """
        Time O(n⋅k^2)   k -> distinct character in s
        Space O(k)  k -> distinct character in s
        Kadane's algorithm的变体应用，原始算法是计算在一个array里面找到连续的和最大的substring。
        这里我们变成找到variance最大的substring。Kadane算法需要O(n)的时间遍历一次string，对于每个pair我们需要遍历一次整个string。
        总共有k^2个pairs。这里需要注意的是最大的variance一定会有两个distinct value在substring里面，
        所以我们每次更新全局最大值和更新局部初始的时候需要确定当前substring里面一定有minor的character存在。详细见注释。
        """
        # 计算所有character出现的频率
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        # 全局变量记录最大variance
        global_max = 0
        # 构建所有可能的两两组合
        pairs = [(i, j) for j in set(s) for i in set(s)]
        # 遍历所有组合
        for pair in pairs:
            major = pair[0]
            minor = pair[1]
            # 如果相等variance一定为0所以不是最大的情况，直接跳过
            if major == minor:
                continue
            # 统计最大和最小的case下的数量
            cnt_major, cnt_minor = 0, 0
            # 记录还有多少minor的character
            remain_minor = freq[minor]
            # 遍历string
            for ch in s:
                # 遇到major
                if ch == major:
                    cnt_major += 1
                # 遇到minor
                elif ch == minor:
                    cnt_minor += 1
                    remain_minor -= 1
                # 如果有minor在当前的substring里面，更新全局变量，计算当前最大variance
                if cnt_minor:
                    global_max = max(global_max, cnt_major - cnt_minor)
                # 如果此时variance为负数，说明此时的substring一定不是最多情况，初始化计量，但是前提是剩下的substring里面一定要有minor
                # 不然就会出现剩下的substring只有一种character那么variance一定为0
                if cnt_major < cnt_minor and remain_minor > 0:
                    # 初始化计量，等同于Kadane里面初始化sum为0遇到负数的sum的时候
                    cnt_major, cnt_minor = 0, 0
        # 返回全局最大值
        return global_max


s = Solution2()
print(s.largestVariance(s="aababbb"))
print(s.largestVariance(s="abcde"))
