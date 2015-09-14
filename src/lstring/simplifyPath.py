__author__ = 'hanxuan'


"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

'/' => '/'

'/../' => '/'

"""


def simplify_path(path):
    """
    :param path: string
    :return: string
    """
    if not path:
        return ''

    p0 = path.split('/')
    p1 = []
    for p in p0:
        if p != '' and p != '.':
            p1.append(p)

    p2 = []
    for p in p1:
        if p != '..':
            p2.append(p)
        elif p2:
            p2.pop()
        else:
            continue
    p2.insert(0, '')

    return '/'.join(p2) if len(p2) > 1 else '/'


if __name__ == '__main__':

    print(simplify_path('/'))
    print(simplify_path('/home/'))
    print(simplify_path('/a/./b/../../c/'))
    print(simplify_path('/../../../c'))
    print(simplify_path('/a//b'))
