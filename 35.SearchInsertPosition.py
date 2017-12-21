"""
@Auth:  Mark24Code
@Email: mark.zhangyoung@qq.com
@Data:  2017.12.21

@Intro:
35. Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2

Example 2:

Input: [1,3,5,6], 2
Output: 1

Example 3:

Input: [1,3,5,6], 7
Output: 4

Example 1:

Input: [1,3,5,6], 0
Output: 0


"""


class Solution:
    def searchInsert(self, nums, target):
        """
        二分比较，做了点改动
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            midnum = nums[mid]
            if midnum<target:
                low = mid+1
            elif midnum > target:
                high = mid-1
            else:
                return mid
        return low


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1,3,5,6], 4))