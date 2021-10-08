class Solution:
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


from collections import defaultdict, Counter


class Solution:
    def mostVisitedPattern(self, username: [str], timestamp: [int], website: [str]) -> [str]:

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


s = Solution()
print(s.mostVisitedPattern(username=["ua", "ua", "ua", "ub", "ub", "ub"], timestamp=[1, 2, 3, 4, 5, 6],
                           website=["a", "b", "a", "a", "b", "c"]))
# print(s.mostVisitedPattern(username=["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"],
#                            timestamp=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#                            website=["home", "about", "career", "home", "cart", "maps", "home", "home", "about",
#                                     "career"]))
