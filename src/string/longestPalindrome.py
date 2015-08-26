__author__ = 'hanxuan'


"""
    find the longest palindrome of a give string s
    :param s: string
    :return: string
"""

def longestPalindromeV1(s):

    global_best_str = ''
    for i in range(0, len(s)):
        for j in range(i + 1, len(s)):
            sub = s[i:j + 1]
            sub_reverse = sub[::-1]
            if sub == sub_reverse and len(sub) > len(global_best_str):
                global_best_str = sub
    return global_best_str


def longestPalindromeV2(s):

    st, ed = dpLongestPalindrome(s, 0, len(s) - 1, {})
    return s[st:ed + 1]

def dpLongestPalindrome(s, start, end, dic):
    """
    :param s:
    :param start:
    :param end:
    :param dic:
    :return:
    """

    if (start, end) in dic:
        return dic[(start, end)]

    if start > end:
        return 0, -1

    if start == end:
        dic[(start, end)] = (start, end)
        return start, end

    if end - start == 1:
        if s[start] == s[end]:
            dic[(start, end)] = (start, end)
            return start, end
        else:
            dic[(start, end)] = (start, start)
            return start, start

    if s[start] == s[end] and dpLongestPalindrome(s, start + 1, end - 1, dic) == (start + 1, end - 1):
        dic[(start, end)] = (start, end)
        return start, end

    tpl1 = dpLongestPalindrome(s, start + 1, end, dic)
    tpl3 = dpLongestPalindrome(s, start, end - 1, dic)
    m = {tpl1: tpl1[1] - tpl1[0], tpl3: tpl3[1] - tpl3[0]}

    best = sorted(m, key=m.get, reverse=True)

    dic[(start, end)] = best[0]

    return best[0]


def longestPalindromeV3(s):

    bstart = 0
    bend = 0
    for i in range(0, len(s)):
        for j in range(i + 1, len(s)):
            sub = s[i:j + 1]
            sub_reverse = sub[::-1]
            if sub == sub_reverse and len(sub) > bend - bstart + 1:
                bstart = i
                bend = j

    return s[bstart:bend + 1]

def dplongestPalindromeV4(s):

    memo = {}
    bstart = 0
    bend = 1
    for i in range(len(s)):
        memo[(i, i)] = True
        for j in range(i):
            if j == i - 1:
                memo[(j, i)] = s[j] == s[i]
            else:
                memo[(j, i)] = s[j] == s[i] and memo[(j + 1, i - 1)]

            if memo[(j, i)] and i - j > bend - bstart:
                bstart = j
                bend = i
    return s[bstart:bend + 1]

def dplongestPalindromeV5(s):

    table = [[False] * 1000] * 1000
    bstart = 0
    bend = 1
    for i in range(len(s)):
        table[i][i] = True
        for j in range(i):
            if j == i - 1:
                table[i][j] = s[j] == s[i]
            else:
                table[i][j] = s[j] == s[i] and table[i - 1][j + 1]

            if table[i][j] and i - j > bend - bstart:
                bstart = j
                bend = i
    return s[bstart:bend + 1]

def linerLongestPalindromeV6(s):
    """
    string(i,l) is a substring of s where i is the start index and l is the length

    S(n) is the longest palindrome for substring of s with indice from 0 to n

    if S(n-1) = string(i,l)

    then S(n) =

    string(n-l, l+1) if string(n-l, l+1) is palindrome
    string(n-l-1, l+2) if string(n-l-1, l+2) is palindrome
    S(n) otherwise

    # The key intuition of this algorithm is that palindromes are made up of
    # smaller palindromes.

    # So, a palindrome of length 100 (for example), will have a palindrome of
    # length 98 inside it, and one of length 96, ... 50, ... 4, and 2.

    # Because of this, we can move across our string, checking if the current
    # place is a palindrome of a particular length (the longest length palindrome
    # found so far + 1), and if it is, update the longest length, and move forward.

    # In this way, we find our longest palindromes "from the inside out", starting
    # with length x, then x+2, x+4, ...

    # Example:
    # "xxABCDCBAio"
    #  0123456789  < indexes
    # As we scan our string, we initially find a palindrome of length 2 (xx)
    # We always look backwards!
    # When we get to index 2,3,4, we see no length 3+ palindrome ending there.
    # But when we get to index 6, looking back 3 characters, we see "CDC"! So our
    # longest palindrome is now length 3.
    # At index 7, we look back and see no length 4 palindromes, but find one of
    # length 5 ("BCDCB").
    # And finally, by i = 8, we find the full "ABCDCBA"

    :param s:
    :return:
    """

    start = 0
    max_len = 0
    for i in range(len(s)):
        if i - max_len >= 1 and s[i - max_len - 1:i + 1] == s[i - max_len - 1:i + 1][::-1]:
            start = i - max_len - 1
            max_len += 2
        elif i - max_len >= 0 and s[i - max_len: i + 1] == s[i - max_len:i + 1][::-1]:
            start = i - max_len
            max_len += 1
    return s[start:start + max_len]


