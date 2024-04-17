from typing import List


class Solution:
    def count_plates(self, s):
        # 计算有多少plates
        candle = 0
        total_plates = 0
        cur_plates = 0

        for i in range(len(s)):
            # 如果是candle，计数 +1
            if s[i] == "|":
                candle += 1
            # 如果是plate并且找到一个candle，则当前计数plate +1
            if s[i] == "*" and candle == 1:
                cur_plates += 1
            # 如果是plate并且找到两个candle，说明可以计入总数，并且更新当前plate数量
            if s[i] == "|" and candle == 2:
                total_plates += cur_plates
                candle -= 1
                cur_plates = 0

        return total_plates

    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        """
        Time O(q * n)
        Space O(n)
        对于每个query我们提取substring，然后计算substring里面有多少个plates。此方法会超时，
        因为每次提取substring我们都需要从新找一次有多少个plates，有大量的重复计算。
        """
        res = []
        # 遍历所有query，依次计算并添加进结果
        for query in queries:
            sub_s = s[query[0]: query[1] + 1]
            res.append(self.count_plates(sub_s))

        return res


class Solution2:
    def pre_sum(self, s):
        # 计算前缀和，pre_sum[i]表示从开始到以i下角标结束的字符内总共有多少个plates
        pre_sum = [0] * len(s)
        candle = 0
        left = 0

        for i in range(len(s)):
            # 如果是candle，计数器 +1
            if s[i] == "|":
                candle += 1
                # 如果找到一个candle，说明进如可能有plate的区间
                if candle == 1:
                    # 左指针更新 index
                    left = i
                    # 此时因为只有一个candle，依旧没有合理区间，当前前缀和等于前一个
                    pre_sum[i] = pre_sum[i - 1]
                # 如果找到两个candle，说明已经找到有plate的区间
                if candle == 2:
                    # 计数器更新
                    candle -= 1
                    # 前缀和等于前一个前缀和 + 两个指针直接有多少个plates
                    pre_sum[i] = pre_sum[i - 1] + i - left - 1
                    # 更新左指针
                    left = i
            # 如果是plate，则当前前缀和等于前一个
            else:
                pre_sum[i] = pre_sum[i - 1]

        return pre_sum

    def get_left(self, s):
        # 找到每个plate的最左边的candle index
        left_index = [-1] * len(s)
        # 初始化candle index指针为 -1
        left = -1
        for i in range(len(s)):
            # 如果是plates，当前左边candle等于左candle指针
            if s[i] == "*":
                left_index[i] = left
            # 如果是candle，更新当前左candle的指针，并赋值
            elif s[i] == "|":
                left = i
                left_index[i] = i

        return left_index

    def get_right(self, s):
        # 找到每个plate的最右边的candle index
        # 同理找左边的 index，只是需要反向遍历
        right_index = [-1] * len(s)
        right = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "*":
                right_index[i] = right
            elif s[i] == "|":
                right = i
                right_index[i] = i

        return right_index

    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        """
        Time O(n)
        Space O(n)
        先找到每个plate的最左边的candle index，再找到每个plate的最右边的candle index，然后我们真正找plates的区间则是
        [right_index[query[0]], left_index[query[1]]]。再计算出前缀和，此时只需要pre_sum[left] - pre_sum[right]即可算出
        此区间总共有多少合理的plates。此方法只需要遍历三此string即可，不需要每次query都遍历一次string。
        """
        # 拿到左index，右index，和前缀和
        res = []
        pre_sum = self.pre_sum(s)
        left_index = self.get_left(s)
        right_index = self.get_right(s)
        # 遍历query
        for query in queries:
            # 实际左candle，和实际右candle
            left = right_index[query[0]]
            right = left_index[query[1]]
            # 情况1，一遍没有合理的candle，则说明没有合理的plates，记录 0
            if left == -1 or right == -1:
                res.append(0)
            # 情况2，query在我们左右candle区间里面，说明此时query里面没有任何candle，记录 0，
            # 这里只会有一种情况，当在candle里面的时候，及left > right
            elif right < query[0] and left > query[1]:
                res.append(0)
            # 情况3，计算真正query的区间情况，利用前缀和，这里只有 right > left，因为如果 left > right，则说明一定是上面第二种情况
            else:
                res.append(pre_sum[right] - pre_sum[left])

        return res


class Solution3:
    def left_bound(self, arr, target):
        # 查找大于等于target值的最小的左边界，标准写法
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] < target:
                left = mid + 1
            elif arr[mid] == target:
                right = mid - 1
            elif arr[mid] > target:
                right = mid - 1

        return left

    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        """
        Time O(q * log(candle))
        Space O(candle)
        二分法查找每个query的最左边的candle和最右边的candle，计算这个candle区间里面有多少个plate。详细见注释。
        在一个递增区间内，找到一个大于或者等于target值的数值，一定可以用二分法。
        """
        # 拿到所有candle的index，因为要查找最左边界
        candles = [i for i, c in enumerate(s) if c == "|"]

        ans = []
        for a, b in queries:
            # 找到最左边界和最右边界的index，这里注意，我们查找的是二分法的最左边界，所以candle的右边界需要减1
            l, r = self.left_bound(candles, a), self.left_bound(candles, b + 1) - 1
            # 找到index后，candles[r] - candles[l] - 1 找到两个candle中间如果没有任何别的candle的话有多少个plate
            # r - l - 1 计算出两个candle中间有多少个其它的candle，也就是不是plate的个数，相减计算出总共的plate个数
            ans.append((candles[r] - candles[l] - 1) - (r - l - 1) if l < r else 0)

        return ans


s = Solution3()
print(s.platesBetweenCandles(s="**|**|***|", queries=[[2, 5], [5, 9]]))
print(s.platesBetweenCandles(s="***|**|*****|**||**|*", queries=[[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]))
