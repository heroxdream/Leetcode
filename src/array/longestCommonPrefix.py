__author__ = 'hanxuan'
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
        return ''

    min_len = sorted(map(lambda x: len(x), strs))[0]
    print('min_len: {}'.format(min_len))

    prefixes = []
    for i in range(0, min_len):
        chars_set = set()
        for j in range(len(strs)):
            chars_set.add(strs[j][i])
            if len(chars_set) > 1:
                break
        if len(chars_set) > 1:
            break
        prefixes.append(chars_set.pop())
    return ''.join(prefixes)


if __name__ == '__main__':
    print(longestCommonPrefix(['12', '123']))
    print(longestCommonPrefix([]))
