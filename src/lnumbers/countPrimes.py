__author__ = 'hanxuan'
"""
Count the number of prime numbers less than a non-negative number, n.

"""


def countPrimes(n):
    """
    :param n: int >= 0
    :return:
    """
    if n <= 2:
        return 0

    x = 0
    for i in range(2, n):
        if isPrime(i):
            x += 1
    return x

def isPrime(n):
    """
    :param n: int >= 2
    :return: bool

    O(n^0.5) time

    """

    if n == 2:
        return True

    start = 2
    end = n
    while start <= end:
        if n % start != 0:
            start += 1
            end = n // start
        else:
            return False

    return True


def countPrimesV2(n):

    if n <= 2:
        return 0

    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5)):

        if primes[i]:
            j = i ** 2
            while j < n:
                primes[j] = False
                j += i
    return sum(primes)


def countPrimesV3(n):
    """
    :param n:
    :return:

    very efficient
    """
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return sum(primes)



if __name__ == '__main__':
    # print(countPrimes(2))
    # print(countPrimes(7))
    # print(countPrimes(8))
    # print(countPrimes(47))
    # print(countPrimes(49))
    # print(countPrimes(499979))
    import time
    t1 = time.time()
    print(countPrimesV2(2))
    print(countPrimesV2(7))
    print(countPrimesV2(8))
    print(countPrimesV2(47))
    print(countPrimesV2(49))
    print(countPrimesV2(499979))
    print(countPrimesV2(1500000))

    t2 = time.time()
    print(countPrimesV3(2))
    print(countPrimesV3(7))
    print(countPrimesV3(8))
    print(countPrimesV3(47))
    print(countPrimesV3(49))
    print(countPrimesV3(499979))
    print(countPrimesV3(1500000))
    t3 = time.time()

    print(t2 - t1, t3 - t2)     # 0.67 vs. 0.19


