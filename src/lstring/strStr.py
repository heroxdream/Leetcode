__author__ = 'hanxuan'

def strStrBruteForce(haystack, needle):
    """
    :param haystack: string
    :param needle: string
    :return: int
    Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
    """

    pointer = 0
    n_len = len(needle)
    while pointer < len(haystack):
        if haystack[pointer:pointer + n_len] == needle:
            return pointer
        pointer += 1
        if pointer + n_len > len(haystack):
            return -1
    return 0 if needle == haystack else -1

if __name__ == '__main__':
    print(strStrBruteForce('', ''))
    print(strStrBruteForce('', '134'))
    print(strStrBruteForce('asfasdf134', '1345'))
    print(strStrBruteForce('134', ''))
