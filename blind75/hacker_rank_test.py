'''
Given two strings, str1, and str2, where str1 contains exactly one character more than str2, find the indices of the characters in str1 that can be removed to make str1 equal to str2. Return the array of indices in increasing order. If it is not possible, return the array [-1]. 

Note: Use 0-based indexing.

Example

str1 = "abdgggda"

str2 = "abdggda"

ith position is removed 


Any "g" character at positions 3, 4, or 5 can be deleted to obtain str2. Return [3, 4, 5].
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getRemovableIndices' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING str1
#  2. STRING str2
#


def find_removal_indices(str1: str, str2: str) -> list:
    # Ensure that str1 is exactly 1 character longer than str2
    if len(str1) != len(str2) + 1:
        return [-1]

    removal_indices = []
    j = 0  # pointer for str2

    # Iterate over str1
    for i in range(len(str1)):

        # When mismatch happens, try skipping this character in str1
        # Check if the remaining substring matches
        if str1[:i] + str1[i+1:] == str2:
            removal_indices.append(i)
    
    # If no valid indices found, return [-1]
    return removal_indices if removal_indices else [-1]

# Test case example
str1 = "aabbb"
str2 = "aabb"
print(find_removal_indices(str1, str2))  # Output: [2, 3, 4]

    
    
    



# if __name__ == '__main__':
#     str1 = input()

#     str2 = input()

#     result = getRemovableIndices(str1, str2)

#     print('\n'.join(map(str, result)))
