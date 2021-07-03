def reverseString(s: [str]) -> None:
    """
    0(n/2) time, 0(1) space, loop half of string, use two pointers
    """
    end_index = len(s) - 1
    for i in range(len(s) // 2):
        s[i], s[end_index] = s[end_index], s[i]
        end_index -= 1

    return s


print(reverseString(["h", "e", "l", "l", "o", "f"]))
