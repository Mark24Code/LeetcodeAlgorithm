"""
@Auth:  Mark24Code
@Email: mark.zhangyoung@qq.com
@Data:  2017.12.08

@Intro:
46.Permutations
输出 A(n,k)

主要是代码这边，要使用 list，作用类似于 copy.copy 深度复制
否则会影响 lst

    nlst = list(lst)
    nlst.pop(i)

"""


class Solution:
    def permute(self, arr):
        """
        :type arr: List
        :rtype: List[List[int]]
        """
        lst = arr
        m = len(arr)
        def perm(lst, m):
            if m > len(lst):
                return []
            if m == 0:
                return [[]]
            res = []
            for i, x in enumerate(lst):
                nlst = list(lst)
                nlst.pop(i)
                for suffix in perm(nlst, m - 1):
                    res.append([x] + suffix)
            return res
        return perm(lst,m)


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))
