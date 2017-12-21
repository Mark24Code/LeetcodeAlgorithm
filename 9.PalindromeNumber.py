"""
@Auth:  Mark24Code
@Email: mark.zhangyoung@qq.com
@Data:  2017.12.21

@Intro:
9.Palindrome Number
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.
Some hints:

Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x%10==0 and x!=0):
            #<0 && 2120
            return False
        elif x//10==0:
            #0<=x<10
            return True
        else:
            pa = 0
            while pa<x:
                pa = pa*10 + x%10
                x = x//10
            if x==0:
                return False
            else:
                return x==pa or x==pa//10

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(10))
