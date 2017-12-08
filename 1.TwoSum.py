"""
@Auth:  Mark24Code
@Email: mark.zhangyoung@qq.com
@Data:  2017.12.08

@Intro:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, i in enumerate(nums):
            rest = target - i
            if rest in nums[index + 1:]:
                rest_index = index + nums[index + 1:].index(rest) + 1
                return [index, rest_index]
        return []


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
