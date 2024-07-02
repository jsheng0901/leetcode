from math import ceil


class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        """
        Time O(2 * (num_rows * num_cols) + n)
        Space O(num_rows * num_cols)
        基本上就是翻译题目的意思，构建Z字形的走位string，填写进matrix，然后再每一行一行的加入结果。最复杂的是计算多少个column，这里需要
        把一个Z字想象成一个section，然后找有多少个这样的section，然后每个section需要的column刚好是row - 1，详细见注释
        """
        # 特殊情况，直接返回结果
        if num_rows == 1:
            return s

        n = len(s)
        # 计算有多少个section，这里中间Z的部分是 num_rows - 2，Z字竖的部分是 num_rows，取ceiling
        sections = ceil(n / (2 * num_rows - 2.0))
        # 每个section需要的column刚好是num_rows - 1
        num_cols = sections * (num_rows - 1)

        # 构建matrix
        matrix = [[" "] * num_cols for _ in range(num_rows)]

        curr_row, curr_col = 0, 0
        curr_string_index = 0
        # Iterate in zig_zag pattern on matrix and fill it with string characters.
        while curr_string_index < n:
            # Move down.
            while curr_row < num_rows and curr_string_index < n:
                matrix[curr_row][curr_col] = s[curr_string_index]
                curr_row += 1
                curr_string_index += 1

            curr_row -= 2
            curr_col += 1

            # Move up (with moving right also).
            while curr_row > 0 and curr_col < num_cols and curr_string_index < n:
                matrix[curr_row][curr_col] = s[curr_string_index]
                curr_row -= 1
                curr_col += 1
                curr_string_index += 1

        # 重新按顺序遍历matrix构建结果
        res = ''
        for i in range(num_rows):
            for j in range(num_cols):
                c = matrix[i][j]
                if c != " ":
                    res += c

        return res


class Solution2:
    def convert(self, s: str, num_rows: int) -> str:
        """
        Time O(n)
        Space O(n)
        第二种思路其实我们并不需要记录column，只需要知道每个字符对应在哪行就行，一直叠加进那一行。
        """
        if num_rows == 1:
            return s

        # 对每一行构建一个空string
        rows = [""] * num_rows
        # 是否要反过来走
        backward = True
        # 初始index对应的行
        index = 0
        # 遍历每个字符找到当前字符对应的行
        for char in s:
            # 当前字符对应的行进行叠加
            rows[index] += char
            # 如果是第一行或者最后一行
            if index == 0 or index == num_rows - 1:
                # 调转方向
                backward = not backward
            # 如果是往回走，行 -1
            if backward:
                index -= 1
            # 如果是往前走，行 +1
            else:
                index += 1

        return "".join(rows)


class Solution3:
    def convert(self, s: str, num_rows: int) -> str:
        """
        Time O(n)
        Space O(1)
        第三种思路有点数学找规律的意思，每一步跳跃到下一步其实有一定的规律。详细见注释。
        """
        if num_rows == 1:
            return s

        answer = ""
        n = len(s)
        # 计算有多少个字符在一个section里面
        chars_in_section = 2 * num_rows - 2

        # 遍历有多少个row
        for curr_row in range(num_rows):
            # 初始化index从第一行开始
            index = curr_row
            # 先找到第一行对应的所有index
            while index < n:
                answer += s[index]

                # If curr_row is not the first or last row,
                # then we have to add one more character of current section.
                if curr_row != 0 and curr_row != num_rows - 1:
                    # 两个index直接有多少个字符相隔
                    chars_in_between = chars_in_section - 2 * curr_row
                    # 下一步index对应的位置
                    second_index = index + chars_in_between

                    if second_index < n:
                        answer += s[second_index]
                # Jump to same row's first character of next section.
                index += chars_in_section

        return answer


s = Solution2()
print(s.convert(s="PAYPALISHIRING", num_rows=3))
print(s.convert(s="PAYPALISHIRING", num_rows=4))
print(s.convert(s="A", num_rows=1))
print(s.convert(s="A", num_rows=2))
print(s.convert(s="AB", num_rows=1))
print(s.convert(s="ABC", num_rows=1))
