from typing import List


class Solution1:
    def __init__(self):
        # 初始化全局变量存储结果，此处用set因为可能会有好几种一模一样的移除后的结果
        self.result = set()
        self.min_removed = float('inf')

    def backtracking(self, s, start_index, left_count, right_count, path, rem_count):
        # 递归终止条件
        if start_index == len(s):
            # 走到最后一个字符并且左右括号数量相等
            if left_count == right_count:
                # 如果移除括号数量小于等于当前最小值，进入判断
                if rem_count <= self.min_removed:
                    # string在Python里面是immutable的，所以list转化成string后不用担心list之后被改变
                    path_str = "".join(path)
                    # 如果当前移除数量更小，忽视之前所有结果，初始化result和min_removed变量
                    if rem_count < self.min_removed:
                        self.result = set()
                        self.min_removed = rem_count
                    # 加入结果进set
                    self.result.add(path_str)

        # 当前字符
        cur_c = s[start_index]
        # 第一种情况：如果当前字符不是括号，直接加入进path并且递归进下一个
        if cur_c != '(' and cur_c != ')':
            path.append(cur_c)
            self.backtracking(s, start_index + 1, left_count, right_count, path, rem_count)
            # 注意递归结束后要弹出之前结果，因为path是list在Python里面会被后续操作改动
            path.pop()
        else:
            # 第二种情况第一种子情况：如果当前字符并且不加入，不加入进path直接递归进下一个
            self.backtracking(s, start_index + 1, left_count, right_count, path, rem_count + 1)
            # 第二种情况第二种子情况：如果当前字符并且加入，加入进path并且递归进下一个
            path.append(cur_c)
            # 如果是左括号，则左括号计数器 +1
            if s[start_index] == "(":
                self.backtracking(s, start_index + 1, left_count + 1, right_count, path, rem_count)
            # 如果是右括号，则右括号计数器 +1，不过这里我们只会在左括号多于右括号的情况下进入递归
            elif s[start_index] == ")" and left_count > right_count:
                self.backtracking(s, start_index + 1, left_count, right_count + 1, path, rem_count)
            # 回溯弹出
            path.pop()

    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        Time O(2^n) worst case: n left ( need to be removed or not
        Space O(n) recursive stack to store n character in s
        回溯题型，对于每一个character，我们考虑两种大情况：
            1. character不是符号是字母，则直接加入path递归进入下一个字符
            2. character是符号不是字母，两种子情况：
                - 此符号不加入最终表达式，跳过此符合，直接递归进入下一个字符
                - 此符号加入最终表达式，则直接加入path递归进入下一个字符
        停止情况为，当我们走到最后一个character的时候，并且括号和右括号的个数相等的情况下，我们判断被移除的括号数量是不是最小的，
        如果是最小的情况下，则加入path的string形式进最终结果
        """

        self.backtracking(s, 0, 0, 0, [], 0)

        # 注意这里最终要set转化成list
        return list(self.result)


class Solution2:
    def __init__(self):
        self.result = {}
        self.min_removed = float('inf')

    def backtracking(self, s, start_index, left_count, right_count, path, left_rem, right_rem):
        # 递归终止条件
        if start_index == len(s):
            # 如果左右都满足了被移除，则说明此组合是合理的，直接加入结果
            if left_rem == 0 and right_rem == 0:
                path_str = "".join(path)
                self.result[path_str] = 1
        else:
            cur_c = s[start_index]
            # 如果当前字符需要被移除，则直接进入下一个递归并更新左右括号需要被移除的个数
            if (cur_c == '(' and left_rem > 0) or (cur_c == ')' and right_rem > 0):
                self.backtracking(s, start_index + 1, left_count, right_count, path, left_rem - (cur_c == "("),
                                  right_rem - (cur_c == ")"))   # 此处用一个判断来转化成0，1表示

            # 如果不需要被移除，加入path先
            path.append(cur_c)
            # 不属于括号，直接进入递归
            if cur_c != "(" and cur_c != ")":
                self.backtracking(s, start_index + 1, left_count, right_count, path, left_rem, right_rem)
            # 左括号，更新左括号计数变量
            elif cur_c == "(":
                self.backtracking(s, start_index + 1, left_count + 1, right_count, path, left_rem, right_rem)
            # 右括号，更新右括号计数变量，同上只有左括号数量大于右括号的时候才进递归
            elif cur_c == ")" and left_count > right_count:
                self.backtracking(s, start_index + 1, left_count, right_count + 1, path, left_rem, right_rem)
            path.pop()

    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        Time O(2^n) worst case: n left ( need to be removed or not
        Space O(n) recursive stack to store n character in s
        最差情况下时间复杂度一样，不过我们skip掉了找到所有移除情况下的合理的组合，相反我们需要的是找到最小移除状态下的所有组合，
        所以我们可以提前算出有多少左括号和右括号需要被移除在此情况下进入递归。
        """
        left, right = 0, 0
        # 找到需要被移除的左右括号的数量
        for c in s:
            if c == "(":
                left += 1
            elif c == ")" and left == 0:
                right += 1
            elif c == ")" and left > 0:
                left -= 1

        self.backtracking(s, 0, 0, 0, [], left, right)

        return list(self.result.keys())


class Solution3:
    def __init__(self):
        self.result = []

    def is_valid(self, s):
        count = 0
        for i in s:
            if i == '(':
                count += 1
            elif i == ')':
                count -= 1

            if count < 0:
                return False

        return count == 0

    def backtracking(self, s, start_index, left, right):
        # 如果需要被移除的括号都移除了并且此时string是合规的，则直接加入最终结果
        if left == 0 and right == 0 and self.is_valid(s):
            self.result.append(s)

        for i in range(start_index, len(s)):
            if i - 1 >= start_index and s[i] == s[i - 1]:       # jump repeat
                continue
            if right > 0 and s[i] == ')':                           # 删除右括号
                self.backtracking(s[:i] + s[i + 1:], i, left, right - 1)
            if left > 0 and s[i] == '(':                           # 删除左括号
                self.backtracking(s[:i] + s[i + 1:], i, left - 1, right)

    def removeInvalidParentheses(self, s: str) -> [str]:
        """
        Time O(2^n) worst case: n left ( need to be removed or not
        Space O(n) recursive stack to store n character in s

        用l和r记录不匹配的左括号数量和右括号数量
        然后从0位置开始递归，如果l == 0 and r == 0 并且做移除不合法括号处理后的字符串是合法的话，即isValid的话，
        就添加到结果集中
        在递归的时候，先移除右括号，再移除左括号，因为先移除右括号后能保障前面的序列prefix是合法的序列，然后再从后面的
        字符串中移除左括号，如果先移除左括号，后面的右括号不匹配的数量就会变多。
        遍历的时候，重复出现的左括号或者右括号，只删除最开头的那个就好了，所if s[i] == s[i-1]:continue，但是要求
         i-1 >= start
        如果s[i]是')'，如果r > 0说明有右括号不匹配，移除第i个位置的字符，向下递归，新的字符串就是s[:i] + s[i + 1:]，
        同时 r - 1
        如果s[i]是'('，如果l > 0说明有左括号不匹配，移除第i个位置的字符，向下递归，新的字符串就是s[:i] + s[i + 1:]
        同时 l - 1
        向下传的start = i，也就是说下面的处理就只处理第i位置开始的了，事实上由于当前会删一个字符，所以后面的字符会向前
        挪一个，一般来说应该是range(start+1,len(s))，但是由于第i个位置的字符删掉了，后面的字符向前挪了一位，所以向下
        的时候从start = i的位置处理其实就相当于原来的处理第start+1也就是i+1的位置的字符，所以是合理的，向后逐位处理
        所以整体的策略就是先检测出字符串中需要删除的左右括号的数量，然后逐个删除，直到l = r = 0，然后如果此时的s是合法的话
        就可以添加进结果中了。删除的时候从前向后，先删右括号再删左括号
        """
        left = 0
        right = 0
        for i in s:
            if i == '(':
                left += 1
            elif i == ')':
                if left == 0:
                    right += 1
                else:
                    left -= 1

        self.backtracking(s, 0, left, right)

        return self.result


s = Solution3()
print(s.removeInvalidParentheses(s=')('))
