"""
@Auth:  Mark24Code
@Email: mark.zhangyoung@qq.com
@Data:  2017.12.21

@Intro:
28. Implement strStr()
 Implement strStr().(http://www.cplusplus.com/reference/cstring/strstr/)

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1


"""


class Solution:
    def gen_pnext(self,p):
        i,k,m = 0,-1,len(p)
        pnext = [-1]*m
        while i<m-1:
            if k==-1 or p[i] == p[k]:
                i,k=i+1,k+1
                if p[i]==p[k]:
                    pnext[i]=pnext[k]
                else:
                    pnext[i]=k
            else:
                k=pnext[k]
        return pnext

    def matching_KMP(self,t,p,pnext):
        j,i = 0,0
        n,m = len(t),len(p)
        while j<n and i < m:
            if i==-1 or t[j]==p[i]:
                j,i = j+1,i+1
            else:
                i = pnext[i]
        if i==m:
            return j-i
        return -1

    def strStr(self, haystack, needle):
        """
        KMP算法
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        pnext = self.gen_pnext(needle)
        return self.matching_KMP(haystack,needle,pnext)


if __name__ == '__main__':
    s = Solution()
    print(s.strStr('abcllcc','ff'))