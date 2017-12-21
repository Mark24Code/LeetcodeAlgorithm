"""
@Auth:  Mark24Code
@Email: mark.zhangyoung@qq.com
@Data:  2017.12.21

@Intro:
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        统计数字,回文长度为N,字符串数组长度为M
        方法简介且高效
        O(N*(M-1))
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix = []
        len_arr = [len(s) for s in strs]
        min_str_index = len_arr.index(min(len_arr))
        min_str_len = strs[min_str_index]
        strs.pop(min_str_index)
        rest_count = len(strs)
        for index,ch in enumerate(min_str_len):
            count = 0
            for st in strs:
                if st[index]==ch:
                    count+=1
            if count==rest_count:
                prefix.append(ch)
            else:
                break

        return "".join(prefix)

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(['abc','abcdef','abcccc','eeeeeeee']))
