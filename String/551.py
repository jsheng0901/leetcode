class Solution:
    def checkRecord(self, s: str) -> bool:
        """
        Time O(n)
        Space O(1)
        遍历一次string， 统计absent的次数，同时统计最长连续late的长度，最后判断一下是否同时满足条件。
        """
        absent = 0
        max_late = 0
        cur_late = 0

        for ch in s:
            # 如果是absent，计数 +1
            if ch == 'A':
                absent += 1
                # 同时记得要初始化当前late的次数
                cur_late = 0
            elif ch == 'L':
                # late计数 +1
                cur_late += 1
                # 记录最长连续late次数
                max_late = max(max_late, cur_late)
            elif ch == 'P':
                # 同时记得要初始化当前late的次数
                cur_late = 0

        # 同时满足两个条件
        return absent < 2 and max_late < 3


s = Solution()
print(s.checkRecord(s="PPALLP"))
print(s.checkRecord(s="PPALLL"))
