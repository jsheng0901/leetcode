def calculate_sum(n):
    sum = 0
    while n:
        sum += (n % 10) * (n % 10)
        n //= 10
    return sum


def isHappy(n: int) -> bool:
    sum_history = set()     # define a set to store sum not seen before
    while True:
        s = calculate_sum(n)
        if s == 1:
            return True

        if s not in sum_history:
            sum_history.add(s)
        else:
            return False
        n = s


print(isHappy(19))