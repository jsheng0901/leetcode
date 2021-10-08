import heapq
from collections import defaultdict, Counter


class Solution:
    """ O(n) time, count, heap and return all O(n), O(n) space """
    def topKFrequent(self, words: [str], k: int) -> [str]:
        count = Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
    # below is sort dictionary way
#         words.sort()
#         dict1={}
#         for i in words:
#             if i not in dict1:
#                 dict1[i]=0
#             dict1[i]+=1

#         sorted_dict= {k:v for k,v in sorted(dict1.items(), key = lambda x: x[1], reverse=True)}

#         count=0
#         l=[]
#         for i in sorted_dict:
#             if count<k:
#                 l.append(i)
#             count+=1

#         return l
