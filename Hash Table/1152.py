from collections import defaultdict, Counter
from typing import List


class Solution1:
    def __init__(self):
        self.res = []

    def backtracking(self, arr, start_index, path):
        if len(path) == 3:
            self.res.append(tuple(path))

        for i in range(start_index, len(arr)):
            path.append(arr[i])
            self.backtracking(arr, i + 1, path)
            path.pop()

        return

    def mostVisitedPattern(self, username: [str], timestamp: [int], website: [str]) -> [str]:

        hash_map = {}
        patter = []
        current_user = username[0]
        max_patter = float('-inf')
        time = []
        for i in range(len(username)):
            if username[i] == current_user:
                patter.append(website[i])
                time.append(timestamp[i])
            if username[i] != current_user or i == len(username) - 1:
                patter = [x for _, x in sorted(zip(time, patter))]
                if len(patter) == 3:
                    if tuple(patter) in hash_map:
                        hash_map[tuple(patter)] += 1
                    else:
                        hash_map[tuple(patter)] = 1
                    max_patter = max(max_patter, hash_map[tuple(patter)])
                if len(patter) > 3:
                    self.backtracking(patter, 0, [])
                    for j in self.res:
                        if j in hash_map:
                            hash_map[j] += 1
                        else:
                            hash_map[j] = 1
                        max_patter = max(max_patter, hash_map[j])
                    self.res = []
                patter = []
                time = []
                current_user = username[i]
                patter.append(website[i])
                time.append(timestamp[i])
        ans = []
        for k, v in hash_map.items():
            if v == max_patter:
                ans.append(k)

        if len(ans) > 1:
            return list(sorted(ans)[0])
        else:
            return list(ans[0])


class Solution2:
    def mostVisitedPattern(self, username: [str], timestamp: [int], website: [str]) -> [str]:
        """
        Time O(n * log(n) + n^3 + n)
        Space O(n)
        """

        # Interviewer may ask you to implement itertools.Combinations
        # This is the specializaton where r = 3
        def combinations(l: list):
            for a in range(0, len(l) - 2):
                for b in range(a + 1, len(l) - 1):
                    for c in range(b + 1, len(l)):
                        yield (l[a], l[b], l[c])

        # Stage 1: O(nLogN) time, O(N) space
        # Sort the entire input stream in nLogN time, N space
        # Then append to a hash map in O(N) time (append O(1) * N entries)
        web_list_for_user = defaultdict(list)  # key = user, val = list[websites]
        for u, t, w in sorted(zip(username, timestamp, website)):
            web_list_for_user[u].append(w)

        # Stage 2: Combinations is O(n³)
        # Building the set is O(1) in both time and space per operation,
        # but applied O(n³) times. Counter also O(1) but applied O(n³) times
        freq_for_3seq = Counter()
        for web_list in web_list_for_user.values():
            freq_for_3seq.update(set(combinations(web_list)))

        # O(N) on the combinations, O(n³) on the input, O(1 space)
        return min(freq_for_3seq, key=lambda x: (-freq_for_3seq[x], x))


class Solution3:
    def __init__(self):
        self.distinct_pattern = set()

    def backtracking(self, web_list, path, start_index):
        # 回溯标准模板，找所有出现的组合情况
        if len(path) == 3:
            pattern = tuple(path)
            self.distinct_pattern.add(pattern)
            return

        # 不能往回找，只能按顺序组合
        for i in range(start_index, len(web_list)):
            path.append(web_list[i])
            self.backtracking(web_list, path, i + 1)
            path.pop()

        return

    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        """
        Time O(n * log(n) + n^3 + n)
        Space O(n)
        同思路2，先把用户到访问的网站建立起hash map，再对所有访问的网站找出按顺序来的所有三元素组合，再统计每个元素出现的频率，最后找到
        出现频率最高的那个元素。
        """
        # 用户到所有访问网站的关系，注意这里要先sort一下对timestamp，因为pattern的顺序和访问网站的时间顺序有关系
        user_to_web_list = defaultdict(list)
        for u, t, w in sorted(zip(username, timestamp, website)):
            user_to_web_list[u].append(w)

        # 统计每个访问的pattern的出现频率
        freq_for_web_list = defaultdict(int)
        # 统计出现频率最高的次数
        max_freq = float('-inf')
        # 对每个用户访问的网站列表进行组合搜索
        for web_list in user_to_web_list.values():
            # 每次组合统计unique value pattern
            self.distinct_pattern = set()
            # 回溯找到所有组合情况
            self.backtracking(web_list, [], 0)
            # 统计每个pattern出现的频率，并记录最高频率
            for pattern in self.distinct_pattern:
                freq_for_web_list[pattern] += 1
                max_freq = max(max_freq, freq_for_web_list[pattern])

        # 找到最高频率出现的pattern
        max_freq_pattern = []
        for k, v in freq_for_web_list.items():
            if v == max_freq:
                max_freq_pattern.append(k)

        # 返回最高频率出现中按照字母顺序排序最小的那个pattern
        return list(sorted(max_freq_pattern)[0])


s = Solution3()
print(s.mostVisitedPattern(username=["ua", "ua", "ua", "ub", "ub", "ub"], timestamp=[1, 2, 3, 4, 5, 6],
                           website=["a", "b", "a", "a", "b", "c"]))
print(s.mostVisitedPattern(username=["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"],
                           timestamp=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                           website=["home", "about", "career", "home", "cart", "maps", "home", "home", "about",
                                    "career"]))
print(s.mostVisitedPattern(username=["h", "eiy", "cq", "h", "cq", "txldsscx", "cq", "txldsscx", "h", "cq", "cq"],
                           timestamp=[527896567, 334462937, 517687281, 134127993, 859112386, 159548699, 51100299,
                                      444082139, 926837079, 317455832, 411747930],
                           website=["hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi",
                                    "hibympufi", "hibympufi", "yljmntrclw", "hibympufi", "yljmntrclw"]))
