# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]



Solution 1: simple

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
      for i in range(nums.count(0)):
    
        nums.pop(nums.index(0))
        nums.extend([0])



Solution 2: Faster than solution 1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count = nums.count(0)
        i, j = 0, 0
        
        while count != j:
    
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                j += 1
            else:
                i+= 1
