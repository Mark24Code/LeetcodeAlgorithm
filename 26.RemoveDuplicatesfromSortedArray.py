"""
@Auth:  Mark24Code
@Email: mark.zhangyoung@qq.com
@Data:  2017.12.21

@Intro:
26. Remove Duplicates from Sorted Array
 Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.


"""


class Solution:
    def removeDuplicates(self, nums):
        """
        双指针法
        题目的意思是，[1,1,2]要变成 [1,2,2] ,[1,2]后面元素保留也无所。本质要把去重数组搬运到最前面
        这道题目太难理解，为了出题而出题的感觉
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        tail = 0
        for i in range(1,len(nums)):
            if nums[tail] != nums[i]:
                tail += 1
                nums[tail] = nums[i]
        return tail+1



if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,1,1]))