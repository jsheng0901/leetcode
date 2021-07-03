def canConstruct(ransomNote: str, magazine: str) -> bool:
    """
    O(N) time, same as 242, loop magazine first and store item and frequency. loop ransomNote delete 1 if appear before
    """
    magazine_dict = {}
    for i in magazine:
        if i not in magazine_dict:
            magazine_dict[i] = 1
        else:
            magazine_dict[i] += 1

    for j in ransomNote:
        if j in magazine_dict:
            if magazine_dict[j] > 0:
                magazine_dict[j] -= 1
            else:
                return False
        else:
            return False

    return True


print(canConstruct(ransomNote="aa", magazine="baa"))
