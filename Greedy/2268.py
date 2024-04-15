from collections import defaultdict, Counter


class Solution1:
    def sort_by_freq(self, s):
        freq = Counter(s)
        sort_s = ""
        for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True):
            sort_s += k * v

        return sort_s

    def minimumKeypresses(self, s: str) -> int:
        """
        Time O(n * log(n) + n)
        Space O(n)
        先按照出现的频率进行sort，因为出现的越多，我们希望排在前面这样可以少按次数。之后记录每个按钮对应的字符和字符对应的按钮，
        先把前9个数都排一遍，如果前9个数排满了就排第二遍。贪心的思想，局部最小达到整体最小。
        """
        # 按照出现的频率从高到低排一遍
        s = self.sort_by_freq(s)
        num_to_char = defaultdict(list)
        char_to_num = defaultdict(int)
        res = 0
        num = 1
        # 遍历新的string
        for v in s:
            # 如果出现过就直接记录次数，不用叠加当前number
            if v in char_to_num:
                pre_num = char_to_num[v]
                res += len(num_to_char[pre_num])
                continue
            # 如果是转折点记录为9
            if num % 9 == 0:
                num = 9
            # 其它的取余数
            else:
                num %= 9
            # 记录进数字对字符
            num_to_char[num].append(v)
            # 反向记录，方便出现重复的字符的时候直接提取按钮次数
            char_to_num[v] = num
            # 累加
            res += len(num_to_char[num])
            # 叠加数字
            num += 1

        return res


class Solution2:
    def minimumKeypresses(self, s: str) -> int:
        """
        Time O(n * log(n) + n)
        Space O(n)
        其实我们并不需要记录数字和字符的关系，因为第一次填满后一点是按一次，第二次一定是按两次，我们只需要知道当前出现的频率和index即可。
        理论上第二种方法更快，因为不需要对字典进行list上面的记录，速度和空间更省。
        """
        # 记录出现的频率
        freq = Counter(s)
        res = 0
        count = 0
        # 从高到低遍历
        for i, v in enumerate(sorted(freq.values(), reverse=True)):
            # 如果当前余数是0，说明按一次，比如index = 0，按一次，index = 9 的时候已经是第二遍了，按两次
            if i % 9 == 0:
                count += 1
            # 出现的频率 * 按的次数 叠加进总次数
            res += count * v

        return res


s = Solution2()
print(s.minimumKeypresses(s="aaaaaaaabcdefgggghijkllllllllllmmmnoppponono"))
