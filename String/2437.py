class Solution:
    def countTime(self, time: str) -> int:
        """
        Time O(1)
        Space O(1)
        非常直白的题目，直接按照题意进行if-else组合，hour的组合 * second的组合就是所有的组合情况。
        """
        h, s = time.split(":")
        hour_res = 1
        second_res = 1

        # hour 的组合情况
        h_0, h_1 = h[0], h[1]
        if h_0 == "?":
            # 两个都是问号
            if h_1 == "?":
                hour_res = 24
            # 一个问号，第二个三以内
            elif int(h_1) <= 3:
                hour_res = 3
            # 第二个大于三，只能是0，1 因为没有24
            else:
                hour_res = 2
        # 第二个是问号，第一个不是
        elif h_1 == "?":
            if int(h_0) == 0 or int(h_0) == 1:
                hour_res = 10
            elif int(h_0) == 2:
                hour_res = 4

        # second 的组合情况
        s_0, s_1 = s[0], s[1]
        if s_0 == "?":
            # 两个都是问号，可以是60种情况
            if s_1 == "?":
                second_res = 60
            # 第二个不是问号，0 - 5 都可以
            else:
                second_res = 6
        # 第二个是问号，0 - 9 都可以
        elif s_1 == "?":
            second_res = 10

        return hour_res * second_res


s = Solution()
print(s.countTime(time="?5:00"))