def manacherLongestPalindrome(s):
    """
    :param s:
    :return:

    lots of details and tricks
    """

    t = '#'.join('^{}$'.format(s))
    right = 0
    center = 0
    p = [0] * len(t)
    for i in range(1, len(t) - 1):

        p[i] = int(right > i) and min(p[2 * center - i], right - i)

        while t[i - p[i] - 1] == t[i + p[i] + 1]:
            p[i] += 1

        if i + p[i] > right:
            center, right = i, i + p[i]

    max_len, best_center = max((n, i) for i, n in enumerate(p))

    return s[(best_center - max_len) // 2: (best_center + max_len) // 2]

if __name__ == '__main__':

    s0 = 'a'
    s1 = '1223'
    s2 = 'abac'
    s3 = 'ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy'
    s4 = 'cccc'
    s5 = 'bb'

    from time import time

    # print(longestPalindromeV1('1223'))
    # print(longestPalindromeV1('abac'))
    #
    #
    #
    #
    # start = time() * 1000
    # print(longestPalindromeV1(s))  # 286 ms, bad
    # end = time() * 1000
    # print(end - start)

    # print(longestPalindromeV2(s0))
    # print(longestPalindromeV2(s1))
    # print(longestPalindromeV2(s2))
    #
    # t1 = time() * 1000
    # print(longestPalindromeV2(s3))  # 1.63 s, very bad
    # t2 = time() * 1000
    # print(t1 - t2)
    # print(longestPalindromeV2(s4))

    # print(longestPalindromeV3(s0))
    # print(longestPalindromeV3(s1))
    # print(longestPalindromeV3(s2))
    #
    # t1 = time() * 1000
    # print(longestPalindromeV3(s3))  # 300 s, bad
    # t2 = time() * 1000
    # print(t2 - t1)
    # print(longestPalindromeV3(s4))

    # print(dplongestPalindromeV4(s0))
    # print(dplongestPalindromeV4(s1))
    # print(dplongestPalindromeV4(s2))
    #
    # t1 = time() * 1000
    # print(dplongestPalindromeV4(s3))  # 300 s, bad
    # t2 = time() * 1000
    # print(t2 - t1)
    # print(dplongestPalindromeV4(s4))

    # print(dplongestPalindromeV5(s0))
    # print(dplongestPalindromeV5(s1))
    # print(dplongestPalindromeV5(s2))
    #
    # t1 = time() * 1000
    # print(dplongestPalindromeV5(s3))  # 120 ms, fair
    # t2 = time() * 1000
    # print(t2 - t1)
    # print(dplongestPalindromeV5(s4))

    # print(linerLongestPalindromeV6(s0))
    # print(linerLongestPalindromeV6(s1))
    # print(linerLongestPalindromeV6(s2))
    #
    # t1 = time() * 1000
    # print(linerLongestPalindromeV6(s3))  # 1.20 ms, good
    # t2 = time() * 1000
    # print(t2 - t1)
    # print(linerLongestPalindromeV6(s4))

    print(manacherLongestPalindrome(s0))
    print(manacherLongestPalindrome(s1))
    print(manacherLongestPalindrome(s2))

    t1 = time() * 1000
    print(manacherLongestPalindrome(s3))  # 2 ms, good
    t2 = time() * 1000
    print(t2 - t1)
    print(manacherLongestPalindrome(s4))
    print(manacherLongestPalindrome('a'))
