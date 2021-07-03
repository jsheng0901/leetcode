def fourSumCount(A: [int], B: [int], C: [int], D: [int]) -> int:
    """
    O（(n ^ 2)/2) time, n is length of each A, B, C, D
    same as two sum, just separate four into 2 of two sum, store first two sum in dictionary and loop last two find
    if the rest value has been shown before in first two sum dictionary
    """
    # loop A, B two list first and store a + b as key and a + b frequency as value
    a_b = {}
    for a in A:
        for b in B:
            if a + b in a_b:
                a_b[a + b] += 1
            else:
                a_b[a + b] = 1

    count = 0  # define final output count
    # loop over C and D find 0 - (c + d) has shown before in a_b dictionary and return frequency
    for c in C:
        for d in D:
            rest = 0 - (c + d)
            if rest in a_b:
                count += a_b[rest]

    return count


print(fourSumCount(A=[1, 2], B=[-2, -1], C=[-1, 2], D=[0, 2]))
