"""
@Auth:  Mark24Code
@Email: mark.zhangyoung@qq.com
@Data:  2017.12.21

@Intro:
27. Remove Element
Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

"""


class Solution:
    def removeElement(self, nums, val):
        """
        和第26题指导思想一样
        O(n)
        去修改内存中的
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        tail = 0
        for num in nums:
            if num != val:
                nums[tail] = num
                tail += 1
        return tail



if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([3,2,2,3],3))