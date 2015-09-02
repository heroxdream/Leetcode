__author__ = 'hanxuan'

"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level
revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""

def compareVersion(version1, version2):

    if version1 is version2:
        return 1

    digits1 = [i for i in map(lambda x: int(x), version1.split('.'))]
    digits2 = [i for i in map(lambda x: int(x), version2.split('.'))]

    ptr1 = ptr2 = 0
    min_len = min(len(digits1), len(digits2))
    while ptr1 < min_len and ptr2 < min_len:
        if digits1[ptr1] > digits2[ptr2]:
            return 1
        elif digits1[ptr1] < digits2[ptr2]:
            return -1
        else:
            ptr1 += 1
            ptr2 += 1

    if len(digits1) == len(digits2):
        return 0

    if len(digits1) > len(digits2) and sum(digits1[ptr1:]) == 0:
        return 0

    if len(digits2) > len(digits1) and sum(digits2[ptr2:]) == 0:
        return 0

    return 1 if len(digits1) > len(digits2) else -1

if __name__ == '__main__':
    print(compareVersion('1', '0'))
    print(compareVersion('1.1.1.1.1', '1.1.1.1.1'))
    print(compareVersion('1.1.1.1.1', '1.1.1.1'))
    print(compareVersion('01', '1'))
    print(compareVersion('1.0', '1.0.0'))
