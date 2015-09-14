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

    p0 = list(path)

    #   step 1:
    while p0[-1] is '/':
        p0.pop()

    p1 = ''.join(p0).split('/')
    p1.remove('.')

    for p in p1:
        if p is '..':
            p1.pop()

