from typing import List


class Solution1:
    def dp(self, word, words, start_index, memo):
        # dp的带备忘的写法，DFS的后续遍历写法
        # 如果切到最后，则说明成功，直接返回true
        if start_index == len(word):
            return True

        # 如果切分过，返回结果
        if memo[start_index] != -1:
            return memo[start_index]

        # 记录当前所有子树的结果，只要有一条合理的path即可
        sub_res = False
        for i in range(start_index, len(word)):
            # 当前切分的sub_string
            sub_string = word[start_index: i + 1]
            # 如果在字典里面，继续切分
            if sub_string in words:
                # 注意这里下一个起始点的位置
                # 返回只要有一个true则当前节点返回值就是true
                sub_res = sub_res or self.dp(word, words, i + 1, memo)

        # 记录进备忘录
        memo[start_index] = sub_res
        return sub_res

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        Time O(n * m + m^2 * n)  m -> max length of word,  n -> number of word
        Space O(m * n)
        每个词去切分判断是否可以由其它words里面的词组合成，所以这个题目就变成了判断一个word是否可以由其它给定的word组合成。
        dp带备忘录的写法这里，后续遍历，返回是否有可行的一条路径。这里有两个优化，一个是words转化成set，方便快速查找是否存在，另一个是
        这里至少要由两个词拼接成，所以word的长度至少要大于等于最短的两个词的长度和，否则直接跳过。详细见注释。
        """
        # 如果只有一个词，直接返回不可能
        if len(words) == 1:
            return []

        # 找到所有长度
        word_length = []
        for word in words:
            word_length.append(len(word))

        # 从小到大排序
        word_length.sort()
        # 计算出最短的拼接词的长度
        min_concatenate_length = word_length[0] + word_length[1]
        # 字典化整个words
        words_set = set(words)
        # 记录结果
        res = []
        for i in range(len(words)):
            # 当前需要判断的词
            cur_word = words[i]
            # 如果小于最短长度，则说明不可能是拼接词，跳过
            if len(cur_word) < min_concatenate_length:
                continue
            # dp 备忘录，记录每个切分点的状态是否可以组成
            cur_memo = [-1] * len(cur_word)
            # 这里注意一定要记得移除掉自己这个word，这里直接构建一次字典然后用remove，达到O(1)的速度
            words_set.remove(cur_word)
            # 这里再次注意，一定不要用这个方式移除，因为这样每次都要重新构建字典，重新构建字典是非常费时的，因为需要对每个词都去映射一次
            # 并且这里相当于每次判断都要对剩下的所有词进行一次映射，则每次都会多一个 O(m * n)，整体多一个 O(m * n^2)
            # words_set = set(words[:i] + words[i + 1:])
            # 开始dp标准判断，是否可以拼接成功
            if self.dp(cur_word, words_set, 0, cur_memo):
                res.append(cur_word)
            # 同理之前移除了要加回来，对于后续的词判断，用add，达到O(1)的速度
            words_set.add(cur_word)

        return res


class Solution2:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        Time O(n * m + m^2 * n)  m -> max length of word,  n -> number of word
        Space O(m * n)
        同思路一，这里用从前往后的dp的写法来实现，dp[i]的状态取决于 dp[j] 和 word[j:i]是否在字典里面。
        这里没有优化，也可以加一个长度判断更快。
        """
        dictionary = set(words)
        answer = []
        for word in words:
            length = len(word)
            dp = [False] * (length + 1)
            dp[0] = True

            for i in range(1, length + 1):
                for j in range((i == length) and 1 or 0, i):
                    if not dp[i]:
                        dp[i] = dp[j] and word[j:i] in dictionary
            if dp[length]:
                answer.append(word)
        return answer


s = Solution1()
print(s.findAllConcatenatedWordsInADict(words=["cat", "dog", "catdog"]))
