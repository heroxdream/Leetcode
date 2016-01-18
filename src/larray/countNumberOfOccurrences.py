"""
Given a sorted array arr[] and a number x, write a function that counts the occurrences of x in arr[].
 Expected time complexity is O(Logn)

Examples:

  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 2
  Output: 4 // x (or 2) occurs 4 times in arr[]

  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 3
  Output: 1

  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 1
  Output: 2

  Input: arr[] = {1, 1, 2, 2, 2, 2, 3,},   x = 4
  Output: -1 // 4 doesn't occur in arr[]
Method 1 (Linear Search)
Linearly search for x, count the occurrences of x and return the count.

Time Complexity: O(n)

Method 2 (Use Binary Search)
1) Use Binary search to get index of the first occurrence of x in arr[]. Let the index of the first occurrence be i.
2) Use Binary search to get index of the last occurrence of x in arr[]. Let the index of the last occurrence be j.
3) Return (j – i + 1);
"""


def first(arr, lo, hi, x):

    if lo > hi:
        return -1

    mid = (lo + hi) // 2
    if x == arr[mid] and (mid == 0 or arr[mid - 1] < x):
        return mid
    elif x > arr[mid]:
        return first(arr, mid + 1, hi, x)
    else:
        return first(arr, lo, mid - 1, x)


def last(arr, lo, hi, x):

    if lo > hi:
        return -1

    mid = (lo + hi) // 2
    if x == arr[mid] and (mid == len(arr) - 1 or arr[mid + 1] > x):
        return mid
    elif x < arr[mid]:
        return last(arr, lo, mid - 1, x)
    else:
        return last(arr, mid + 1, hi, x)


def search(arr, x):

    length = len(arr)

    i = first(arr, 0, length - 1, x)

    if i < 0:
        return -1

    j = last(arr, 0, length - 1, x)

    # print(j, i)

    return j - i + 1


if __name__ == '__main__':
    arr0 = [1, 1, 2, 2, 2, 2, 3]
    print(search(arr0, 1))
    print(search(arr0, 2))
    print(search(arr0, 3))
    print(search(arr0, 4))
