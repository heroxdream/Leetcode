__author__ = 'hanxuan'

def lengthOfLongestSubstring(s):

    global_max_list = []
    consecutive_dict = {}
    for i in range(len(s)):
        if s[i] in consecutive_dict:
            if len(consecutive_dict) > len(global_max_list):
                global_max_list = sorted(consecutive_dict, key=consecutive_dict.get)
            start = consecutive_dict[s[i]] + 1
            consecutive_dict = dict(filter(lambda x: x[1] >= start, consecutive_dict.items()))

        consecutive_dict[s[i]] = i

    if len(consecutive_dict) > len(global_max_list):
        global_max_list = sorted(consecutive_dict, key=consecutive_dict.get)

    return len(global_max_list), global_max_list

def lengthOfLongestSubstringV2(s):

    global_max = []
    consecutive = []
    for c in s:
        if c in consecutive:
            if len(consecutive) > len(global_max):
                global_max = consecutive[:]
            for cc in consecutive[:]:
                consecutive.remove(cc)
                if cc == c:
                    break

        consecutive.append(c)

    if len(consecutive) > len(global_max):
        global_max = consecutive

    return len(global_max), global_max


if __name__ == '__main__':

    s1 = 'abc'
    print('{} : {}'.format(s1, lengthOfLongestSubstringV2(s1)))

    s1 = 'abcabcbb'
    print('{} : {}'.format(s1, lengthOfLongestSubstringV2(s1)))

    s1 = 'aa'
    print('{} : {}'.format(s1, lengthOfLongestSubstringV2(s1)))

    s1 = 'abccdeftt'
    print('{} : {}'.format(s1, lengthOfLongestSubstringV2(s1)))

    s1 = 'jbpnbwwd'
    print('{} : {}'.format(s1, lengthOfLongestSubstringV2(s1)))

    s1 = "dvdf"
    print('{} : {}'.format(s1, lengthOfLongestSubstringV2(s1)))