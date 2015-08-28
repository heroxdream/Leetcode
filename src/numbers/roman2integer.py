__author__ = 'hanxuan'


'''
I = 1;
V = 5;
X = 10;
L = 50;
C = 100;
D = 500;
M = 1000;

I   placed before V or X indicates one less, so four is IV (one less than five) and nine is IX (one less than ten)

X   placed before L or C indicates ten less, so forty is XL (ten less than fifty) and ninety is XC (ten less than a
    hundred)

C   placed before D or M indicates a hundred less, so four hundred is CD (a hundred less than five hundred) and nine
    hundred is CM (a hundred less than a thousand)
'''

def roman_to_int(s):
    """
    :type s: str
    :rtype: int
    """
    r2i = {'S': -1, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result = 0
    for i in range(len(s)):
        c = s[i]
        c_next = s[i + 1] if i + 1 < len(s) else 'S'
        if r2i[c] < r2i[c_next]:
            result += r2i[c] * -1
        else:
            result += r2i[c]
    return result

if __name__ == '__main__':
    r0 = 'MCMLIV'   # 1954
    r1 = 'MCMXC'    # 1990
    r2 = 'MMXIV'    # 2014
    r3 = 'I'        # 1

    print(roman_to_int(r0), 1954)
    print(roman_to_int(r1), 1990)
    print(roman_to_int(r2), 2014)
    print(roman_to_int(r3), 1)
