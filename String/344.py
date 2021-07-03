def reverseString(s: [str]) -> None:
    """
    0(n/2) time, 0(1) space, loop half of string, use two pointers
    """
    j = len(s) - 1    # left pointer
    for i in range(len(s) // 2):     # loop only half string
        s[i] = s[j]                  # change position
        j -= 1

    print(s)

    return None


reverseString(["h", "e", "l", "l", "o"])
