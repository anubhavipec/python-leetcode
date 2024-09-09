from collections import deque  # You need to import deque


class Solution:
    def isValid(self,s:str) -> bool:
        if len(s) == 0 : return True
        bracket_dict = { "]" : "[","}":"{",")":"("}
        stack = deque()
        for item in s:
            if item not in bracket_dict:
                stack.append(item)
            else:
                if len(stack) == 0:
                    return False
                poped = stack.pop()
                if poped != bracket_dict.get(item):
                    return False
        if len(stack) == 0:
            return True
        return False