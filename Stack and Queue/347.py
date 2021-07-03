import heapq


def topKFrequent(nums: [int], k: int) -> [int]:
    """
    O(nlogn) time, first count frequency, then build a min heap, here we use build in heap, then transfer to list
    """
    # calculate frequency first
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    min_heap = []                     # min value will be on top
    for key, val in freq.items():
        heapq.heappush(min_heap, (val, key))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    top_numbers = [el[1] for el in min_heap]

    return top_numbers


print(topKFrequent([1, 1, 1, 2, 2, 4], 2))
