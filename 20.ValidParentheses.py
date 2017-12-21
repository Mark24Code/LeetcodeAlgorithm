"""
@Auth:  Mark24Code
@Email: mark.zhangyoung@qq.com
@Data:  2017.12.21

@Intro:
20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        stack = []
        left_brackets = ['(','[','{']
        right_brackets = [')',']','}']
        match_brackets = {
            "[":"]",
            "{":"}",
            "(":")"
        }
        while s:
            elem = s.pop()
            if elem in right_brackets:
                stack.append(elem)
            elif elem in left_brackets:
                if not stack or match_brackets[elem] != stack.pop():
                    return False
        if stack:
            return False
        else:
            return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValid('{}'))
