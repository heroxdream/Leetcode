"""
Given a string of numbers and operators, return all possible results from computing all the different
possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
"""


def diffWaysToCompute(input):
    """
    :type input: str
    :rtype: List[int]
    """
    if (input.isdigit()):
        return [int(input)]

    ret = []
    for i in range(len(input)):
        if input[i] in '+-*':
            part1 = input[:i]
            part2 = input[i+1:]
            ret1 = diffWaysToCompute(part1)
            ret2 = diffWaysToCompute(part2)
            for d1 in ret1:
                for d2 in ret2:
                    ret.append(helper(d1, d2, input[i]))
    return ret


def helper(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2