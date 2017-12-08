"""
@Auth:  Mark24Code
@Email: mark.zhangyoung@qq.com
@Data:  2017.12.08

@Intro:
77.Combinations
输出 C(n,k)

以每个元素为起点，向外延伸，分叉点为自己的子，递归生成
从根节点到叶节点的长度为 目标长度k 停止

这还是我第一次看到生成组合的方法。高中没学好，超过四位就不晓得如何生成组合了。
这个是十分简单的操作方法。
"""


class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nlst = list(range(1, n + 1))

        def comb(lst, m):
            if m > len(lst):
                return []
            if m == 0:
                return [[]]
            res = []
            for i, x in enumerate(lst):
                for suffix in comb(lst[i + 1:], m - 1):
                    res.append([x] + suffix)
            return res

        return comb(nlst, k)


if __name__ == '__main__':
    s = Solution()
    print(s.combine(3, 1))
