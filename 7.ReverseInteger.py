"""
@Auth:  Mark24Code
@Email: mark.zhangyoung@qq.com
@Data:  2017.12.08

@Intro:
7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
    XMAX = 2 ** 31 - 1
    XMIN = -2 ** 31 - 1

    @staticmethod
    def checkRange(x):
        return True if Solution.XMIN < x < Solution.XMAX else False

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not self.checkRange(x):
            return 0

        SIGN = False
        if x < 0:
            SIGN = True
            x = 0 - x

        s = []
        while x != 0:
            s.append(x % 10)
            x = x // 10
        s.reverse()

        r = 0
        for index, i in enumerate(s):
            r += i * 10 ** index

        if SIGN:
            r = 0 - r

        return r if self.checkRange(r) else 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))
