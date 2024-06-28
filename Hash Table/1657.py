from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        Time O(n)
        Space O(n --> 26) --> O(1)
        此题换句话来说就是，两个word里面出现的字符必须一样，出现的频率必须一样，但每个词对应的频率的字符不一定要一致。
        统计每个词对应的频率，计算是否他们的key一样，或者他们的频率一样，频率这里必须先sort一下才能判断，不然移动数组判断很耗时。
        这里虽然有sort因为最多就26个字符，所以sort的时间复杂度是O(26 * log(26)) --> O(1)。
        """
        # 统计每个词小出现的频率
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        # 得到对应的每个词的key和出现的频率
        key1 = freq1.keys()
        key2 = freq2.keys()
        # 频率需要sort一下先，方便判断
        val1 = sorted(list(freq1.values()))
        val2 = sorted(list(freq2.values()))

        # 如果key不一样，直接返回false
        if key1 != key2:
            return False
        # 如果key一样继续判断是否出现的频率是一样的
        else:
            return val1 == val2


s = Solution()
print(s.closeStrings(word1="abc", word2="bca"))
print(s.closeStrings(word1="a", word2="aa"))
print(s.closeStrings(word1="cabbba", word2="abbccc"))
