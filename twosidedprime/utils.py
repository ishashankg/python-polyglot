def checkPrime(number: int) -> str:
    if number.isnumeric():
        num = int(number)
    else:
        return "Please provide numeric value"
    isPrime = [True] * (num + 1)
    _populatePrimeArray(num, isPrime)
    if _rightTruncatablePrime(num, isPrime) and _leftTruncatablePrime(num, isPrime):
        return "{} {}".format(num, " is a two sided prime number")
    else:
        return "{} {}".format(num, " is NOT a two sided prime number")


def _populatePrimeArray(n: int, isPrime: list):
    isPrime[0] = isPrime[1] = False
    p = 2
    while p * p <= n:
        if isPrime[p]:
            i = p * 2
            while i <= n:
                isPrime[i] = False
                i = i + p
        p = p + 1


def _rightTruncatablePrime(n: int, isPrime: list) -> bool:
    while n != 0:
        if isPrime[n]:
            n = n // 10
        else:
            return False
    return True


def _leftTruncatablePrime(n: int, isPrime: list) -> bool:
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
        if not isPrime[n % mod]:
            return False

    return True


def _power(x: int, y: int) -> int:
    if y == 0:
        return 1
    elif y % 2 == 0:
        return _power(x, y // 2) * _power(x, y // 2)
    else:
        return x * _power(x, y // 2) * _power(x, y // 2)
