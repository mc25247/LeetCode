"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""


class Solution(object):
    def search(self, nums, target):
        l,r = 0,len(nums)-1
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        while l <= r:
            m= (l+r)// 2
            if nums[m]>target:
                r = m - 1
            elif nums [m] < target:
                l = m + 1
            else:
                return m
        return -1    
    
