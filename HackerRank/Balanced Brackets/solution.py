#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    braket_dict = {')': '(', '}': '{', ']': '['}
    stack = []
    for ss in s:
        if ss in braket_dict.keys() and len(stack) > 0:
            if braket_dict[ss] == stack[-1]:
                stack.pop()
            else:
                return "NO"
        else:
            stack.append(ss)

    return "YES" if len(stack) == 0 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

