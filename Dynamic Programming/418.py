from typing import List


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        """
        Time O(row * col)
        Space O(row * col)
        遍历每个点，往里面放sentence，如果可以放进去符合要求就填满此区间，并且sentence指针走一步，如果走到底说明完成一个sentence。
        此方法会超时，特殊情况只有一个sentence，screen很大，则需要遍历整个screen。
        """
        screen = [["-"] * cols for _ in range(rows)]
        pointer = 0
        res = 0
        i = 0
        j = 0

        while i < rows:
            while j < cols:
                # 如果当前行没办法放进去整个词，跳一步
                if cols - j < len(sentence[pointer]):
                    j += 1
                    continue
                # 如果当前的前一个不是空格说明被填充过，跳一步
                if screen[i][j - 1] != "-":
                    j += 1
                    continue
                # 其它情况都是合理的，直接填充当前单词
                for p in range(len(sentence[pointer])):
                    screen[i][j] = sentence[pointer][p]
                    j += 1

                # 如果sentence用到了最后一个，说明完成了一此填充，结果 +1
                if pointer == len(sentence) - 1:
                    res += 1
                    pointer = 0
                else:
                    pointer += 1

            # 下一行，此处记得col指针j要归零
            i += 1
            j = 0

        return res


class Solution2:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        """
        Time O(row)
        Space O(1)
        换个角度思考，我们需要找到是有多少个合理的space在screen里面，合理的space除以sentence的长度就是我们能填充几次sentence的次数。
        """
        # 先计算整个sentence转化成string后的长度
        sentence_string = " ".join(sentence) + " "
        # 合理的space
        valid_space = 0
        for i in range(rows):
            # 当前合理的所有space
            valid_space += cols
            # 如果为空说明合理的space多了一个，这里我们采用余数，可以处理sentence大于space或者space大于sentence的两种情况
            if sentence_string[valid_space % len(sentence_string)] == " ":
                valid_space += 1
            else:
                # 递减合理的space，如果当前sentence全部放进去的时候不符合要求
                while valid_space > 0 and sentence_string[valid_space % len(sentence_string) - 1] != " ":
                    valid_space -= 1
        return valid_space // len(sentence_string)


s = Solution2()
print(s.wordsTyping(sentence=["hello", "world"], rows=2, cols=8))
