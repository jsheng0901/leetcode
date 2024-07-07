class Solution1:
    def partitionString(self, s: str) -> int:
        """
        Time O(n)
        Space O(n --> 26)  --> O(1)
        贪心思路，如果要subarray个数最少那么就需要每个subarray的长度尽可能的长。我们直接遍历整个string，遇到之前出现过的就split，如果没有
        出现过就加入subarray，这里用set来表示subarray window，达到O(1)的速度查存在。
        """
        # 窗口初始化
        window = set()
        i = 0
        count = 1
        # 遍历string
        while i < len(s):

            # 当前字符
            c = s[i]
            # 往前走一步
            i += 1

            # 如果出现过说明要split了
            if c in window:
                # 记录 +1
                count += 1
                # 重新初始化窗口
                window = set()

            # 如果没有出现过，或者出现过，都需要加入窗口，区别只是是否要先初始化窗口
            window.add(c)

        return count


class Solution2:
    def partitionString(self, s: str) -> int:
        """
        Time O(n)
        Space O(n --> 26)  --> O(1)
        一模一样的思路，只是换成用数组来存储出现的数最后出现的index，如果在此出现的index大于subarray的起始index，说明说明要开始split了。
        """
        last_seen = [-1] * 26
        count = 1
        sub_string_starting = 0

        for i in range(len(s)):
            # 如果当前出现的index大于subarray起点，说明subarray里面有重复的字符了
            if last_seen[ord(s[i]) - ord('a')] >= sub_string_starting:
                count += 1
                sub_string_starting = i
            # 更新当前字符最后出现过的index
            last_seen[ord(s[i]) - ord('a')] = i

        return count


s = Solution1()
print(s.partitionString(s="abacaba"))
print(s.partitionString(s="ssssss"))
