__author__ = 'hanxuan'


"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation
sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.

"""


def ladderLength(beginWord, endWord, wordList):

    if (not wordList) or min_distance(wordList, endWord) > 1 or min_distance(wordList, beginWord) > 1:
        return 0
    return recursive(beginWord, endWord, wordList) + 1


def recursive(beginWord, endWord, wordList):
    """
    """
    if min_distance(wordList, endWord) > 1:
        return len(beginWord)

    if distance(beginWord, endWord) <= 1:
        return 2

    new_word_list = [w for w in wordList if distance(w, beginWord) != 0]

    ans = len(beginWord)
    for w in new_word_list:
        if distance(w, beginWord) == 1:
            ans = min(ans, recursive(w, endWord, new_word_list))
    return ans + 1


def min_distance(word_list, word):
    """
    """

    d = len(word)
    for w in word_list:
        d = min(distance(w, word), d)
    return d

def distance(w1, w2):
    ans = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            ans += 1
    return ans


if __name__ == '__main__':

    b0 = "hit"
    e0 = "cog"
    wl0 = ["hot", "dot", "dog", "lot", "log"]
    print(b0, '->', e0, ladderLength(b0, e0, wl0))

    b1 = 'aaa'
    e1 = 'aaa'
    wl1 = []
    print(b1, '->', e1, ladderLength(b1, e1, wl1))

    b2 = "lit"
    e2 = "lit"
    wl2 = ["hot", "dot", "dog", "lot", "log"]
    print(b2, '->', e2, ladderLength(b2, e2, wl2))

    b3 = "qa"
    e3 = "sq"
    wl3 = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti",
           "ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr",
           "tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi",
           "di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt",
           "io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
    print(b3, '->', e3, ladderLength(b3, e3, wl3))

