def isAnagram(s: str, t: str) -> bool:
    """
    O(n) time, loop over s and t and whole dictionary
    """
    record = {}
    for i in s:                      # loop over s string, if item not in record then add if in then add 1
        if i in record:
            record[i] += 1
        else:
            record[i] = 1

    for j in t:                      # loop over t string, if item not in record then return false if in then minus 1
        if j in record:
            record[j] -= 1
        else:
            return False

    for k in record.values():        # loop over record dict, if has key not 0 return false
        if k != 0:
            return False

    return True


print(isAnagram('esss', 'sses'))
