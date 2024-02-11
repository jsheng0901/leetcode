from typing import List


class Solution1:
    def decoder(self, code):
        # decode成list
        value = code[0]
        freq = code[1]

        return [value] * freq

    def encoder(self, code):
        # encode回来
        count = 1
        res = []
        for i in range(len(code) - 1):
            if code[i] == code[i + 1]:
                count += 1
            else:
                res.append([code[i], count])
                count = 1

        if count > 0:
            res.append([code[-1], count])

        return res

    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        """
        Time O(m + n + 2 * l)
        Space O(m + n + l)
        直接按照题目的意思一步一步的implement。先decode转化成等长的list，然后算出乘积，然后再转换回来。不过虽然是O(n)的情况，但是TLE。
        """
        decoded1 = []
        decoded2 = []
        # 转化成list
        for code in encoded1:
            decoded1 = decoded1 + self.decoder(code)

        for code in encoded2:
            decoded2 = decoded2 + self.decoder(code)
        # 计算乘积
        tmp_code = []
        for i in range(len(decoded1)):
            tmp_code.append(decoded1[i] * decoded2[i])
        # 转化回encode
        return self.encoder(tmp_code)


class Solution2:
    def decoder(self, code):
        value = code[0]
        freq = code[1]

        return [value] * freq

    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        """
        Time O(m + n + l)
        Space O(m + n + l)
        同样的思路，就是把encode，计算product和decode步骤合在一起写。
        不过还是TLE，主要是因为无论如何都要遍历整个数组并且遍历整个product结果。
        """
        i = 0
        j = 0
        k = 0
        count = 0
        pre = None
        decoded1 = []
        decoded2 = []
        res = []
        while i < len(encoded1) or j < len(encoded2):
            if i < len(encoded1):
                decoded1 = decoded1 + self.decoder(encoded1[i])
            if j < len(encoded2):
                decoded2 = decoded2 + self.decoder(encoded2[j])
            while k < len(decoded1) and k < len(decoded2):
                cur = decoded1[k] * decoded2[k]
                if pre and cur != pre:
                    res.append([pre, count])
                    count = 1
                else:
                    count += 1
                pre = cur
                k += 1
            i += 1
            j += 1

        if count > 0:
            res.append([cur, count])

        return res


class Solution3:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        """
        Time O(m + n)
        Space O(1)
        整体思路还是一样的，区别在于计算product的地方，我们并不需要每个元素都遍历一遍计算product，因为对于相等的encode里面都是相同的数字，
        乘积都是一样的，计算一个之后再加上frequency就直接加入result，并不需要每个逐一遍历成一遍。
        """
        # 双指针
        i = 0
        j = 0
        # 当前code的频率和value
        freq1 = 0
        freq2 = 0
        val1 = 0
        val2 = 0
        res = []
        while i < len(encoded1) or j < len(encoded2):
            # 如果当前frequency已经用完了说明要到下一个encode了
            if freq1 == 0 and i < len(encoded1):
                val1, freq1 = encoded1[i]
            if freq2 == 0 and j < len(encoded2):
                val2, freq2 = encoded2[j]
            # 当前最少frequency
            cur_min_freq = min(freq1, freq2)
            # 当前乘积
            product = val1 * val2
            # 如果当前乘积和前一个一样，说明应该update之前的结果频率
            if res and res[-1][0] == product:
                res[-1][1] += cur_min_freq
            # 如果和前一个不一样，说明可以加入新的结果pair
            else:
                res.append([product, cur_min_freq])
            # 减掉用完的frequency
            freq1 -= cur_min_freq
            freq2 -= cur_min_freq
            # encode指针如果frequency用完了则需要进入下一个，如果没有用完说明当前frequency还有没用的数需要计算乘积
            i += 1 if freq1 == 0 else 0
            j += 1 if freq2 == 0 else 0

        return res


s = Solution3()
print(s.findRLEArray(encoded1=[[1, 3], [2, 3]], encoded2=[[6, 3], [3, 3]]))
print(s.findRLEArray(encoded1=[[1, 1], [2, 1], [1, 1], [2, 1], [1, 1]],
                     encoded2=[[1, 1], [2, 1], [1, 1], [2, 1], [1, 1]]))
print(s.findRLEArray(encoded1=[[1, 3], [2, 1], [3, 2]], encoded2=[[2, 3], [3, 3]]))
