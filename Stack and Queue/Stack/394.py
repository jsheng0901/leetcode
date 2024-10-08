class Solution:
    def decodeString(self, s: str) -> str:
        """
        Time O(n) loop once
        Space O(n) stack to save each s
        用stack来写，遇到闭合就开始判断提取字母，直到找到开合，然后找到前面的所有数字，然后相乘后加入stack，继续loop
        """
        stack = []

        for i in range(len(s)):
            if s[i] != ']':
                # 如果不是闭合符号则直接加入stack
                stack.append(s[i])
            else:
                # 提取所有[]里面的字母
                sub_s = ''
                while stack[-1] != '[':
                    # 注意此处要先加弹出的字母再加之前的value，否则字母顺序会反过来
                    sub_s = stack.pop() + sub_s
                # 弹出开合符号
                stack.pop()
                # 提取所有[]前面的数字
                sub_number = ''
                while stack and stack[-1].isnumeric():
                    sub_number = stack.pop() + sub_number
                # 解析字母和数字
                decode = sub_s * int(sub_number)
                # 继续加入stack，继续loop
                stack.append(decode)

        result = "".join(stack)

        return result


s = Solution()
print(s.decodeString(s="3[a]2[bc]"))
print(s.decodeString(s="3[a2[c]]"))
print(s.decodeString(s="10[leet]"))
