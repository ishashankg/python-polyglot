def check_prime(number: int) -> str:
    if number.isnumeric():
        num = int(number)
    else:
        return "Please provide numeric value"
    is_prime = [True] * (num + 1)
    _populate_prime_array(num, is_prime)
    if _right_truncatable_prime(num, is_prime) and _left_truncatable_prime(num, is_prime):
        return "{} {}".format(num, " is a two sided prime number")
    else:
        return "{} {}".format(num, " is NOT a two sided prime number")


def _populate_prime_array(n: int, is_prime: list):
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            i = p * 2
            while i <= n:
                is_prime[i] = False
                i = i + p
        p = p + 1


def _right_truncatable_prime(n: int, is_prime: list) -> bool:
    while n != 0:
        if is_prime[n]:
            n = n // 10
        else:
            return False
    return True


def _left_truncatable_prime(n: int, is_prime: list) -> bool:
    temp = n
    count = 0
    while temp != 0:
        count = count + 1
        temp1 = temp % 10
        if temp1 == 0:
            return False
        temp = temp // 10

    for i in range(count, 0, -1):
        mod = _power(10, i)
        if not is_prime[n % mod]:
            return False

    return True


def _power(x: int, y: int) -> int:
    if y == 0:
        return 1
    elif y % 2 == 0:
        return _power(x, y // 2) * _power(x, y // 2)
    else:
        return x * _power(x, y // 2) * _power(x, y // 2)
