import operator
from collections import defaultdict


class Solution:
    """ O(n + m) time, O(n + m) space"""
    def mostCommonWord(self, paragraph: str, banned: [str]) -> str:
        # 1). replace the punctuations with spaces,
        #      and put all letters in lower case
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

        # 2). split the string into words
        words = normalized_str.split()

        word_count = defaultdict(int)
        banned_words = set(banned)

        # 3). count the appearance of each word, excluding the banned words
        for word in words:
            if word not in banned_words:
                word_count[word] += 1

        # 4). return the word with the highest frequency
        return max(word_count.items(), key=operator.itemgetter(1))[0]