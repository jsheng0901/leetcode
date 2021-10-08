def solution(A, K, L):
    if K + L > len(A):
        return -1

    if K + L == len(A):
        return sum(A)

    alice = 0
    bob = 0
    sum = 0

    for i in range(len(A) - K - L):
        if alice == 0:
            for k in range(i, i + K):
                alice += A[k]
        else:
            alice += A[i + K - 1]
            alice -= A[i - 1]

        bob = 0

        for j in range(i + K, len(A) - L + 1):
            if bob == 0:
                for k in range(j, j + L):
                    bob += A[k]
            else:
                bob += A[j + L - 1]
                bob -= A[j - 1]
            sum = max(sum, alice + bob)

    # reverse
    bob = 0
    for i in range(len(A) - K - L):
        if bob == 0:
            for k in range(i, i + L):
                bob += A[k]
        else:
            bob += A[i + L - 1]
            bob -= A[i - 1]

        alice = 0

        for j in range(i + L, len(A) - K + 1):
            if alice == 0:
                for k in range(j, j + K):
                    alice += A[k]
            else:
                alice += A[j + K - 1]
                alice -= A[j - 1]
            sum = max(sum, alice + bob)

    return sum