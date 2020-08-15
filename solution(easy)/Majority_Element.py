# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.


#  Example 1:
# Input: [3,2,3]
# Output: 3
 
# Example 2:
# Input: [2,2,1,1,1,2,2]
# Output: 2


# Solution 1:

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = {}
        
        for i in range(len(nums)):
    
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
                
        return max(count ,key = count.__getitem__)



# Solution 2:

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        return max(set(nums),key=nums.count)
