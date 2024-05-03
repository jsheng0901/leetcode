class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        """
        Time O(n)
        Space O(1)
        此题很巧妙，首先要知道对于不合规的括号组合只有两种情况，思路同678双指针贪心写法。
        第一 如果')' 的数量超过 '(' 从左到右任意时刻，
        第二 或者 '(' 的数量超过 ')' 的数量到最后，或者从右向左遍历的时候。
        我们遍历两次，每次用一个指针balance来记录左右括号的数量移动。这题有个trick就是对于没有lock的括号其实我们可以随意变动，也就是说
        可以是开也可以是比括号，那么类似万能括号都可以算作balance +1的情况。详细见注释。
        """
        n = len(s)

        if n % 2 != 0:
            return False

        balance = 0
        # 从左向右遍历对应情况1
        for i in range(n):
            # 如果是开括号或者是没有锁的万能括号 +1
            if locked[i] == '0' or s[i] == '(':
                balance += 1
            # 相反 -1
            else:
                balance -= 1

            # 不合规直接返回 false
            if balance < 0:
                return False

        balance = 0
        # 同上从右向左遍历对应情况2
        for i in range(n - 1, -1, -1):
            # 如果是闭括号或者是没有锁的万能括号 +1
            if locked[i] == '0' or s[i] == ')':
                balance += 1
            # 相反 -1
            else:
                balance -= 1
            # 不合规直接返回 false
            if balance < 0:
                return False

        return True


s = Solution()
print(s.canBeValid(s="))()))", locked="010100"))
print(s.canBeValid(s=")(", locked="00"))
print(s.canBeValid(s="((()(()()))()((()()))))()((()(()", locked="10111100100101001110100010001001"))
