"""
@Auth:  Mark24Code
@Email: mark.zhangyoung@qq.com
@Data:  2017.12.21

@Intro:
38. Count and Say

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"

Example 2:

Input: 4
Output: "1211"

网摘录，题目意思：
思路：题意实在太难理解了，尤其是英文又不好，只能参看下别人的资料，理解下规则。终于理解，题意是n=1时输出字符串1；n=2时，数上次字符串中的数值个数，因为上次字符串有1个1，所以输出11；n=3时，由于上次字符是11，有2个1，所以输出21；n=4时，由于上次字符串是21，有1个2和1个1，所以输出1211。依次类推，写个countAndSay(n)函数返回字符串
"""


class Solution:
    def thinkSay(self,words):
        count = 1
        ans = ""
        if not words:
            return ""
        elif len(words)==1:
            ans = "1"+words
        else:
            for i in range(1,len(words)):
                if words[i-1]!=words[i]:
                    ans = "{}{}{}".format(ans,count,words[i-1])
                    count = 1
                else:
                    count +=1
            ans = "{}{}{}".format(ans, count, words[-1])
        return ans


    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        say = "1"
        if n==1:
            return say
        elif n>1:
            for i in range(2,n+1):
                say = self.thinkSay(say)
            return say





if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(4))