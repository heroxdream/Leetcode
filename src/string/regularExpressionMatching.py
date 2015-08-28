__author__ = 'hanxuan'

dot = '.'
asterisk = '*'

# def isMatch(text, pattern):
#     """
#     :param text: string
#     :param pattern: string
#     :return: bool
#
#     Some examples:
#     isMatch("","a") → false
#     isMatch("","a*") → true
#     isMatch("aa","a") → false
#     isMatch("aa","aa") → true
#     isMatch("aaa","aa") → false
#     isMatch("aa", "a*") → true
#     isMatch("aa", ".*") → true
#     isMatch("ab", ".*") → true
#     isMatch("aab", "c*a*b") → true
#     """
#
#     rules = compile_pattern(pattern)
#
#     print('text:{} rules:{}'.format(text, rules))
#
#     hard_line = -1
#     pointer = 0
#     for i in range(len(rules)):
#         rule = rules[i]
#         if asterisk in rule:
#             match_char = rule[0]
#             while pointer < len(text) and isMatchOne(text, pointer, match_char):
#                 pointer += 1
#         elif dot in rule:
#             if pointer < len(text):
#                 pointer += 1
#             elif pointer -1 > hard_line:
#                 hard_line += 1
#             else:
#                 return False
#         else:
#             while True:
#                 if pointer + len(rule) <= len(text) and text[pointer:pointer + len(rule)] == rule:
#                     hard_line += len(rule)
#                     pointer += len(rule)
#                     break
#                 else:
#                     pointer -= 1
#                     if pointer <= hard_line:
#                         return False
#     return True if pointer == len(text) else False

def isMatch(text, pattern):
    """
    :param text: string
    :param pattern: string
    :return: bool

    Some examples:
    isMatch("","a") → false
    isMatch("","a*") → true
    isMatch("aa","a") → false
    isMatch("aa","aa") → true
    isMatch("aaa","aa") → false
    isMatch("aa", "a*") → true
    isMatch("aa", ".*") → true
    isMatch("ab", ".*") → true
    isMatch("aab", "c*a*b") → true
    """

    rules = compile_pattern(pattern)
    print('text:{}, rules:{}'.format(text, rules))
    match_dic = {}
    return match(text, rules, match_dic)


def match(text, rules,  match_dic):

    '''
    :param text: string
    :param rules: List[string]
    :param match_dic: dict
    :return: bool

    a recursive DP solution

    '''

    if (len(text), len(rules)) in match_dic:
        return match_dic[(len(text), len(rules))]

    if len(rules) == 0:
        match_dic[(len(text), len(rules))] = text == ''
        return match_dic[(len(text), len(rules))]

    if len(text) == 0:
        match_dic[(len(text), len(rules))] = sorted(map(lambda x: asterisk in x, rules))[0]
        return match_dic[(len(text), len(rules))]

    rule = rules[0]
    if asterisk in rule:
        match_char = rule[0]
        pointer = 0
        while pointer < len(text) and isMatchOne(text, pointer, match_char):
            pointer += 1
        for i in range(pointer + 1):
            if match(text[i:], rules[1:], match_dic):
                match_dic[(len(text), len(rules))] = True
                return True
        match_dic[(len(text), len(rules))] = False
        return False
    elif dot in rule:
        match_dic[(len(text), len(rules))] = match(text[1:], rules[1:], match_dic)
        return match_dic[(len(text), len(rules))]
    else:
        match_dic[(len(text), len(rules))] = text.startswith(rule) and match(text[len(rule):], rules[1:], match_dic)
        return match_dic[(len(text), len(rules))]

def compile_pattern(pattern):
    rules = []
    seq = []
    for i in range(len(pattern)):
        char = pattern[i]
        if isChar(char):
            seq.append(char)
        elif isAsterisk(char):
            last_char = seq.pop()
            r1 = ''.join(seq)
            r2 = last_char + asterisk
            rules.append(r1) if len(r1) > 0 else 1
            rules.append(r2)
            seq = []
        else:
            if i + 1 < len(pattern) and pattern[i + 1] == asterisk:
                seq.append(char)
                continue
            r1 = ''.join(seq)
            r2 = dot
            rules.append(r1) if len(r1) > 0 else 1
            rules.append(r2)
            seq = []
    rules.append(''.join(seq)) if len(seq) > 0 else 1
    return rules


def isDot(c):
    return c == dot


def isAsterisk(c):
    return c == asterisk


def isChar(c):
    return c != dot and c != asterisk


def isMatchOne(s, p, c):
    return True if isDot(c) and len(s) > p else s[p] == c



if __name__ == '__main__':
    p0 = 'a'
    p1 = 'a*.bccc*.'
    p2 = '.*'
    p3 = 'aa'
    p4 = 'a*'
    p5 = 'a*b*c*'
    p6 = 'a*.b*cccc*.*.'
    p7 = 'a*.b*cccc*.*..'
    p8 = ''
    p9 = 'c*.....'
    p10 = '.*..'
    p11 = 'c*....'
    p12 = 'a.'

    s0 = ''
    s1 = 'aabccc'
    s3 = 'cccc'
    s4 = 'aa'
    s5 = 'a'

    s6, p13 = "aasdfasdfasdfasdfas", "aasdf.*asdf.*asdf.*asdf.*s"
    s7, p14 = "bbcbbcbcbbcaabcacb", "a*.*ac*a*a*.a..*.*"
    s8, p15 = "aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*b"

    # print(compile_pattern(p0))
    # print(compile_pattern(p1))
    # print(compile_pattern(p2))
    # print(compile_pattern(p3))
    # print(compile_pattern(p4))
    # print(compile_pattern(p5))
    # print(compile_pattern(p6))

    print(isMatch(s0, p0))
    print(isMatch(s0, p4))
    print(isMatch(s0, p5))
    print(isMatch(s0, p8))
    print(isMatch(s0, p2))
    print(isMatch(s1, p1))
    print(isMatch(s3, p9))
    print(isMatch(s3, p11))
    print(isMatch(s4, p0))
    print(isMatch(s4, p3))
    print(isMatch(s4, p10))
    print(isMatch(s4, p12))
    print(isMatch(s5, p12))
    print(isMatch(s6, p13))
    print(isMatch(s7, p14))
    print(isMatch(s8, p15))
    print(isMatch('a', 'ab*a'))
