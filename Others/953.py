class Solution:
    def isAlienSorted(self, words: [str], order: str) -> bool:
        """
        构建新的字典顺序，检验每一个词和下一个词的，每个单词，一一对应检测，如果不同，就check顺序，
        前一个词的顺序一定要比后一个词的小，如果大的话就结束return false，如果第一个不同的词没有顺序问题，则直接break返回true
        """
        order_map = {}
        for index, val in enumerate(order):
            order_map[val] = index

        for i in range(len(words) - 1):

            for j in range(len(words[i])):
                # If we do not find a mismatch letter between words[i] and words[i + 1],
                # we need to examine the case when words are like ("apple", "app").
                if j >= len(words[i + 1]):
                    return False

                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]:
                        return False
                    # if we find the first different character and they are sorted,
                    # then there's no need to check remaining letters
                    break

        return True
