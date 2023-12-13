from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        Time O(n)
        Space O(n)
        遍历一次 order + s 即可，先计算s里面出现的频率，然后先把order里面出现过的在s里面的挑出来并组合起来。最后把s剩下的再加回去。
        """
        # 计算s里面出现的频率
        s_map = Counter(s)
        res = ""

        for i in range(len(order)):
            # 当前出现在order并且在s里面的字符
            char = order[i]
            if char in s_map:
                # 乘以出现频率加入结果
                res += char * s_map[char]
                # 记得用完此字符后要删除此key value，加速后面的遍历，因为后面只需要遍历不在order里面的字符
                s_map.pop(char)

        # 不在order里面的字符加入结果
        for key, value in s_map.items():
            res += key * value

        return res


s = Solution()
print(s.customSortString(order="kqep", s="pekeq"))
print(s.customSortString(order="hucw", s="utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzg"
                                         "ypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"))
